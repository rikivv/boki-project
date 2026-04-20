import re
import json

from .basic import oi, get_current_temperature
from integrations.google_calendar.queries import calendar_get_next_n_events

class ToolExecutor:
    def __init__(self):
        self.tool_map = {
            "oi": oi,
            "get_current_temperature": get_current_temperature,
            "calendar_get_next_n_events": calendar_get_next_n_events,
        }

    def parse_tool_call(self, response: str):
        pattern = r"<function=(.*?)>(.*?)</function>"
        match = re.search(pattern, response)

        if not match:
            return None, None

        function_name = match.group(1).strip()
        args_str = match.group(2).strip()

        try:
            args = json.loads(args_str)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in tool arguments")

        return function_name, args

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