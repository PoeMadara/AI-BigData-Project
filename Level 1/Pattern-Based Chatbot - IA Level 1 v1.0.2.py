import re
import time
import random

def normalize_words(words):

    normalization_dict = {
        'music': ['music', 'tunes', 'songs', 'melodies'],
        'anime': ['anime', 'manga', 'japanese animation', 'japanese cartoons'],
        'video games': ['video games', 'games', 'gaming', 'videogames', 'videogame'],
        'python': ['python', 'python language', 'py'],
        'ai': ['ai', 'artificial intelligence', 'machine learning'],
        'help': ['help', 'assist', 'support', 'aid'],
        'thank you': ['thank you', 'thanks', 'appreciate', 'grateful'],
        'goodbye': ['goodbye', 'bye', 'see you', 'later'],
        'question': ['question', 'query', 'inquire'],
        'information': ['information', 'details', 'data'],
        'assist': ['assist', 'help', 'aid', 'support'],
        'discuss': ['discuss', 'talk', 'chat'],
        'further': ['further', 'more', 'additional'],
        'service': ['service', 'assist', 'help'],
        'topic': ['topic', 'subject', 'theme'],
        'explore': ['explore', 'investigate', 'look into'],
        'make': ['make', 'improve', 'enhance'],
        'day': ['day', 'time', 'period'],
        'better': ['better', 'improved', 'enhanced']
    }

    normalized_input = []
    for word in words:
        found = False
        for key, synonyms in normalization_dict.items():
            if word in synonyms:
                normalized_input.append(key)
                found = True
                break
        if not found:
            normalized_input.append(word)
    return normalized_input


