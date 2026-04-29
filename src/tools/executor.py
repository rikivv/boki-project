import re
import json

from .basic import oi, get_current_temperature
from integrations.google_calendar.queries import calendar_get_next_n_events, calendar_create_event

class ToolExecutor:
    def __init__(self):
        self.tool_map = {
            "oi": oi,
            "get_current_temperature": get_current_temperature,
            "calendar_get_next_n_events": calendar_get_next_n_events,
            "calendar_create_event": calendar_create_event,
        }

    def parse_tool_call(self, response: str):
        if "<|tool_call|>" in response:

            start = response.find("{")
            if start == -1:
                return None, None

            # brace matching (SAFE JSON extraction)
            depth = 0
            end = None

            for i in range(start, len(response)):
                if response[i] == "{":
                    depth += 1
                elif response[i] == "}":
                    depth -= 1
                    if depth == 0:
                        end = i
                        break

            if end is None:
                return None, None

            json_str = response[start:end + 1].strip()

            try:
                data = json.loads(json_str)
                return data.get("name"), data.get("arguments", {})
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON in tool call: {json_str}") from e


        old_pattern = r"<function=(.*?)>(.*?)</function>"
        old_match = re.search(old_pattern, response, re.DOTALL)

        if old_match:
            function_name = old_match.group(1).strip()
            args_str = old_match.group(2).strip()

            try:
                args = json.loads(args_str)
                return function_name, args
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON in tool arguments")

        return None, None

    def get_function_from_name(self, name: str):
        return self.tool_map.get(name)

    def execute(self, toolCall: str):
        name, args = self.parse_tool_call(toolCall)

        func = self.get_function_from_name(name)

        if not func:
            raise ValueError(f"Tool '{name}' not found")

        print("[TOOL_EXECUTOR] Executing tool...")
        response = func(**args)
        print("[TOOL_EXECUTOR] Tool Executed.")
        
        return response