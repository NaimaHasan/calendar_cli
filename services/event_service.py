import typer
from datetime import datetime
from services import calendar_service
from models.event import Event
from googleapiclient.errors import HttpError


def add_attendee():
    """
    Prompts the user to add attendees to an event.

    The function repeatedly asks the user if they want to add more attendees until they choose to stop.
    It collects email addresses of the attendees and formats them appropriately.

    Returns:
    --------
    formatted_attendees : List[str]
        A list of formatted attendee email addresses.
    """
    attendees = []

    first_interation = True
    while True:
        if first_interation:
            more_attendee = typer.confirm("\nDo you want to add attendee?", default=True)
        else:
            more_attendee = typer.confirm("Do you want to more add attendee?", default=True)

        first_interation = False

        if more_attendee:
            email = typer.prompt("Enter attendee email").strip()
            attendees.append(email)
        else:
            break

    formatted_attendees = format_attendees(attendees)

    return formatted_attendees


def format_attendees(attendees):
    """
   Formats a list of attendees.
   If the attendees are in dictionary format, extracts email addresses. Otherwise, returns the list as is.
   """
    attendee_list = []
    if attendees:
        if isinstance(attendees[0], dict):
            for attendee in attendees:
                email = attendee['email']
                attendee_list.append(email)
        else:
            attendee_list = attendees

    return attendee_list


def create_event(event):
    """Creates an event in the Google Calendar."""
    service = calendar_service.get_calendar_service()

    event_dictionary = event.convert_to_dictionary()
    created_event = service.events().insert(calendarId='primary', body=event_dictionary).execute()
    typer.echo(f'Event created: {created_event.get("htmlLink")}')


def delete_event(event_id):
    """Deletes an event from the Google Calendar."""
    service = calendar_service.get_calendar_service()

    service.events().delete(calendarId='primary', eventId=event_id).execute()
    typer.echo('Event deleted')


def get_upcoming_events(max_results):
    """
    Retrieves a list of upcoming events from the Google Calendar.

    Parameters:
    -----------
    max_results : int
        The maximum number of upcoming events to retrieve.

    Returns:
    --------
    events : List[Dict]
        A list of dictionaries representing the upcoming events.
    """
    service = calendar_service.get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=max_results, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events


def print_events(events):
    """Prints the details of a list of events."""
    if not events:
        typer.echo('No upcoming events found.')

    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_id = event.get('id', 'No ID')
            summary = event.get('summary', 'No Title')

            typer.echo(f"{start} - {summary} (ID: {event_id})")


def get_event_by_id(event_id: str):
    """Retrieves and prints the details of a specific event by its ID."""
    service = calendar_service.get_calendar_service()

    try:
        event = service.events().get(calendarId='primary', eventId=event_id).execute()
        typer.echo(Event.convert_to_event(event))
    except HttpError as error:
        if error.resp.status == 404:
            typer.echo(f"Event with ID {event_id} not found.")
        else:
            typer.echo(f"An error occurred: {error}")
