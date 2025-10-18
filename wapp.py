import requests

# API endpoint and access token
api_url = "https://graph.facebook.com/v20.0/XXXXXXXXXXXXXXX/messages"  # Replace with your phone number ID
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your valid access token

# Recipient details and message payload
phone_number = "XXXXXXXXXX"  # Replace with the recipient's phone number
image_url = "https://drive.google.com/uc?export=download&id=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your image URL
payload = {
    "messaging_product": "whatsapp",
    "to": phone_number,
    "type": "template",
    "template": {
        "name": "cold_client",  # Replace with your approved template name
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
            }
        ]
    }
}

# Headers for the request
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

try:
    # Send the request
    response = requests.post(api_url, json=payload, headers=headers)

    # Log the response
    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Check for errors
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.json())
except Exception as e:
    print("An error occurred:", e)


