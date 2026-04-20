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

def calendar_create_event(name: str, startTime, endTime, colorIndex: int):

    event = {
        'summary': f'{name}',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2026-04-21T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2026-04-21T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
        'colorId': "3",
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return "oi"