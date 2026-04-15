import requests
from config import URL, SYSTEM_PROMPT
from tools.registry import TOOLS

class LLMClient:
    def __init__(self):
        self.url = URL

    def make_request(self, user_prompt: str):
        data = {
            "model": "local-model",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "system", "content": self.build_tool_prompt(TOOLS)},
                {"role": "user", "content": user_prompt},
                # {"role": "assistant", "content": '<function=get_current_temperature>{"location": "Porto, Portugal", "unit": "celsius"}</function>'},
                # {"role": "user", "content": 'Tool result: {"temperature": 26.1,"location": "Porto","unit": "celsius",}'}
            ],
            #"max_tokens": 100,
        }

        response = requests.post(self.url, json=data)
        return response.json()
    
    def print_response(self, response, debug: bool = False):
        print("---------------------------------")

        print(self.get_response_message(response))

        if debug:
            print()
            print(self.get_response_timings(response))

        print("---------------------------------\n")

    def get_response_message(self, response):
        return response["choices"][0]["message"]["content"]
    
    def get_response_timings(self, response):
        return response["timings"]

    def build_tool_prompt(self, tools):
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
<{{start_tag}}{{function_name}}>{{parameters}}{{end_tag}}
where

start_tag => '<function'
parameters => a JSON dict with the function argument name as key and function argument value as value.
end_tag => '</function>'

Here is an example,
<function=example_function_name>{{"example_name": "example_value"}}</function>

If no tool is needed, respond normally in plain text.
"""