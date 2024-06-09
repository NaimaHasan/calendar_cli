# Google Calendar CLI with Typer

This project is a command-line interface (CLI) application built with Python's Typer library. It allows users to interact with Google Calendar to add, delete, update events, and invite users. Additionally, users can list upcoming events from their calendar.

## Features

- **Add Event**: Create a new event with optional invitee.
- **Delete Event**: Remove an event by its ID.
- **Update Event**: Modify an event's details.
- **List Events**: View a list of upcoming events.

## Installation

1. **Clone the repository**:
    ```bash
    git clone linkkk
    cd google-calendar-cli
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Google Calendar API**:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project.
    - Enable the Google Calendar API.
    - Create OAuth 2.0 credentials (OAuth client ID).
    - Download the `credentials.json` file and place it in the root directory of this project.

## Usage

### Add Event

```bash
python cli.py add-event
```

### Delete Event

```bash
python cli.py delete-event id
```

### Add Recurring Event

```bash
python cli.py add-recurring-event
```

### List Events

```bash
python cli.py list-upcoming-events 
```

## Authentication

The first time you run any command, you will be prompted to authenticate with your Google account. This will generate a `token.json` file that stores your access and refresh tokens. Make sure `credentials.json` is in the root directory of the project.


## Acknowledgments

- [Typer](https://typer.tiangolo.com/)
- [Google Calendar API](https://developers.google.com/calendar)
- [Google Auth Python Library](https://github.com/googleapis/google-auth-library-python)

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.




