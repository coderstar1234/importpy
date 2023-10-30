import requests
import time

# Define the URL of the MIS website
url = "https://www.example.com"  # Replace with the actual URL

# Measure the time it takes to load the page
start_time = time.time()
response = requests.get(url)
end_time = time.time()
load_time = end_time - start_time

# Print the load time
print(f"Page Load Time for {url}: {load_time:.2f} seconds")
