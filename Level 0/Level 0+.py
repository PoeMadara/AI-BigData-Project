#
# This script provides a very basic conversational AI in the form of a chatbot (AI - Level 0).
# For best results, use the keywords and phrases listed in the chatbot's responses.
#
# Usage Guide:
#
# 1. Use keywords such as 'hello', 'how', 'where', etc., to get specific responses.
# 2. If the chatbot does not understand your input, it will ask for clarification.
# 3. The chatbot is generic and designed for basic interactions.
# 4. To stop the chatbot, type 'exit', 'quit', or 'stop'.
#
# Author Carlos (@PoeMadara) - github.com/PoeMadara
#

import re
import time
import random

# Dictionary of keywords and possible responses
responses = {
    'hello': ['Hello!', 'Hi there!', 'Greetings!'],
    'how': ['I’m here to help. How can I assist?', 'I’m fine! How can I help you today?'],
    'thanks': ['You’re welcome!', 'No problem!', 'Glad to help!'],
    'bye': ['Goodbye!', 'See you later!', 'Take care!'],
    'help': ['I can help. What do you need?', 'Sure! What’s your question?', 'How can I help you today?'],
}

def get_response(user_input):
    """
    1. Split user input into words using regex.
       - re.findall(r'\b\w+\b', text) finds all words in the input
         * \b   : word boundary (start/end of a word)
         * \w+  : one or more letters, digits, or underscore
    2. Check if any word matches a keyword in the responses dictionary.
    3. Return a random response if a keyword is found.
    4. Otherwise, return a default message.
    """
    words = re.findall(r'\b\w+\b', user_input.lower())
    for word in words:
        if word in responses:
            return random.choice(responses[word])
    return "I don’t understand. Can you clarify?"

# Main chat loop
while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit', 'stop']:
        print('Chatbot: Goodbye!')
        break
    time.sleep(0.5)
    print("Chatbot: " + get_response(user_input))