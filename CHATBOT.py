import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import random
import json
import pickle
from termcolor import colored
from pyfiglet import figlet_format
from tabulate import tabulate
import re

# Create a dictionary to store the chatbot's responses
responses = [
    (
        r"hi|hello|hey",
        [colored("Hello! How can I assist you today?", "green"),
         colored("Hi there! What can I do for you?", "blue"),
        colored("Hey! What's on your mind today?", "green")]
    ),
    (
        r"what is your name ?",
        [colored("I am a chatbot created to assist you. You can call me Chatbot.", "blue"),
         colored("I'm Chatbot, your friendly assistant!", "green")]
    ),
    (
        r"how are you ?",
        [colored("I'm just code, but I'm doing well! How about you?", "blue"),
         colored("I'm functioning well, thanks! How can I help you today?", "green")]
    ),
    (
        r"what's your name",
        [colored("I go by ChatBot! How can I assist you today?", "cyan")]
    ),
    (
        r"what can you do ?",
        [colored("I can chat with you, answer questions, and assist with basic tasks.", "blue"),
         colored("I'm here to help you with whatever you need!", "green")]
    ),
    (
        r"who created you ?",
        [colored("I was created by a team of developers using NLP techniques.", "blue")]
    ),
    (
        r"what is your purpose ?",
        [colored("My purpose is to assist, chat, and provide useful information to you.", "green")]
    ),
    (
        r"what is python ?",
        [colored("Python is a versatile programming language known for its ease of use.", "blue"),
         colored("Python is a powerful, high-level programming language.", "green")]
    ),
    (
        r"tell me a joke",
        [colored("Why don't programmers like nature? It has too many bugs!", "blue"),
         colored("How many programmers does it take to change a light bulb? None, that's a hardware problem!", "green")]
    ),
    (
        r"bye|goodbye|see you",
        [colored("Goodbye! Have a fantastic day!", "blue"),
         colored("See you later! Take care!", "green")]
    ),
    (
        r"(.*)",
        [colored("I'm not sure how to respond to that. Could you please ask something else?", "blue"),
         colored("That's interesting! Tell me more.", "green"),
         colored("Let's talk about something else.", "blue")]
    ),
]

# Create a function to process the user's input
def process_input(input_text):
    # Tokenize the input text
    tokens = nltk.word_tokenize(input_text)

    # Stem the tokens
    stemmed_tokens = [stemmer.stem(token.lower()) for token in tokens]

    # Check if the input matches any of the chatbot's responses
    for response in responses:
        for token in stemmed_tokens:
            if re.search(response[0], token, re.IGNORECASE):
                return random.choice(response[1])

    # If no match is found, return a default response
    return colored("I'm not sure what you mean. Can you please rephrase your question?", "blue")

# Create a function to display the chatbot's interface
def display_interface():
    print(colored(figlet_format("Chatbot", font="slant"), "cyan"))
    print(colored("Chatbot: Chatbot is ready! Type your message: ", attrs=['bold']))

# Display the chatbot's interface
display_interface()

while True:
    # Get the user's input
    input_text = input(colored("You: ", attrs=['bold'])).strip().lower()

    # Check if the user wants to quit
    if input_text == 'quit':
        print(colored("Chatbot: Goodbye!", attrs=['bold']))
        break

    # Process the user's input
    response = process_input(input_text)

    # Display the chatbot's response
    print(colored(f"Chatbot: {response}", attrs=['bold']))

    # Display responses in a table format for specific questions
    if response in [
        "I'm just code, but I'm doing well! How about you?",
        "I'm functioning well, thanks! How can I help you today?"
    ]:
        print(tabulate([["How are you?", response]], headers=["Question", "Response"], tablefmt="grid"))
