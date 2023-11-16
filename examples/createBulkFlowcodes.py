import requests
import os

## Example Python script demonstrating the functionality of bulk creating Flowcode (dynamic QR codes) via the Flowcode API.
## The script makes a POST request to the /v4/codes/bulk endpoint in the create_flowcodes function below.
## Before running this script, simply replace the 'apikey' value with your own API key. 
## For more information and full documentation of all the Flowcode API endpoints, please visit our Developer Portal: https://developer.flowcode.com/

# Function to create many Flowcodes using the Bulk Code Creation API endpoint
def create_flowcodes(apikey, codes, folder_name):

    # Endpoint URL
    url = "https://gateway.flowcode.com/v4/codes/bulk"

    requestBody = {
        "codes": codes,
        "folder_name": folder_name
    }

    headers = {
        "Content-Type": "application/json",
        "apikey": apikey
    }

    # Initiate a POST API request to /v4/codes/bulk"
    response = requests.post(url, json=requestBody, headers=headers)

    # Check if response was successful
    if response.status_code < 400:
        return response.json()
    else:  # Throw error if not successful
        raise requests.exceptions.HTTPError(
            f"Error: {response.status_code} - {response.text}")


# Example usage
if __name__ == "__main__":
    apikey = 'your_api_key'  # Please use your API key here
    if not apikey:
        raise ValueError("API key not found. Please enter your valid API key.")
    
    # New folder name where Flowcodes will be placed
    folder_name = "My Cool Flowcodes"
    
    flowcodesData = [
        # Add the Flowcodes you wish to create here, as JSON data
        {
            "destination": {
                "destination_type": "URL",
                "redirect_value": {"url": "https://www.flowcode.com/page/devapi"}
            },
            "code_name": "My Cool Flowcode 1"
        },
        {
            "destination": {
                "destination_type": "URL",
                "redirect_value": {"url": "https://www.flowcode.com/page/devapi-2"}
            },
            "code_name": "My Cool Flowcode 2"
        }
    ]

    # Run the function to create the Flowcodes
    try:
        result = create_flowcodes(apikey, flowcodesData, folder_name)
        print("Success!", result)
    except requests.exceptions.RequestException as e:  # Handle exceptions
        print(f"Request error: {e}")
