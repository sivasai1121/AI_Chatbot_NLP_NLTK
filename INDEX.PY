# nltk_chatbot.py
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a simple NLP chatbot using NLTK."]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thanks for asking!", "I'm fine. How about you?"]
    ],
    [
        r"what can you do ?",
        ["I can answer simple questions, greet you, and be your chat companion."]
    ],
    [
        r"who created you ?",
        ["I was created using Python and the NLTK library."]
    ],
    [
        r"(.*) your creator ?",
        ["My creator is a Python developer interested in NLP."]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn’t understand that. Can you rephrase?"]
    ]
]

# Create chatbot
def start_chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chatbot()
