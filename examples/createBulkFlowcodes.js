// Example JavaScript script demonstrating the functionality of bulk creating Flowcode (dynamic QR codes) via the Flowcode API.
// The script makes a POST request to the /v4/codes/bulk endpoint in the createFlowcodes function below.
// Before running this script, simply replace the 'apikey' value with your own API key. 
// For more information and full documentation of all the Flowcode API endpoints, please visit our Developer Portal: https://developer.flowcode.com/

// Function to create many Flowcodes using the Bulk Code Creation API endpoint
async function createFlowcodes(apikey, codes, folderName) {
    // Endpoint URL
    const url = "https://gateway.flowcode.com/v4/codes/bulk";

    const requestBody = {
        codes: codes,
        folder_name: folderName
    };

    const headers = {
        "Content-Type": "application/json",
        "apikey": apikey
    };

    // Initiate a POST API request to /v4/codes/bulk
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(requestBody)
    });

    // Throw an error if response was not successful 
    if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Error: ${response.status} - ${errorText}`);
    } 

    return await response.json();
}

// Example usage
async function main() {
    const apikey = 'your_api_key'; // Please use your API key here
    if (!apikey) {
        throw new Error("API key not found. Please enter your valid API key.");
    }

    // New folder name where Flowcodes will be placed
    const folderName = "My Cool Flowcodes";

    const flowcodesData = [
        // Add the Flowcodes you wish to create here, as JSON data
        {
            destination: {
                destination_type: "URL",
                redirect_value: { url: "https://www.flowcode.com/page/devapi" }
            },
            code_name: "My Cool Flowcode 1"
        },
        {
            destination: {
                destination_type: "URL",
                redirect_value: { url: "https://www.flowcode.com/page/devapi-2" }
            },
            code_name: "My Cool Flowcode 2"
        }
    ];

    // Run the function to create the Flowcodes
    try {
        const result = await createFlowcodes(apikey, flowcodesData, folderName);
        console.log("Success!", result);
    } catch (error) { // Handle exceptions
        console.error(`Request error: ${error.message}`);
    }
}

// Run the example
main();
