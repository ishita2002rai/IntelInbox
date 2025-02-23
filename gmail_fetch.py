import os
import pickle
import base64
from datetime import datetime, timedelta
import pytz  # For timezone conversion

import google.generativeai as genai
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from database import save_summary  # Import Firebase function

# ✅ Set Gemini API Key securely (Replace with your actual key)
genai.configure(api_key="YOUR_API_KEY")

# ✅ Gmail API Scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def authenticate_gmail():
    """Authenticates with Gmail API."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def fetch_todays_emails():
    """Fetches all emails received today in the Primary inbox."""
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    # ✅ Get today's date in Indian Standard Time (IST)
    ist = pytz.timezone('Asia/Kolkata')
    today = datetime.now(ist).strftime('%Y/%m/%d')

    #  Gmail query to fetch emails from today in the "Primary" category
    query = "category:primary newer_than:1d"


    # ✅ Fetch all today's emails (no limit)
    all_messages = []
    results = service.users().messages().list(userId='me', q=query).execute()

    while 'messages' in results:
        all_messages.extend(results['messages'])
        if 'nextPageToken' in results:
            results = service.users().messages().list(userId='me', q=query,
                                                      pageToken=results['nextPageToken']).execute()
        else:
            break

    email_texts = []
    for msg in all_messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data.get('payload', {})
        headers = payload.get('headers', [])

        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
        sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")

        email_body = None
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                    email_body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    break
        elif 'body' in payload and 'data' in payload['body']:
            email_body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')

        if email_body:
            email_texts.append({"from": sender, "subject": subject, "body": email_body})

    return email_texts


def summarize_email(email_text):
    """Uses Google Gemini AI to summarize an email."""
    model = genai.GenerativeModel("gemini-pro")  # ✅ Use Gemini Pro model
    response = model.generate_content(f"Summarize the key points and action items from this email: {email_text}")

    return response.text if response.text else "No summary available"


if __name__ == "__main__":
    emails = fetch_todays_emails()

    if not emails:
        print("❌ No emails found in Primary inbox for today (IST).")

    for email in emails:
        summary = summarize_email(email['body'])
        print("\n📩 **Email from {}**".format(email['from']))
        print(f"📌 **Subject:** {email['subject']}")
        print(f"📝 **Summary:** {summary}")

        # ✅ Store real summaries in Firebase
        save_summary(email['from'], email['subject'], summary)
