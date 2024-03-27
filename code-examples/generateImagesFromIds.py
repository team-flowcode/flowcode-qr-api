import csv
import requests

# Function to make GET request to generate a Flowcode image
def get_flowcode_image(code_id, apikey, image_type):

    # Flowcode image generator API endpoint
    url = f"https://gateway.flowcode.com/v3/codes/generator/{code_id}?image_type={image_type}"

    headers = {
        "apikey": apikey, # Your Flowcode API Key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        image_url = data.get("url")
        if image_url:
            # Handle image here.
            # Add optional code to save image locally, upload to Cloud storage, etc.
            return
        else:
            print(f"No image URL found for code_id: {code_id}")
    else:
        print(f"Failed to fetch data for code_id: {code_id}")
    return


def main():
    apikey = ''         # Your Flowcode API Key
    csv_file = ''       # Name of input CSV File with code_id's
    image_type = 'pdf'  # Set the desired image type. Options are svg, png, pdf, tiff, and jpg

    code_ids = []  # Initialize code_ids list

    # Read code_ids from CSV file
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            code_ids = [row[0] for row in csv_reader]
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print("An error occurred while reading the file:", str(e))

    # Loop through each code_id and make a GET request to generate a Flowcode image
    for code_id in code_ids:
        get_flowcode_image(code_id, apikey, image_type)


if __name__ == "__main__":
    main()
