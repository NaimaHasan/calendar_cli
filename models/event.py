from typing import List, Dict
from datetime import datetime


class Event:
    """
    A class to represent a calendar event.

    Attributes:
    -----------
    summary : str
        A brief description or title of the event.
    start_time : datetime
        The start date and time of the event.
    end_time : datetime
        The end date and time of the event.
    attendees : List[str]
        A list of email addresses of the event attendees.
    event_id : str
        A unique identifier for the event (optional).
    recurrence : List[str]
        A list of recurrence rules for the event (optional).
    """

    def __init__(self, summary: str, start_time: datetime, end_time: datetime,
                 attendees: List[str] = None, event_id=None, recurrence: List[str] = None):
        """Initializes the Event class with the provided parameters."""
        self.event_id = event_id
        self.summary = summary
        self.start_time = start_time
        self.end_time = end_time
        self.attendees = attendees
        self.recurrence = recurrence

    def __str__(self):
        """Returns a string representation of the Event object."""
        attendees_str = ', '.join(self.attendees) if self.attendees else 'None'
        return (f"Summary: {self.summary}\n"
                f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"End Time: {self.end_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Attendees: {attendees_str}")

    def convert_to_dictionary(self) -> Dict:
        """Converts the Event object to a dictionary format suitable for API requests."""
        email_dict = []

        for email in self.attendees:
            email_dict.append({'email': email})

        return {
            'summary': self.summary,
            'start': {'dateTime': self.start_time.isoformat(), 'timeZone': 'UTC'},
            'end': {'dateTime': self.end_time.isoformat(), 'timeZone': 'UTC'},
            'attendees': email_dict,
            'recurrence': self.recurrence
        }

    @staticmethod
    def convert_to_event(event_dict: Dict) -> 'Event':
        """Converts a dictionary representation of an event to an Event object."""
        start_time = datetime.fromisoformat(event_dict['start']['dateTime'])
        end_time = datetime.fromisoformat(event_dict['end']['dateTime'])

        attendees = []
        attendees_list = event_dict.get('attendees', [])

        for attendee in attendees_list:
            email = attendee['email']
            attendees.append(email)

        return Event(
            summary=event_dict['summary'],
            start_time=start_time,
            end_time=end_time,
            attendees=attendees
        )
