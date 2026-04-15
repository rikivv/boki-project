import json

from .basic import oi

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "oi",
            "description": "prints greeting",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
]
