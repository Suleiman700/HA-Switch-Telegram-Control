import requests

# The URL of the Flask server
url = 'http://localhost:5000/convert'

# The weblink to the voice file (replace with an actual URL for testing)
weblink = 'https://download.samplelib.com/mp3/sample-3s.mp3' # audio file

# Construct the URL with the weblink as a query parameter
full_url = f'{url}?weblink={weblink}'

# Send the GET request to the Flask server
response = requests.get(full_url)

# Print the raw response text
print(response.text)

# Try to print the JSON response
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Response content is not in JSON format")