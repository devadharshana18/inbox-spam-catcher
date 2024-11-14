# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

SPAM_KEYWORDS = ['free', 'win', 'money', 'lottery', 'prize', 'click', 'call now']

def is_spam(text):
    text = text.lower()
    return any(word in text for word in SPAM_KEYWORDS)

@app.route('/api/check-spam', methods=['POST'])
def check_spam():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    result = is_spam(data['text'])
    return jsonify({
        'isSpam': result,
        'message': 'Spam' if result else 'Not Spam'
    })

if __name__ == '__main__':
    app.run(debug=True)