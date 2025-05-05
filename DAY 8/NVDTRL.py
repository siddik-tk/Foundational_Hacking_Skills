import requests

# Step 1: Define the base URL for the NVD API
base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Step 2: Define the keyword to search for
keyword = "openssl"  # You can replace this with any service name

# Step 3: Create the query URL with parameters
params = {
    "keywordSearch": keyword,
    "resultsPerPage": 5  # Limit results for testing
}

# Step 4: Send a GET request to the NVD API
response = requests.get(base_url, params=params)

# Step 5: Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    # Step 6: Loop through the vulnerabilities
    for cve in data.get("vulnerabilities", []):
        cve_id = cve["cve"]["id"]
        description = cve["cve"]["descriptions"][0]["value"]
        print(f"{cve_id}: {description}")
else:
    print("Error:", response.status_code)
