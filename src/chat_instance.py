from llm.client import LLMClient
from tools.executor import ToolExecutor
from integrations.google_calendar.client import GoogleCalendarClient
from config import NO_THINK
from tools.registry import TOOLS

client = LLMClient()
toolExecutor = ToolExecutor()

class ChatInstance:
    def __init__(self):
        self.history = []
    
    def send_message(self, user_input: str):
        user_input = user_input.strip()
        response = client.make_request(user_input)

        responseMessage = client.get_response_message(response)

        if "<function=" in responseMessage:
            toolResult = toolExecutor.execute(responseMessage)
            #print(toolResult)

            response = client.make_request_tool_call(user_input, responseMessage, toolResult)

        client.print_response(response, True)

        return response

    def add_to_history(self, message):
        self.history.append(message)