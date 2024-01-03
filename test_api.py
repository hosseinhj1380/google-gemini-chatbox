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
GOOGLE_API_KEY=os.environ.get("API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

response = model.generate_content("What is the meaning of life?")

to_markdown(response.text)