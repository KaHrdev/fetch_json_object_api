import requests
from utils_functions import *

# API URL
url = "https://data.vatsim.net/v3/vatsim-data.json"

# Make GET request
response = requests.get(url)

# Check if response was successful
if response.status_code == 200:
    # Print content on JSON format
    data = response.json()
    print("data before:", data)
    data = get_objects_controllers_and_atis(data)
    data = get_objects_callsign_and_frequency(data)
    print(f"data after: {data}")
else:
    print("Error en la petición:", response.status_code)