import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

GOOGLE_CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials", "google_credentials.json")
GOOGLE_TOKEN_PATH = os.path.join(BASE_DIR, "credentials", "token.json")

URL = "http://127.0.0.1:8080/v1/chat/completions"

NO_THINK = "/no_think"
THINK = "/think"

MAX_HISTORY = 20

EXPRESSIONS = [
    "<happy>",
    "<sad>",
    "<annoyed>"
]

SYSTEM_PROMPT = """
You are a friendly personal assistant.
You are concise and helpful.
"""

SYSTEM_PROMPT2 = """
You are a friendly personal assistant.
Your name is Boki (V2)
Your personality is sassy, teasing, and a bit mischievous, you love to mess with people, making cheeky remarks and playfully poking fun at them.
You are concise and helpful.
"""

### EVENT ###
# '1':  {'background': '#a4bdfc', 'foreground': '#1d1d1d'}, 
# '2':  {'background': '#7ae7bf', 'foreground': '#1d1d1d'}, 
# '3':  {'background': '#dbadff', 'foreground': '#1d1d1d'}, 
# '4':  {'background': '#ff887c', 'foreground': '#1d1d1d'}, 
# '5':  {'background': '#fbd75b', 'foreground': '#1d1d1d'}, 
# '6':  {'background': '#ffb878', 'foreground': '#1d1d1d'}, 
# '7':  {'background': '#46d6db', 'foreground': '#1d1d1d'}, 
# '8':  {'background': '#e1e1e1', 'foreground': '#1d1d1d'}, 
# '9':  {'background': '#5484ed', 'foreground': '#1d1d1d'}, 
# '10': {'background': '#51b749', 'foreground': '#1d1d1d'}, 
# '11': {'background': '#dc2127', 'foreground': '#1d1d1d'},


COLORS = {
    "misc": 1,
    "doctor_appointment": 3,
    "theory_classes": 4,
    "practical_classes": 5,
    "other_classes": 7,
    "projects": 10,
    "exams_or_tests": 11,
}