import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
# from google.colab import
from dotenv import load_dotenv
import os 
load_dotenv()

from IPython.display import display , Markdown


GOOGLE_API_KEY=os.environ.get("API_KEY")


class GenAi :
    def __init__(self) -> None:
        pass

    def to_markdown(self,text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    def chat(self,message):
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        response = chat.send_message(str(message))
        # self.to_markdown(response.text)
        return( response.text)
        
    def stream_chat(self,message):
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message, stream=True)
        for chunk in response:
            return(chunk.text)  
            


