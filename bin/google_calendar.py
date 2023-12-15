import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the scope for Google Calendar API
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def google_authenticate():
    """Authenticate with Google API."""
    creds = None

    # Load credentials if they exist
    if os.path.exists("data/configs/token.json"):
        creds = Credentials.from_authorized_user_file("data/configs/token.json")
    
    # Refresh credentials if they are expired or not valid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # If no valid credentials, use installed app flow for authentication
            flow = InstalledAppFlow.from_client_secrets_file("data/configs/credentials.json", scopes=SCOPES)
            creds = flow.run_local_server()
            
        # Save the credentials for the next run
        with open("data/configs/token.json", "w") as token:
            token.write(creds.to_json())
    
    try:
        # Build the service for the Google Calendar API
        service = build("calendar", "v3", credentials=creds)
        return service
    
    except HttpError as err:
        print(err)

def google_get_next_events(max_results, google_service):
    """Retrieve the next events from Google Calendar.
    
    Args:
    max_results (int): Maximum number of events to retrieve.
    google_service (googleapiclient.discovery.Resource): Google Calendar API service object."""

    # Get current time in ISO format
    now = dt.datetime.now().isoformat() + "Z"

    # Request a list of upcoming events
    event_results = google_service.events().list(calendarId="primary", timeMin=now, maxResults=max_results, singleEvents=True, orderBy="startTime").execute()
    events = event_results.get("items", [])

    new_events_list = []

    # Process and format each event
    if not events:
        print("No upcoming events found.")
    for event in events:
        # Extract and format start and end times
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        try:
            new_start = dt.datetime.strptime(start[:19], "%Y-%m-%dT%H:%M:%S")
            new_start = new_start.strftime("%B %d at %I:%M %p")
            new_end = dt.datetime.strptime(end[:19], "%Y-%m-%dT%H:%M:%S")
            new_end = new_end.strftime("%I:%M %p")
            output = event["summary"] + " starts on " + str(new_start) + " and ends at " + str(new_end)
            new_events_list.append(output)
        except ValueError:
            # Fallback for all-day events or different date formats
            new_start = dt.datetime.strptime(start[:10], "%Y-%m-%d")
            new_start = new_start.strftime("%B %d")
            new_end = dt.datetime.strptime(end[:10], "%Y-%m-%d")
            new_end = new_end.strftime("%B %d")
            output = event["summary"] + " starts on " + str(new_start) + " and ends on " + str(new_end)
            new_events_list.append(output)

    return new_events_list

def modify_event(event_id, google_service, summary=None, start=None, end=None):
    """Modify an existing event in Google Calendar.
    
    Args:
    event_id (str): ID of the event to be modified.
    google_service (googleapiclient.discovery.Resource): Google Calendar API service object.
    summary (str): New summary for the event.
    start (dict): New start time for the event.
    end (dict): New end time for the event."""

    # Retrieve the event to be modified
    event = google_service.events().get(calendarId="primary", eventId=event_id).execute()

    # Update the event details if provided
    if summary != None:
        event["summary"] = summary
    if start != None:
        event["start"] = start
    if end != None:
        event["end"] = end

    # Save the updated event
    updated_event = google_service.events().update(calendarId="primary", eventId=event_id, body=event).execute()

    return updated_event

def create_event(google_service, summary, start, end):
    """Create a new event in Google Calendar.
    
    Args:
    google_service (googleapiclient.discovery.Resource): Google Calendar API service object.
    summary (str): Summary for the event.
    start (dict): Start time for the event.
    end (dict): End time for the event."""

    # Define the new event
    event = {
        "summary": summary,
        "start": start,
        "end": end
    }

    # Add the event to the calendar
    event = google_service.events().insert(calendarId="primary", body=event).execute()

    return event

def delete_event(event_id, google_service):
    """Delete an event from Google Calendar.
    
    Args:
    event_id (str): ID of the event to be deleted.
    google_service (googleapiclient.discovery.Resource): Google Calendar API service object."""

    # Remove the specified event
    google_service.events().delete(calendarId="primary", eventId=event_id).execute()

    return "Event deleted"

def main():
    """Main function to demonstrate the usage of Google Calendar functions."""
    # Authenticate with Google and get a list of next events
    event_list = google_get_next_events(20, google_authenticate())

    # Print each event
    for event in event_list:
        print(event)

if __name__ == "__main__":
    main()
