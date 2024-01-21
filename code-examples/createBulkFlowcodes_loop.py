import requests
import json
import time

# This is script that will generate a defined number of Flowcodes from a starting to an end number, set with a fixed destination
# It uses a loop to create a codes array and makes a POST API request to the Flowcode JSON bulk endpoint: https://gateway.flowcode.com/v4/codes/bulk
# If the POST request returns a 202 response, it will return a bulk task_id which the script will check every few seconds for a few minutes

############### Please enter your details variables #########################
folder_name = "My Cool Flowcodes"
start_code_number = 1   # Update with the desired start code number
end_code_number = 1000  # Update with the desired end code number
api_key = "enterYourAPIKey"  # Replace with your actual API key
destinationUrl = "https://www.flowcode.com/page/devapi" # Flowcode destination
##############################################################################

# Create codes within the specified range
codes = []
for i in range(start_code_number, end_code_number + 1):
    code = {
        "destination": {
            "destination_type": "URL",
            "redirect_value": {
                "url": destinationUrl
            }
        },
        "code_name": f"My_Cool_Flowcode_{i}"
    }
    codes.append(code)

# Create reqBody JSON object
req_body = {
    "codes": codes,
    "folder_name": folder_name
}

# Make Flowcode bulk POST request
url = "https://gateway.flowcode.com/v4/codes/bulk"
headers = {"Content-Type": "application/json", "apiKey": api_key}

try:
    response = requests.post(url, data=json.dumps(req_body), headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses
    if response.status_code == 201:
        print("Bulk request successful, codes created.")
    elif response.status_code == 202:
        task_id = response.json().get("task_id")
        print(f"API bulk Flowcode request successful. Your request is being worked on, here is your Task ID: {task_id}")

        # Check Flowcode bulk task status every couple of seconds
        max_wait_time_seconds = 300  # 5 minutes
        start_time = time.time()

        while time.time() - start_time < max_wait_time_seconds:
            status_url = f"https://gateway.flowcode.com/v4/codes/bulk/{task_id}/status"
            status_response = requests.get(status_url, headers=headers)
            status_response.raise_for_status()  # Raise HTTPError for bad responses

            if status_response.status_code == 200:
                task_status = status_response.json().get("status")
                print(f"Task status: {task_status}")

                if task_status in ["SUCCESS", "FAILURE"]:
                    break  # Exit loop if task status is either SUCCESS or FAILURE

            time.sleep(5)  # Wait for a few seconds before checking again

        if task_status not in ["SUCCESS", "FAILURE"]:
            print("Exiting, please check the task status again in a few minutes.")
        else:
            print("Bulk Flowcode creation completed.")
    else:
        print(f"Failed to make Flowcode bulk POST request. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
