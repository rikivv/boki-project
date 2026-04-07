import requests
from tools import tools

url = "http://127.0.0.1:8080/v1/chat/completions"


system_prompt = """
You are a friendly personal assistant.
You are concise and helpful.
"""


def build_tool_prompt(tools):
    tool_descriptions = ""
    args_desc = "no arguments"

    for name, tool in tools.items():
        args = tool.get("arguments", {})

        if args:
            args_desc = ", ".join([f"{k}: {v}" for k, v in args.items()])
        tool_descriptions += f"- {name}({args_desc}): {tool['description']}\n"

    return f"""
You have access to the following tools:

{tool_descriptions}

Decide whether a tool is necessary to answer the user's request.

- Only use a tool if it is clearly required to provide the answer.
- If the request can be answered directly with your own knowledge, DO NOT use a tool.
- Do NOT force tool usage.

If you choose to use a tool, respond ONLY with valid JSON in this format:
{{
    "tool": "tool_name",
    "arguments": {{
        "arg1": "value"
    }}
}}

If no tool is needed, respond normally in plain text.
"""


def getRequest():
    user_prompt = "what day is it?"

    data = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": build_tool_prompt(tools)},
            {"role": "user", "content": user_prompt},
        ],
        #"max_tokens": 100,
    }

    request = requests.post(url, json=data)

    request_response = request.json()

    print(f"User Prompt: {user_prompt}\n")
    print("---------------------------------\n")
    print(request_response["choices"][0]["message"]["content"])
    print()
    print(request_response["timings"])

if __name__ == "__main__":
    getRequest()