from llm.client import LLMClient
from tools.executor import ToolExecutor
from config import NO_THINK

client = LLMClient()
toolExecutor = ToolExecutor()

def send_message(user_input: str):
    user_input = user_input.strip() + " " + NO_THINK
    response = client.make_request(user_input)

    # responseMessage = client.get_response_message(response)

    # if "<function=" in responseMessage:
    #     print("opa tem coisa aki!!")
    #     # toolExecutor.execute

    client.print_response(response)

    return response


if __name__ == "__main__":
    message = input("\nUser Prompt: ")
    response = send_message(message)
    #print(response)
    #print(toolExecutor.parse_tool_call(response["choices"][0]["message"]["content"]))

    