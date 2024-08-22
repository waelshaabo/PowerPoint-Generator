from flask import Flask, request
from flask_cors import CORS
import traceback
import logging
from consts import PROMPT
import openai


openai.api_key = 'Put your openai API Key'

logger = logging.getLogger()

HOST = '0.0.0.0'
PORT = 8081

app = Flask(__name__)
CORS(app)

@app.route('/api/completion', methods=['POST'])
def completion():
    try:
        req = request.get_json()
        words = req.get('content')
        if not words:
            raise ValueError("No input word.")
        output = generate_text(words)
        print(output)
        return output, 200
    except Exception:
        logger.error(traceback.format_exc())
        return "Error", 500

def generate_text(content):
    try:
        # prompt = PROMPT + f"\n{content}"
        prompt = PROMPT.replace("{content}", content)

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
        
    except openai.error.OpenAIError as e:
        return f"OpenAI API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
