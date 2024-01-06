import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
# from google.colab import
from dotenv import load_dotenv
import os 
load_dotenv()

from IPython.display import display
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=os.environ.get("AIzaSyANjL6qLDhj75XCQ6GRyEkVm527QwzljzQ")

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def sart():

  genai.configure(api_key="AIzaSyANjL6qLDhj75XCQ6GRyEkVm527QwzljzQ")
  model = genai.GenerativeModel('gemini-pro')
  chat = model.start_chat(history=[])
  response = chat.send_message("what is my name ?")
  print(response.text)
  
  


sart()