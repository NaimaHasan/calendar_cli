import typer
from datetime import datetime

from services import calendar_service


def add_attendee():
    attendees = []

    first_interation = True
    while True:
        if first_interation:
            more_attendee = typer.confirm("\nDo you want to add attendee?", default=True)
        else:
            more_attendee = typer.confirm("Do you want to more add attendee?", default=True)

        if more_attendee:
            email = typer.prompt("Enter attendee email").strip()
            attendees.append(email)
        else:
            break

    attendees = format_attendees(attendees)

    return attendees


def format_attendees(attendees):
    attendee_list = []
    if attendees:
        if isinstance(attendees[0], dict):
            for attendee in attendees:
                email = attendee['email']
                attendee_list.append(email)

    return attendee_list


def create_event(event):
    service = calendar_service.get_calendar_service()

    event_dictionary = event.convert_to_dictionary()
    created_event = service.events().insert(calendarId='primary', body=event_dictionary).execute()
    typer.echo(f'Event created: {created_event.get("htmlLink")}')


def delete_event(event_id):
    service = calendar_service.get_calendar_service()

    service.events().delete(calendarId='primary', eventId=event_id).execute()
    typer.echo('Event deleted')


def get_upcoming_events(max_results):
    service = calendar_service.get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=max_results, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events


def print_events(events):
    if not events:
        typer.echo('No upcoming events found.')

    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_id = event.get('id', 'No ID')
            summary = event.get('summary', 'No Title')

            typer.echo(f"{start} - {summary} (ID: {event_id})")
