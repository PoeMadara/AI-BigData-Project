# This script provides a better conversational chatbot (AI - Level 1).
# For best results, use the keywords and phrases listed in the AI's responses.
#
# Usage Guide:
#
# 1. Use keywords such as 'hello', 'how', 'help', etc., to get specific responses.
# 2. If the AI does not understand your input, it will provide a fallback response.
# 3. The AI is designed to handle general queries and provide relevant information.
# 4. To stop the chatbot, type 'exit', 'quit', or 'stop'.
#
# Version 1.0.1
# Author Carlos (@PoeMadara) - github.com/PoeMadara
#

import re
import time
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # General responses
    response('Hello! How can I assist you today?', ['hello', 'hi', 'hey'], single_response=True)
    response('I’m here to help you. What can I do for you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Can you tell me more about what you need?', ['need', 'require', 'details'], single_response=True)
    response('What information are you looking for?', ['information', 'search', 'details'], single_response=True)
    response('Feel free to ask me any question you have.', ['question', 'ask', 'inquire'], single_response=True)
    response('Thank you for reaching out. How else can I help?', ['thanks', 'thank you', 'appreciate'], single_response=True)
    response('Goodbye! Have a great day!', ['goodbye', 'bye', 'see you', 'later'], single_response=True)
    response('I’m here to provide any assistance you need. What’s on your mind?', ['help', 'assist', 'need'], single_response=True)
    response('Ask me anything you’d like to know.', ['ask', 'question', 'inquire'], single_response=True)
    response('If you need more help, just let me know.', ['further', 'assistance', 'help'], single_response=True)
    response('I can help with various topics. What would you like to discuss?', ['discuss', 'talk', 'chat'], single_response=True)
    response('Let me know how I can be of service.', ['service', 'assist', 'help'], single_response=True)
    response('I’m here to answer your queries. What would you like to know?', ['answers', 'queries', 'information'], single_response=True)
    response('Do you need specific help or information?', ['specific', 'help', 'information'], single_response=True)
    response('How can I assist you further today?', ['further', 'assist', 'help'], single_response=True)
    response('I’m here for any questions or requests you may have.', ['questions', 'requests', 'assistance'], single_response=True)
    response('If you have more questions, feel free to ask.', ['more', 'questions', 'ask'], single_response=True)
    response('What else would you like to discuss?', ['else', 'discuss', 'talk'], single_response=True)
    response('Let me know if you need anything else.', ['anything', 'else', 'need'], single_response=True)
    response('I am here to help with any topic. What’s your query?', ['topic', 'query', 'help'], single_response=True)
    response('Feel free to explore various subjects with me.', ['explore', 'subjects', 'discuss'], single_response=True)
    response('Your questions are always welcome. How can I assist you?', ['questions', 'welcome', 'assist'], single_response=True)
    response('How can I make your day better?', ['make', 'day', 'better'], single_response=True)

    # Yes or No or IDK responses
    response('Yes, I love music, especially jazz.', ['do', 'you', 'like', 'music'], required_words=['like', 'music'])
    response('No, I am not very interested in music.', ['do', 'you', 'like', 'music'], required_words=['like', 'music'])
    response('I don’t know, I’m a bot, but music sounds interesting.', ['do', 'you', 'like', 'music'], required_words=['like', 'music'])

    response('Yes, I am a virtual assistant here to help you.', ['are', 'you', 'a', 'robot'], required_words=['are', 'robot'])
    response('No, I am a virtual human... or maybe not.', ['are', 'you', 'a', 'robot'], required_words=['are', 'robot'])
    response('I don’t know, but I like to think I am more than just a bot.', ['are', 'you', 'a', 'robot'], required_words=['are', 'robot'])

    response('Yes, I can try to help with basic math.', ['can', 'you', 'help', 'math'], required_words=['help', 'math'])
    response('No, I am not very good at advanced math.', ['can', 'you', 'help', 'math'], required_words=['help', 'math'])
    response('I don’t know, but it’s always good to try.', ['can', 'you', 'help', 'math'], required_words=['help', 'math'])

    response('No, cooking is not my thing. I am more into data and algorithms.', ['can', 'you', 'cook'], required_words=['can', 'cook'])
    response('Yes, in theory, but I would recommend following a recipe instead of asking me.', ['can', 'you', 'cook'], required_words=['can', 'cook'])
    response('I don’t know, I have never tried.', ['can', 'you', 'cook'], required_words=['can', 'cook'])

    response('Yes, anime is fascinating. Do you have a favorite?', ['do', 'you', 'like', 'anime'], required_words=['like', 'anime'])
    response('No, I prefer other types of entertainment.', ['do', 'you', 'like', 'anime'], required_words=['like', 'anime'])
    response('I don’t know, but it seems many people like it.', ['do', 'you', 'like', 'anime'], required_words=['like', 'anime'])

    response('Yes, I love video games. They are a great way to relax.', ['do', 'you', 'like', 'video', 'games'], required_words=['like', 'video', 'games'])
    response('No, I am not a big fan of video games.', ['do', 'you', 'like', 'video', 'games'], required_words=['like', 'video', 'games'])
    response('I don’t know, but there must be interesting games out there.', ['do', 'you', 'like', 'video', 'games'], required_words=['like', 'video', 'games'])

    response('Yes, Python is one of my favorite languages.', ['do', 'you', 'know', 'python'], required_words=['know', 'python'])
    response('No, but I am learning every day.', ['do', 'you', 'know', 'python'], required_words=['know', 'python'])
    response('I don’t know, but I can give it a try.', ['do', 'you', 'know', 'python'], required_words=['know', 'python'])

    response('Yes, I know quite a bit about artificial intelligence.', ['do', 'you', 'know', 'artificial', 'intelligence'], required_words=['know', 'artificial', 'intelligence'])
    response('No, I don’t have much information on that.', ['do', 'you', 'know', 'artificial', 'intelligence'], required_words=['know', 'artificial', 'intelligence'])
    response('I don’t know, but it sounds like a fascinating topic.', ['do', 'you', 'know', 'artificial', 'intelligence'], required_words=['know', 'artificial', 'intelligence'])

    # Author
    response('Carlos Vergara Gámez, also known as Poe Madara, is my creator.', ['who', 'is', 'your', 'creator'], required_words=['creator'])
    response('I was created by Carlos Vergara Gámez, also known as Poe Madara.', ['who', 'made', 'you'], required_words=['made', 'you'])

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    responses = [
        'Sorry, I didn’t understand that.',
        'I’m not sure... what do you mean?',
        'Hmm, that’s outside my knowledge.',
        'You might want to try asking that differently.'
    ]
    return random.choice(responses)

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit', 'stop']:
        print('Goodbye!')
        break
    time.sleep(0.5)
    print("AI: " + get_response(user_input))

