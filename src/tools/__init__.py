import json

from .basic import oi, get_current_temperature

def get_function_from_name(name):
    if name == "oi":
        return oi
    if name == "get_current_temperature":
        return get_current_temperature
    
    return 

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

    {
        "type": "function",
        "function": {
            "name": "get_current_temperature",
            "description": "Get current temperature at a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": 'The location to get the temperature for, in the format "City, Country".',
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": 'The unit to return the temperature in. Defaults to "celsius".',
                    },
                },
                "required": ["location"],
            },
        },
    },
]
