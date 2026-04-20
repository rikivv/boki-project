from llm.client import LLMClient
from tools.executor import ToolExecutor
from integrations.google_calendar.client import GoogleCalendarClient
from config import NO_THINK
from tools.registry import TOOLS

from chat_instance import ChatInstance

chatInstance = ChatInstance()

if __name__ == "__main__":
    #print(client.build_tool_prompt(TOOLS))

    message = input("\nUser Prompt: ")
    print()
    print(chatInstance.history)
    message = {"role": "user", "content": "oi gente"}
    chatInstance.add_to_history(message)
    print(chatInstance.history)
    #response = chatInstance.send_message(message)
    #print(response)
    #print(toolExecutor.parse_tool_call(response["choices"][0]["message"]["content"]))

    