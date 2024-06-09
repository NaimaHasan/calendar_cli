import typer
from datetime import datetime
from typing_extensions import Annotated

from services import event_service
from services import recurring_event_service
from models.event import Event

app = typer.Typer(no_args_is_help=True)


@app.command()
def add_event(summary: Annotated[str, typer.Option(prompt=True)],
              start_time: Annotated[
                  datetime, typer.Option(prompt="\nTime formats: YYYY-MM-DD, YYYY-MM-DD HH:MM:SS\n"
                                                "Start time")],
              end_time: Annotated[datetime, typer.Option(prompt=True)]) -> None:
    """Add an event."""

    attendees = event_service.add_attendee()

    event = Event(summary=summary, start_time=start_time, end_time=end_time, attendees=attendees)
    event_service.create_event(event)


@app.command()
def add_recurring_event(summary: Annotated[str, typer.Option(prompt=True)],
                        start_time: Annotated[
                            datetime, typer.Option(prompt="\nTime formats: YYYY-MM-DD, YYYY-MM-DD HH:MM:SS\n"
                                                          "Start time")],
                        end_time: Annotated[datetime, typer.Option(prompt=True)]) -> None:
    """Add a recurring event."""

    attendees = event_service.add_attendee()
    recurrence = recurring_event_service.get_recurrence_rule()

    event = Event(summary=summary, start_time=start_time, end_time=end_time, attendees=attendees, recurrence=recurrence)
    event_service.create_event(event)


@app.command()
def delete_event(event_id: Annotated[str, typer.Option(prompt=True)]):
    """Delete event by its id."""
    event_service.delete_event(event_id)


@app.command()
def list_upcoming_events(max_results: Annotated[int, typer.Option(prompt=True)]):
    """List upcoming events in the primary calendar."""
    events = event_service.get_upcoming_events(max_results)
    event_service.print_events(events)


@app.command()
def get_event_by_id(event_id: Annotated[str, typer.Option(prompt=True)]):
    event_service.get_event_by_id(event_id)


if __name__ == "__main__":
    app()
