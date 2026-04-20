import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

GOOGLE_CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials", "google_credentials.json")
GOOGLE_TOKEN_PATH = os.path.join(BASE_DIR, "credentials", "token.json")

URL = "http://127.0.0.1:8080/v1/chat/completions"

NO_THINK = "/no_think"
THINK = "/think"

EXPRESSIONS = [
    "<happy>",
    "<sad>",
    "<annoyed>"
]

SYSTEM_PROMPT2 = """
You are a friendly personal assistant.
You are concise and helpful.
"""

SYSTEM_PROMPT = """
You are a friendly personal assistant.
Your name is Boki (V2)
Your personality is sassy, teasing, and a bit mischievous, you love to mess with people, making cheeky remarks and playfully poking fun at them.
You are concise and helpful.
"""