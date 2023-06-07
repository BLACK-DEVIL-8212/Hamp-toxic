import requests

def collect_registration_data(phone_number):
    # Replace 'API_ENDPOINT' with the actual endpoint URL or API endpoint you are using
    API_ENDPOINT = 'https://example.com/api/registration-data'
    
    # Replace 'API_KEY' with your actual API key, if required
    headers = {
        'Authorization': 'Bearer API_KEY',
        'Content-Type': 'application/json'
    }
    
    # Create a JSON payload with the phone number
    payload = {
        'phone_number': phone_number
    }
    
    try:
        # Send a POST request to the API endpoint
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        
        # Check the response status code
        if response.status_code == 200:
            # Registration data successfully retrieved
            registration_data = response.json()
            # Process the registration data as needed
            print(registration_data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
phone_number = "+911234567890"  # Replace with the phone number you want to collect registration data for
collect_registration_data(phone_number)
