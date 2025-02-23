import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

# Firestore database instance
db = firestore.client()

def save_summary(sender, subject, summary):
    """Saves email summaries to Firestore."""
    doc_ref = db.collection("email_summaries").add({
        "sender": sender,
        "subject": subject,
        "summary": summary
    })
    print("Summary saved:", doc_ref)

# Example usage
#if __name__ == "__main__":
    #save_summary("John Doe", "Project Update", "Decided to launch the product on April 15.")
