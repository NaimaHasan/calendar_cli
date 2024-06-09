from typing import List, Dict
from datetime import datetime


class Event:
    def __init__(self, summary: str, start_time: datetime, end_time: datetime,
                 attendees: List[str] = None, event_id=None):
        self.event_id = event_id
        self.summary = summary
        self.start_time = start_time
        self.end_time = end_time
        self.attendees = attendees

    def __str__(self):
        attendees_str = ', '.join(self.attendees) if self.attendees else 'None'
        return (f"Summary: {self.summary}\n"
                f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"End Time: {self.end_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Attendees: {attendees_str}")

    def convert_to_dictionary(self) -> Dict:
        return {
            'summary': self.summary,
            'start': {'dateTime': self.start_time.isoformat(), 'timeZone': 'UTC'},
            'end': {'dateTime': self.end_time.isoformat(), 'timeZone': 'UTC'},
            'attendees': [{'email': email} for email in self.attendees]
        }
