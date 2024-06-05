import os
import typer
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

app = typer.Typer(no_args_is_help=True)


@app.command()
def find_all_recipes():
    typer.echo("HIIIIIIIIIIIIIIIII")


if __name__ == "__main__":
    app()
