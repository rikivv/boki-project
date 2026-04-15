import requests
from tools import TOOLS

#TODO: Change format specification to match https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/
url = "http://127.0.0.1:8080/v1/chat/completions"


SYSTEM_PROMPT = """
You are a friendly personal assistant.
You are concise and helpful.
"""

NO_THINK = "/no_think"
THINK = "/think"


def build_tool_prompt(tools):
    tool_descriptions = ""

    for tool in tools:
        tool_descriptions += f"- {tool}\n"

    return f"""
You have access to the following tools:

{tool_descriptions}

Decide whether a tool is necessary to answer the user's request.

- Only use a tool if it is clearly required to provide the answer.
- If the request can be answered directly with your own knowledge, DO NOT use a tool.
- Do NOT force tool usage.

If a you choose to call a function ONLY reply in the following format:
<{{start_tag}}={{function_name}}>{{parameters}}{{end_tag}}
where

start_tag => '<function'
parameters => a JSON dict with the function argument name as key and function argument value as value.
end_tag => '</function>'

Here is an example,
<function=example_function_name>{{"example_name": "example_value"}}</function>

If no tool is needed, respond normally in plain text.
"""


def make_request(user_prompt: str):

    data = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": build_tool_prompt(TOOLS)},
            {"role": "user", "content": user_prompt},
        ],
        #"max_tokens": 100,
    }

    request = requests.post(url, json=data)

    request_response = request.json()

    print("---------------------------------\n")
    print(request_response["choices"][0]["message"]["content"])
    print()
    print(request_response["timings"])


def send_message(input: str):

    input = input.strip()
    input = input + " " + NO_THINK

    make_request(input)


if __name__ == "__main__":
    #print(build_tool_prompt(TOOLS))
    #get_request()
    message = input("User Prompt: ")
    send_message(message)