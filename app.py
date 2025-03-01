import os

import dotenv
from flask import Flask, render_template, jsonify, request
import openai
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

openai.api_key =  os.getenv("OPENAI_API_KEY")

flashcards = [
    {'question': 'Що таке Python?',
     'answer': 'Python — це мова програмування високого рівня, з акцентом на читабельність коду.'},
    {'question': 'Що таке Flask?', 'answer': 'Flask — це мікрофреймворк для розробки веб-додатків на Python.'},
    {'question': 'Що таке Git?',
     'answer': 'Git — це система контролю версій, яка дозволяє відслідковувати зміни у файлах.'},
]


@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards)


@app.route('/ask_openai', methods=['POST'])
def ask_openai():
    question = request.form['question']


    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=100
        )
        return jsonify({'answer': response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
