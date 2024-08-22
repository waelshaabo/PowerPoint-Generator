import json
import os

from slide_deck import SlideDeck
from llm_call import chat_completion_request

FOLDER = "generated"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def generate_json_list_of_slides(content):
    try:
        resp = chat_completion_request(content)
        print("Raw response:", resp)  # Debug print
        if not resp.strip():
            raise ValueError("Empty response from LLM")
        obj = json.loads(resp.replace("```json","").replace("```",""))
        return obj
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Response content: {resp}")
        raise
    except Exception as e:
        print(f"Error in generate_json_list_of_slides: {e}")
        raise

def generate_presentation(content, template_option):
    deck = SlideDeck(template_option)
    slides_data = generate_json_list_of_slides(content)
    title_slide_data = slides_data[0]
    slides_data = slides_data[1:]
    return deck.create_presentation(title_slide_data, slides_data)