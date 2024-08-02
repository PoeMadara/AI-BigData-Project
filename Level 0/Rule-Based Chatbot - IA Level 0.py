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

responses = {
    'hello': 'Hello! How can I assist you today?',
    'hi': 'Hi there! What can I do for you?',
    'greetings': 'Greetings! How can I help you?',
    'hey': 'Hey! What’s on your mind?',
    'how': 'I’m here to help. How can I assist you?',
    'are': 'I’m doing great! How can I assist you today?',
    'you': 'I’m here to assist you. What do you need help with?',
    'feeling': 'I’m just a bot, but I’m here to help! How can I assist?',
    'where': 'I’m right here, ready to assist you. What do you need?',
    'location': 'I’m available wherever you are. How can I help?',
    'question': 'Feel free to ask any questions you have.',
    'search': 'What are you searching for? I’m here to help.',
    'thank': 'You’re welcome! If you need anything else, just ask.',
    'goodbye': 'Goodbye! Have a great day!',
}

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    for word in split_message:
        if word in responses:
            return responses[word]
    return 'I’m not sure how to respond to that. Can you please clarify?'

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit', 'stop']:
        print('Chatbot: Goodbye! Have a great day!')
        break
    time.sleep(0.5)
    print("Chatbot: " + get_response(user_input))
