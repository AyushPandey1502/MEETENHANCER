import requests
import tkinter as tk
from tkinter import simpledialog

# Replace with your Fireflies API key
API_KEY = "c9747856-48f3-4fb0-b28b-d0e359627078"

# Create a Tkinter window to ask for Google Meet link
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask for the Google Meet link
meet_link = simpledialog.askstring("Input", "Enter the Google Meet link:")
if not meet_link:
    print("Google Meet link is required. Exiting.")
    exit()

# Use a REST API endpoint to create a meeting instead of GraphQL mutation
# Start the meeting recording
def start_meeting():
    response = requests.post(
        "https://api.fireflies.ai/graphql",
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
        json={
            "query": """
            mutation {
                createMeeting {
                    id
                }
            }
            """
        }
    )
    if response.status_code == 200:
        meeting_id = response.json().get("data", {}).get("createMeeting", {}).get("id")
        return meeting_id
    else:
        print("Error starting meeting:", response.text)
        return None


# Join the ongoing meeting
def join_meeting(meeting_id):
    response = requests.post(
        "https://api.fireflies.ai/graphql",
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
        json={
            "query": """
            mutation joinMeeting($meetingId: ID!) {
                joinMeeting(meetingId: $meetingId)
            }
            """,
            "variables": {
                "meetingId": meeting_id,
            },
        }
    )
    if response.status_code == 200:
        print("Successfully joined meeting")
    else:
        print("Error joining meeting:", response.text)

# Stop the meeting recording
def stop_meeting(meeting_id):
    response = requests.post(
        "https://api.fireflies.ai/graphql",
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
        json={
            "query": """
            mutation stopMeeting($meetingId: ID!) {
                stopMeeting(meetingId: $meetingId)
            }
            """,
            "variables": {
                "meetingId": meeting_id,
            },
        }
    )
    if response.status_code == 200:
        print("Meeting recording stopped")
    else:
        print("Error stopping meeting:", response.text)

# Get the minutes of the meeting
def get_minutes(meeting_id):
    response = requests.post(
        "https://api.fireflies.ai/graphql",
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
        json={
            "query": """
            query getMeetingMinutes($meetingId: ID!) {
                getMeetingMinutes(meetingId: $meetingId) {
                    minutes {
                        text
                    }
                }
            }
            """,
            "variables": {
                "meetingId": meeting_id,
            },
        }
    )
    if response.status_code == 200:
        minutes_data = response.json().get("data", {}).get("getMeetingMinutes", {}).get("minutes")
        if minutes_data:
            # Combine the text from all the minutes
            minutes = "\n".join([item.get("text", "") for item in minutes_data])
            return minutes
        else:
            print("No minutes data found.")
            return None
    else:
        print("Error getting meeting minutes:", response.text)
        return None

if __name__ == "__main__":
    meeting_id = start_meeting()

    if meeting_id:
        join_meeting(meeting_id)

        # Assume the meeting is ongoing based on user input
        print("Meeting is assumed to be ongoing.")

        # Simulate the passage of time (replace this with actual meeting duration)
        input("Press Enter after the meeting has progressed...")

        stop_meeting(meeting_id)
        minutes = get_minutes(meeting_id)

        # Save minutes to a text file
        with open("meeting_minutes.txt", "w") as file:
            file.write(minutes)

        print("Meeting minutes saved to 'meeting_minutes.txt'")