def get_response(input_text):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', input_text.lower())
    normalized_message = normalize_words(split_message)
    response = check_all_messages(normalized_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []

    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words)) if recognized_words else 0

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

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob
        prob = message_probability(message, list_of_words, single_response, required_words)
        if prob > 0:
            highest_prob[bot_response] = prob

    # General responses
    response(
        'Hello! How can I assist you today?', ['hello', 'hi', 'hey'], single_response=True
    )
    response(
        'I’m here to help you. What can I do for you?', ['how', 'are', 'you', 'doing'],
        required_words=['how']
    )
    response(
        'Can you tell me more about what you need?', ['need', 'require', 'details'],
        single_response=True
    )
    response(
        'What information are you looking for?', ['information', 'search', 'details'],
        single_response=True
    )
    response(
        'Feel free to ask me any question you have.', ['question', 'ask', 'inquire'],
        single_response=True
    )
    response(
        'Thank you for reaching out. How else can I help?', ['thanks', 'thank you', 'appreciate'],
        single_response=True
    )
    response(
        'Goodbye! Have a great day!', ['goodbye', 'bye', 'see you', 'later'],
        single_response=True
    )
    response(
        'I’m here to provide any assistance you need. What’s on your mind?', ['help', 'assist', 'need'],
        single_response=True
    )
    response(
        'Ask me anything you’d like to know.', ['ask', 'question', 'inquire'],
        single_response=True
    )
    response(
        'If you need more help, just let me know.', ['further', 'assistance', 'help'],
        single_response=True
    )
    response(
        'I can help with various topics. What would you like to discuss?', ['discuss', 'talk', 'chat'],
        single_response=True
    )
    response(
        'Let me know how I can be of service.', ['service', 'assist', 'help'],
        single_response=True
    )
    response(
        'I’m here to answer your queries. What would you like to know?', ['answers', 'queries', 'information'],
        single_response=True
    )
    response(
        'Do you need specific help or information?', ['specific', 'help', 'information'],
        single_response=True
    )
    response(
        'How can I assist you further today?', ['further', 'assist', 'help'],
        single_response=True
    )
    response(
        'I’m here for any questions or requests you may have.', ['questions', 'requests', 'assistance'],
        single_response=True
    )
    response(
        'If you have more questions, feel free to ask.', ['more', 'questions', 'ask'],
        single_response=True
    )
    response(
        'What else would you like to discuss?', ['else', 'discuss', 'talk'],
        single_response=True
    )
    response(
        'Let me know if you need anything else.', ['anything', 'else', 'need'],
        single_response=True
    )
    response(
        'I am here to help with any topic. What’s your query?', ['topic', 'query', 'help'],
        single_response=True
    )
    response(
        'Feel free to explore various subjects with me.', ['explore', 'subjects', 'discuss'],
        single_response=True
    )
    response(
        'Your questions are always welcome. How can I assist you?', ['questions', 'welcome', 'assist'],
        single_response=True
    )
    response(
        'How can I make your day better?', ['make', 'day', 'better'],
        single_response=True
    )

    # Topic-specific responses with follow-ups
    response(
        'Yes, I love music, especially jazz. What about you? What kind of music do you like?',
        ['music'], required_words=['music']
    )
    response(
        'Music is a great way to relax. Do you have a favorite band or artist?',
        ['favorite', 'band', 'artist'], required_words=['favorite', 'band', 'artist']
    )
    response(
        'That’s interesting! What genre of music do you listen to the most?',
        ['genre', 'music', 'listen'], required_words=['genre', 'music']
    )

    response(
        'Yes, anime is fascinating. Do you have a favorite series or character?',
        ['anime'], required_words=['anime']
    )
    response(
        'Anime can be really diverse. What genre do you enjoy most?',
        ['genre', 'anime', 'enjoy'], required_words=['genre', 'anime']
    )
    response(
        'I’d love to hear more about your favorite anime! What’s it about?',
        ['favorite', 'anime', 'about'], required_words=['favorite', 'anime']
    )

    response(
        'Yes, I love video games. They are a great way to relax. What games do you enjoy?',
        ['video games'], required_words=['video games']
    )
    response(
        'Video games can be a lot of fun! What kind of games do you like? RPG, action, shooters, puzzles, or sports?',
        ['like', 'rpg', 'action', 'shooters', 'puzzles', 'sports', 'games'], required_words=['like', 'games']
    )
    response(
        'That’s cool! Have you tried any new games recently?',
        ['new', 'games', 'recently'], required_words=['new', 'games']
    )

    response(
        'Yes, Python is one of my favorite languages. Are you working on any projects with it?',
        ['python'], required_words=['python']
    )
    response(
        'Python is quite versatile. What do you like most about it?',
        ['versatile', 'like', 'python'], required_words=['versatile', 'like', 'python']
    )
    response(
        'I’d be interested to know more about your Python projects. What are you building?',
        ['projects', 'building', 'python'], required_words=['projects', 'python']
    )

    response(
        'Yes, I know quite a bit about artificial intelligence. Are you interested in any specific aspect?',
        ['artificial intelligence', 'ai'], required_words=['artificial intelligence']
    )
    response(
        'AI is a broad field. What areas of AI are you most curious about?',
        ['areas', 'ai', 'curious'], required_words=['areas', 'ai']
    )
    response(
        'I’d love to discuss more about AI. What topics interest you?',
        ['discuss', 'ai', 'topics'], required_words=['discuss', 'ai']
    )

    # Author
    response(
        'Carlos Vergara Gámez, also known as Poe Madara, is my creator.', ['who', 'is', 'your', 'creator'],
        required_words=['creator']
    )
    response(
        'I was created by Carlos Vergara Gámez, also known as Poe Madara.', ['who', 'made', 'you'],
        required_words=['made', 'you']
    )

    if highest_prob:
        best_match = max(highest_prob, key=highest_prob.get)
        return best_match
    else:
        return unknown()


def unknown():
    responses = [
        'Sorry, I did not understand that.',
        'I’m not sure... what do you mean?',
        'Hmm, that’s outside my knowledge.',
        'You might want to try asking that differently.'
    ]
    return random.choice(responses)


while True:
    input_text = input('You: ')
    if input_text.lower() in ['exit', 'quit', 'stop']:
        print('Goodbye!')
        break

    time.sleep(0.5)
    print("AI: " + get_response(input_text))
