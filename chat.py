from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from weather import getTemperature
load_dotenv()

client = OpenAI()
# prompt = "whats your name?"

OpenAI.api_key = os.getenv('OPENAI_API_KEY')

messages = []

def set_system_prompt(prompt):
    '''
    set system prompt for chatgpt
    '''
    messages.append({"role": "system", "content": prompt})

def get_completion(prompt, client_instance=client, model="gpt-4o"):
    '''
    chat with gpt 
    '''
    messages.append({"role": "user", "content": prompt})
    response = client_instance.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=400,
    temperature=0,
    )
    return response.choices[0].message.content

# print(get_completion(prompt, client)) # call your function
