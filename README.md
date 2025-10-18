# 📨 WhatsApp Bulk Messaging Automation (Google Sheets + Meta API)

This Python project automates **sending personalized WhatsApp messages** to clients using the **Meta (Facebook) Graph API** and **Google Sheets** as the data source.

It reads phone numbers and company names from a Google Sheet, sends each recipient a templated WhatsApp message (with an image), and then updates the spreadsheet with the **status** (`Sent` or `Failed`) and **timestamp** for tracking.

---

## 🚀 Features

- ✅ Google Sheets integration via `gspread`
- ✅ WhatsApp Business API integration via `requests`
- ✅ Sends **templated image messages** automatically
- ✅ Updates message **status** and **timestamp** back to the sheet
- ✅ Handles **up to 1500 messages** per run (configurable)
- ✅ Includes delay between requests to prevent rate-limit issues

---

## 📂 Project Structure

whatsapp-meta-api-automation-main/
<br>
│
<br>
├── main.py # Main automation script
<br>
├── requirements.txt # Python dependencies
<br>
├── README.md # Project documentation
<br>
└── credentials.json # Google API credentials (FIND YOUR GOOGLE API CREDENTIALS)

---



## 🛠️ Requirements

- Python **3.8+**
- A **Google Cloud Service Account** with access to your Google Sheet
- A valid **Meta WhatsApp Business API** setup
- A **pre-approved WhatsApp message template** on Meta

---




## 📦 Installation
<br>
1️⃣ Clone this repository

```bash
git clone https://github.com/monojitbgit/whatsapp-meta-api-automation.git
```

```bash
cd whatsapp-meta-api-automation-main
```

<br>
2️⃣ Install dependencies

Make sure you have Python 3.8+ and pip installed, then run:
<br>pip install -r requirements.txt

<br>
3️⃣ Create credentials.json

<br>- Go to your [Google Cloud Console](https://console.cloud.google.com/).
<br>- Create or use an existing **Service Account**.
<br>- Generate a **JSON key file** and download it.
<br>- Rename the file to `credentials.json`.
<br>- Place it in the root of your project folder.
<br>- After you create your service account and `credentials.json`, you must **share your Google Sheet** with your service account’s email address.
  <br> It usually looks like this:
  <br> your-service-account-name@your-project-id.iam.gserviceaccount.com

<br>Now your script will be authorized to read and update the sheet using that service account.


<br>
4️⃣ Update configuration in the script

Open main.py and replace the following placeholders with your actual credentials and IDs:
<br>api_url = "https://graph.facebook.com/v20.0/YOUR_PHONE_NUMBER_ID/messages"
<br>access_token = "YOUR_ACCESS_TOKEN"
<br>template_name = "your_template_name"
<br>image_url = "https://drive.google.com/uc?export=download&id=YOUR_IMAGE_ID"
<br>SPREADSHEET_NAME = "YOUR SPREADSHEET NAME" 
<br>WORKSHEET_NAME = "YOUR SHEET NAME"

---

## 🚀 Running the Script

Once everything is configured, run:
<br>python main.py

You’ll see console output showing:
<br>API responses
<br>Message delivery status
<br>Timestamp updates
<br>Your Google Sheet will be updated automatically in:

<br>Column	Purpose
<br>A	Phone Number
<br>B	Company Name
<br>L	Timestamp (auto)
<br>M	Status (Sent/Failed)


<br>
⚙️ Behavior Details

Processes only rows where Column M (Status) is empty.
<br>Writes timestamp in Column L and status in Column M.
<br>Includes a time.sleep(1) delay between messages to respect API limits.
<br>Stops automatically after 1500 messages (configurable in the code).


<br>
🧩 Dependencies

The project depends on the following Python packages:
<br>gspread
<br>google-auth
<br>requests


These are listed in requirements.txt.
<br>Install them all at once using:
<br>pip install -r requirements.txt

---

## 🧾 License

This project is licensed under the MIT License.
<br>You’re free to use, modify, and distribute it for personal or commercial purposes.

---
