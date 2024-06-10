import os

import typer
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError, TransportError

SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_calendar_service():
    """
    Obtains the Google Calendar API service using OAuth2 credentials.

    This function handles the authentication flow for accessing the Google Calendar API.
    It checks for existing credentials in a 'token.json' file, refreshes them if expired,
    or initiates a new authentication flow if necessary.

    Returns:
    --------
    service : googleapiclient.discovery.Resource
        A Resource object with methods for interacting with the Google Calendar API.
    """
    try:
        credentials = None

        if os.path.exists('token.json'):
            # Load the credentials from the token.json file
            credentials = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                # Prompt the user to log in if no valid credentials are found
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                credentials = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(credentials.to_json())

        service = build('calendar', 'v3', credentials=credentials)

        return service

    except FileNotFoundError:
        typer.echo("Error: 'credentials.json' or 'token.json' file not found.")
    except RefreshError:
        typer.echo("Error: Failed to refresh OAuth2 credentials. Please try again later.")
    except TransportError:
        typer.echo("Error: Unable to establish a connection to Google's servers. Please check your internet connection.")
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}")

    return None
