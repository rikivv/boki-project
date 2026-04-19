import datetime

from integrations.google_calendar.client import GoogleCalendarClient

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

    events = event_results.get("items", [])

    return events