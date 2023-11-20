import requests
import csv

## Example Python script demonstrating the functionality of generating Flowcode images via the Flowcode API.
## The script makes a GET request to get all Flowcodes in a given folder and then makes GET requests to generate Flowcode images for those Flowcodes.
## Before running this script, simply replace the 'apikey' and 'folder_id' with your own values. 
## For more information and full documentation of all the Flowcode API endpoints, please visit our Developer Portal: https://developer.flowcode.com/

# Function that makes a request to the Flowcode API to get all Flowcodes in a folder.
def get_flowcodes(apikey,folder_id):
    # Flowcode codes API endpoint
    url = f"https://gateway.flowcode.com/v4/codes"
    # folder_id to get codes in
    params = {"folder_id": folder_id}

    headers = {
        "Content-Type": "application/json",
        "apikey": apikey
    }

    # Make a GET request to list codes in folder
    response = requests.get(url, params=params, headers=headers)

    # Return data if successful
    if response.status_code < 400:
        data = response.json()
        return data['results']
    else:  # Throw error if not successful
        raise requests.exceptions.HTTPError(
            f"Error: {response.status_code} - {response.text}")


def get_flowcode_img_url(apikey, code_id):
    # Flowcode generator API endpoint
    url = f"https://gateway.flowcode.com/v3/codes/generator/{code_id}"
    
    headers = {
        "Content-Type": "application/json",
        "apikey": apikey
    }

    # Make a GET request to get the Flowcode image of the URL.
    # For a list of options you can pass, such as for customizing the Flowcode image, please see here:
    # https://developer.flowcode.com/documentation/flowcode-api#/operations/generateDynamicImage
    response = requests.get(url, headers=headers)

    # Return data if successful
    if response.status_code < 400:
        data = response.json()
        if "url" in data:
            return data["url"]
    else:  # Throw error if not successful
        raise requests.exceptions.HTTPError(
            f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":

    # Please replace with your folder_id and apikey here
    folder_id = "your_folder_id"  
    apikey = "your_api_key"

    #Check if missing or incorrect folder_id and apikey
    if not folder_id or folder_id == "your_folder_id":
        raise ValueError(
            "Folder ID (folder_id) missing or incorrect. Please enter your valid folder_id.")
    if not apikey or apikey == 'your_api_key':
        raise ValueError("API key (apikey) missing or incorrect. Please enter your valid API key.")

    try:
        codes = get_flowcodes(apikey, folder_id)

        if not codes:
            print("No Flowcodes found in folder.")

        filename = "flowcode_img_urls"  # You can replace "flowcode_img_urls" with any desired filename

        with open(f"{filename}.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["code_id", "url"])

            # Loop through Flowcodes
            for code in codes:
                code_id = code.get("code_id")
                if code_id:
                    try:
                        # Get the URL image for the Flowcode
                        url = get_flowcode_img_url(apikey, code_id)
                        if url is not None:
                            # Write URL to a CSV
                            csv_writer.writerow([code_id, url])
                        else:
                            print(f"Failed to get URL for code_id: {code_id}")
                    except Exception as e:
                        print(f"An error occurred for code_id {code_id}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")