import typer
from datetime import datetime


def get_recurrence_rule():
    frequency = get_frequency()
    interval = typer.prompt("\nInterval", type=int)
    count = typer.prompt("\nNumber of occurrences", type=int)
    recurrence = [f"RRULE:FREQ={frequency};INTERVAL={interval};COUNT={count}"]

    return recurrence


def get_frequency() -> str:
    frequency_map = {
        1: "DAILY",
        2: "WEEKLY",
        3: "MONTHLY",
        4: "YEARLY"
    }

    while True:
        frequency = typer.prompt("\nFrequency Options\n"
                                 "1. DAILY\n"
                                 "2. WEEKLY\n"
                                 "3. MONTHLY\n"
                                 "4. YEARLY\n"
                                 "Enter Frequency option",
                                 type=int)
        if frequency not in [1, 2, 3, 4]:
            typer.echo("Invalid frequency option. Please enter a number between 1 and 4.")
        else:
            break

    return frequency_map[int(frequency)]
