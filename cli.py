import typer
from datetime import datetime
from typing_extensions import Annotated
from typing import List, Optional

from services import calendar_service
from services import event_service
from models.event import Event

app = typer.Typer(no_args_is_help=True)


@app.command()
def add_event(summary: Annotated[str, typer.Option(prompt=True)],
              start_time: Annotated[datetime, typer.Option(prompt="\nTime formats: YYYY-MM-DD, YYYY-MM-DD HH:MM:SS\n"
                                                                  "Start time")],
              end_time: Annotated[datetime, typer.Option(prompt=True)]) -> None:
    attendees = event_service.add_attendee()

    event = Event(summary=summary, start_time=start_time, end_time=end_time, attendees=attendees)
    event_service.create_event(event)


@app.command()
def delete_event(event_id: Annotated[str, typer.Option(prompt=True)]):
    event_service.delete_event(event_id)


@app.command()
def list_upcoming_events(max_results: Annotated[int, typer.Option(prompt=True)]):
    """List upcoming events in the primary calendar."""
    events = event_service.get_upcoming_events(max_results)
    event_service.print_events(events)


if __name__ == "__main__":
    app()
