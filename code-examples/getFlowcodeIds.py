import requests
import csv

#Function to make GET requests List Codes API endpoint to get Flowcode code_id's
def get_codes(apikey, folder_id, limit):
    url = "https://gateway.flowcode.com/v4/codes"
    headers = {"apikey": apikey}
    params = {"folder_id": folder_id, "limit": limit}
    code_ids = []

    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            for result in results:
                code_ids.append(result.get("code_id"))
            url = data.get("next") # Make a request to get code_id's from next page
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            break

    return code_ids

#Save Flowcode code_id's to CSV file
def save_to_csv(code_ids, filename):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["code_id"])
            for code_id in code_ids:
                writer.writerow([code_id])
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")

def main():
    apikey = ""     # Your Flowcode API Key
    folder_id = ""  # Folder to pull code_id's from
    limit = 450     # Limit codes returned in each successful request, recommended under 500
    filename = ""   # Output CSV filename

    #Get Flowcode code_id's via API requests to List Codes endpoint 
    code_ids = get_codes(apikey, folder_id, limit)

    if code_ids:
        save_to_csv(code_ids, filename) #Save code_id's to file
        print(f"Code IDs saved to {filename}")
    else:
        print("No code IDs found.")

if __name__ == "__main__":
    main()
