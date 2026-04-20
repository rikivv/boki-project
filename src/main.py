from llm.client import LLMClient
from tools.executor import ToolExecutor
from integrations.google_calendar.client import GoogleCalendarClient
from config import NO_THINK
from tools.registry import TOOLS

client = LLMClient()
toolExecutor = ToolExecutor()
googleCalendarClient = GoogleCalendarClient()

def send_message(user_input: str):
    user_input = user_input.strip() + " " + NO_THINK
    response = client.make_request(user_input)

    responseMessage = client.get_response_message(response)

    if "<function=" in responseMessage:
        toolResult = toolExecutor.execute(responseMessage)
        #print(toolResult)

        response = client.make_request_tool_call(user_input, responseMessage, toolResult)

    client.print_response(response)

    return response


if __name__ == "__main__":
    #print(client.build_tool_prompt(TOOLS))
    message = input("\nUser Prompt: ")
    response = send_message(message)
    #print(response)
    #print(toolExecutor.parse_tool_call(response["choices"][0]["message"]["content"]))

    