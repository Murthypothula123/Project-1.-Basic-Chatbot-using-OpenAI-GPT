# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16kXjEfYUEmQugXKx3ofqplN4Cs_u0aYG
"""

!pip install openai

# Commented out IPython magic to ensure Python compatibility.
# %env OPENAI_API_KEY=your_key_here

import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your actual key

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change to "gpt-4" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

print("Welcome to the GPT Chatbot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    reply = chat_with_gpt(user_input)
    print("AI:", reply)

!python basic_chatbot.py

# Commented out IPython magic to ensure Python compatibility.
from IPython import get_ipython
from IPython.display import display
# %%
!pip install openai

# %%
# %env OPENAI_API_KEY=your_key_here
# %%
import openai
import os

# Initialize the OpenAI client with the API key
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def chat_with_gpt(prompt):
    # Use the new syntax for creating chat completions
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change to "gpt-4" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # The response object structure has also changed slightly
    return response.choices[0].message.content

print("Welcome to the GPT Chatbot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    reply = chat_with_gpt(user_input)
    print("AI:", reply)