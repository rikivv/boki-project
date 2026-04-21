from datetime import datetime, timezone

from llm.client import LLMClient
from tools.executor import ToolExecutor
from integrations.google_calendar.client import GoogleCalendarClient
from config import NO_THINK, SYSTEM_PROMPT, MAX_HISTORY
from tools.registry import TOOLS

client = LLMClient()
toolExecutor = ToolExecutor()

class ChatInstance:
    def __init__(self):
        self.history = []

        self.system_messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": client.build_tool_prompt(TOOLS)},
        ]

        self.debug = False

    def send(self, user_input: str):
        user_input = user_input.strip()

        if (user_input[0] == "/"):
            return self.process_command(user_input[1:])

        return self.send_message(user_input)

    def send_message(self, user_input: str):
        self.history.append({
            "role": "user",
            "content": user_input
        })

        current_time_message = {
            "role": "system",
            "content": f"Current datetime: {datetime.now().astimezone().isoformat()}"
        }

        messages = self.system_messages + [current_time_message] + self.history

        response = client.make_request(messages, self.debug)
        response_message = client.get_response_message(response)

        while "<function=" in response_message:
            tool_result = toolExecutor.execute(response_message)

            self.history.append({
                "role": "assistant",
                "content": response_message
            })

            self.history.append({
                "role": "user",
                "content": f"Tool result: {tool_result}"
            })

            messages = self.system_messages + [current_time_message] + self.history

            response = client.make_request(messages, self.debug)
            response_message = client.get_response_message(response)

        self.history.append({
            "role": "assistant",
            "content": response_message
        })


        if len(self.history) > MAX_HISTORY:
            self.history = self.history[-MAX_HISTORY:]

        return response_message

    def process_command(self, command: str):
        print("[CHAT_INSTANCE_PROCESS_COMMAND] Processing command...")
        if(command == "history"):
            self.print_history()
        elif(command == "debug"):
            self.switch_debug()
        else:
            print(f"[CHAT_INSTANCE_PROCESS_COMMAND] Invalid command ({command}).")


    def print_history(self):
        print(f"[CHAT_INSTANCE_PRINT_HISTORY] Printing chat history...")
        for message in self.history:
            print(message)

    def switch_debug(self):
        if self.debug:
            print(f"[CHAT_INSTANCE_SWITCH_DEBUG] Debug is now turned OFF.")
            self.debug = False
        else:
            print(f"[CHAT_INSTANCE_SWITCH_DEBUG] Debug is now turned ON.")
            self.debug = True