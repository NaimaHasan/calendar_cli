import typer


def add_recurrence_rule():
    """
    Prompts the user to create a recurrence rule for an event.

    Returns:
    --------
    recurrence_rule : List[str]
        A list containing a single recurrence rule string.
    """
    frequency = get_frequency()
    interval = typer.prompt("\nInterval", type=int)
    count = typer.prompt("\nNumber of occurrences", type=int)
    recurrence_rule = [f"RRULE:FREQ={frequency};INTERVAL={interval};COUNT={count}"]

    return recurrence_rule


def get_frequency() -> str:
    """
   Prompts the user to select a frequency for the recurrence rule.

   Returns:
   --------
   frequency : str
       The selected frequency as a string (e.g., "DAILY", "WEEKLY", "MONTHLY", "YEARLY").
   """
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
