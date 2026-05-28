import datetime
import hmac
import hashlib
import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()

# Payload data
data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "name": "Sakuntala Napit",
    "email": "napitsakun@gmail.com",
    "resume_link": "https://sakuntalanapit.com.np/assets/Sakuntala-Napit-Resume.pdf",
    "repository_link": "https://github.com/napitsakun/pyci-runner",
    "action_run_link": "https://github.com/napitsakun/pyci-runner/actions/runs/26552221861"
}

# Encode the payload data to bytes
payload_data = json.dumps(
    data,
    separators=(",", ":"),
    sort_keys=True
).encode('utf-8')

# Get the secret key from environment variable
secret_key = os.getenv("SECRET_KEY")

# Create the HMAC signature using the secret key and payload data
signature = hmac.new(
    str(secret_key).encode(),
    payload_data,
    hashlib.sha256
).hexdigest()

# Set the signature in the header
headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}"
}

# Send the POST request to the specified URL with the payload data and headers
remote_url = os.getenv("REMOTE_ADDRESS")
response = requests.post(
    remote_url,
    data=payload_data,
    headers=headers
)

print("Response: ", response.json())
