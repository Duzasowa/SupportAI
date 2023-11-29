from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Load FAQ data from a JSON file on server start
with open('FAQ.json', 'r', encoding='utf-8') as faq_file:
    faq_data = json.load(faq_file)

def search_faq(question):
    """
    Search for an answer in the FAQ data.
    This function converts the question to lowercase and checks if any of the keywords
    in each FAQ entry match a part of the user's question.
    Returns the plain text answer if a match is found; otherwise, returns None.
    """
    question = question.lower()
    for entry in faq_data:
        if any(keyword.lower() in question for keyword in entry['Keywords']):
            return entry['Answer_plain_text']
    return None

def ask_chatgpt(question):
    """
    Makes a request to the OpenAI ChatGPT API.
    It sends the user's question and returns the API's response.
    If the API call is successful, it returns the content of the response;
    otherwise, it returns an error message.
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # Replace with your actual API key
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error when calling the ChatGPT API."

@app.route('/')
def index():
    """
    Route for the main page.
    Renders the index.html template which contains the form for user's question.
    """
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def get_answer():
    """
    Route to handle the form submission.
    When the user submits a question, this route first searches the FAQ,
    and if no answer is found, it makes a request to the ChatGPT API.
    It then renders the same index.html template with the answer.
    """
    question = request.form['question']

    # First, search the FAQ for an answer
    answer = search_faq(question)

    # If no answer is found in the FAQ, call the ChatGPT API
    if not answer:
        answer = ask_chatgpt(question)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development purposes
