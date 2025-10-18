import gspread
from google.oauth2.service_account import Credentials
import requests
import time
from datetime import datetime

# Function to authenticate Google Sheets
def authenticate_google_sheets():
    """Authenticate and return the Google Sheets client."""
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
        client = gspread.authorize(creds)
        print("Successfully authenticated with Google Sheets.")
        return client
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None


# WhatsApp API setup
api_url = "https://graph.facebook.com/v20.0/XXXXXXXXXXXXXXX/messages"  # Replace with your phone number ID
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your valid access token
template_name = "cold_client"  # Updated template name
image_url = "https://drive.google.com/uc?export=download&id=XXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your image URL

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, company_name):
    """Send a WhatsApp message using the Meta Graph API."""
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {"link": image_url}
                        }
                    ]
                },
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": company_name  # Use the company name as a placeholder
                        }
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if response.status_code == 200:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
            print(f"Message sent to {phone_number} successfully")
            print(f"Timestamp: {timestamp}")
            return "Sent", timestamp
        else:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
            print(f"Failed to send message to {phone_number}")
            return "Failed", timestamp
    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return "Failed", timestamp


# Main function to read from Google Sheets and send messages
def main():
    """Main function to read phone numbers and company names from Google Sheets and send messages."""
    client = authenticate_google_sheets()
    if not client:
        return

    try:
        # Open the spreadsheet and the worksheet
        SPREADSHEET_NAME = "Bulk Message NBD (Python)"  # Replace with your spreadsheet name
        WORKSHEET_NAME = "contact_list"  # Replace with your worksheet name
        sheet = client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)

        # Read all data from the sheet
        data = sheet.get_all_values()  # Fetch all rows

        # Process only rows where column M is empty
        phone_numbers = []
        company_names = []
        row_indices = []  # Keep track of row indices for updates
        for i, row in enumerate(data[1:], start=2):  # Skip the header row, index starts at 2
            if not row[11].strip():  # Column M is empty
                phone_numbers.append(row[0])  # Column A: Phone number
                company_names.append(row[1])  # Column B: Company name
                row_indices.append(i)

                # Stop processing after 100 rows
                if len(phone_numbers) >= 1500:
                    break

        print(f"Found {len(phone_numbers)} rows to process.")

        # Lists to store bulk updates
        timestamp_updates = []  # Timestamps for column M
        status_updates = []  # Status ("Sent" or "Failed") for column N

        # Send messages to selected rows
        for phone_number, company_name in zip(phone_numbers, company_names):
            if phone_number.strip() and company_name.strip():
                status, timestamp = send_whatsapp_message(phone_number, company_name)
                timestamp_updates.append([timestamp])  # Wrap in a list for bulk update
                status_updates.append([status])  # Wrap in a list for bulk update
                time.sleep(1)  # Delay to avoid hitting rate limits

        # Update the sheet in bulk
        if row_indices:  # Ensure there are updates to process
            status_range = f"M{row_indices[0]}:M{row_indices[-1]}"  # Bulk update range for column N
            timestamp_range = f"L{row_indices[0]}:L{row_indices[-1]}"  # Bulk update range for column M
            sheet.update(timestamp_range, timestamp_updates)  # Bulk update timestamp
            sheet.update(status_range, status_updates)  # Bulk update status

        print("Updates completed successfully.")

    except Exception as e:
        print(f"Error processing spreadsheet: {e}")


if __name__ == "__main__":
    main()



