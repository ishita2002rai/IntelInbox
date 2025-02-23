# InboxIntel - AI Email Summarizer

InboxIntel is an AI-powered email summarization tool that helps users quickly understand their emails without reading lengthy content. Using Google Gemini AI, it extracts key points and displays them in a structured, interactive UI. The tool allows users to mark emails as Read or Read Later, optimizing productivity and workflow.

---

## Features
- Fetches Gmail Emails - Retrieves only today's emails from the Primary inbox using the Gmail API.  
- AI-Powered Summarization - Uses Google Gemini AI to summarize emails into bullet points.  
- Interactive UI - Displays email summaries in an intuitive interface.  
- Read & Read Later - Mark emails as Read (removes from the list) or Read Later (highlights in blue).  
- Smooth Animations - Includes hover effects and slide transitions for a clean UI experience.  
- Secure & Private - Stores no email content; works with Firebase to manage data securely.  

---

## UI Screenshots
![image](https://github.com/user-attachments/assets/438046e5-65d5-45d5-823d-8d1241059622)
![image](https://github.com/user-attachments/assets/575a341c-0ee9-4ace-be4e-079b6d1f8746)

---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/ishita2002rai/IntelInbox.git
cd IntelInbox
```

### Create a Virtual Environment & Activate It
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project directory:
```ini
GEMINI_KEY=your-gemini-api-key
GMAIL_API=credentials.json
FIREBASE_CREDENTIALS=firebase_credentials.json
```
Ensure you have placed `credentials.json` (for Gmail API) and `firebase_credentials.json` (for Firestore) in the project folder.

---

## How to Run the Project
### Start the Backend (Flask Server)
```bash
python app.py
```
The server will start at: `http://127.0.0.1:5000/`

### Open the Frontend
Open a browser and go to:
```
http://127.0.0.1:5000/
```

You will see the AI-generated email summaries.

---

## Technologies Used
- Backend: Flask (Python), Gmail API, Firebase Firestore
- Frontend: HTML, CSS, Bootstrap, JavaScript
- AI Model: Google Gemini AI
- Authentication: Google OAuth 2.0
- Database: Firestore (for storing user email preferences)

---

## Security Considerations
- No email content is stored – AI summaries are generated in real-time.
- Environment variables protect API keys – credentials are not exposed in code.
- Uses Google OAuth – Ensures secure authentication.

---

## Future Enhancements
- Deploy to Railway / Render for public access.
- Add priority email detection (important vs. spam classification).
- Support Outlook emails in addition to Gmail.
- Implement multi-language support for email summaries.

---

## Contributing
Want to improve InboxIntel? Follow these steps:
1. Fork the repo  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m "Added new feature"`)  
4. Push to GitHub (`git push origin feature-name`)  
5. Create a pull request  

---

## License
This project is open-source under the MIT License.

