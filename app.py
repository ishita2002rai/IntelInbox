from flask import Flask, jsonify, render_template
from database import db

app = Flask(__name__)

@app.route('/summaries', methods=['GET'])
def fetch_summaries():
    """Fetches saved email summaries from Firestore."""
    summaries = []
    docs = db.collection("email_summaries").stream()

    for doc in docs:
        summaries.append(doc.to_dict())

    return jsonify(summaries)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
