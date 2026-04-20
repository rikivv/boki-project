import datetime

from integrations.google_calendar.client import GoogleCalendarClient
from config import COLORS

client = GoogleCalendarClient()
service = client.get_service()

def calendar_get_next_n_events(n: int):
    events = []
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

    event_results = service.events().list(
            calendarId="primary",
            timeMin=now,
            maxResults=n,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

    events = event_results.get("items", []
    )

    return events

def calendar_create_event(
    name: str,
    startTime: str,
    endTime: str,
    color: str = "misc",
    description: str = "",
    location: str = "",
    timezone: str = "Europe/Lisbon",
    ):

    colorIndex = COLORS.get(color, 0)

    event = {
        "summary": name,
        "location": location,
        "description": description,
        "start": {
            "dateTime": startTime,
            "timeZone": timezone,
        },
        "end": {
            "dateTime": endTime,
            "timeZone": timezone,
        },
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "popup", "minutes": 10},
            ],
        },
    }

    if 0 <= colorIndex <= 11:
        event["colorId"] = str(colorIndex)

    created_event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return {
        "id": created_event.get("id"),
        "link": created_event.get("htmlLink"),
        "summary": created_event.get("summary"),
    }
