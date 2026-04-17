import datetime

def calendar_get_next_n_events(service, n: int):
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