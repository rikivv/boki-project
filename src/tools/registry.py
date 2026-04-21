import json

from config import COLORS

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

    {
        "type": "function",
        "function": {
            "name": "calendar_get_next_n_events",
            "description": "Get the next N upcoming events from the user's primary Google Calendar.",
            "parameters": {
                "type": "object",
                "properties": {
                    "n": {
                        "type": "integer",
                        "description": "The number of upcoming events to retrieve from the current time."
                    }
                },
                "required": ["n"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calendar_create_event",
            "description": "Create a new event in the user's primary Google Calendar.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The title or summary of the calendar event."
                    },
                    "startTime": {
                        "type": "string",
                        "description": "The start date and time of the event in ISO 8601 format."
                    },
                    "endTime": {
                        "type": "string",
                        "description": "The end date and time of the event in ISO 8601 format."
                    },
                    "category": {
                        "type": "string",
                        "enum": list(COLORS.keys()),
                        "description": "Category of the event, mapped internally to a calendar color."
                    },
                    "description": {
                        "type": "string",
                        "description": "An optional description for the event."
                    },
                    "location": {
                        "type": "string",
                        "description": "An optional location for the event."
                    },
                    "timezone": {
                        "type": "string",
                        "description": "The timezone for the event (e.g., 'Europe/Lisbon'). Defaults to 'Europe/Lisbon'."
                    }
                },"calendar_create_event"
                "required": ["name", "startTime", "endTime", "category"]
            }
        }
    }
]
