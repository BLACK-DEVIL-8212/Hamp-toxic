import requests

def track_last_location(phone_number):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    url = f'https://example.com/api/track?number={phone_number}&key={api_key}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            last_location = data['location']
            return last_location
        else:
            print('Error:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Error:', e)

# Example usage
phone_number = input("Enter a phone number: ")
last_location = track_last_location(phone_number)
print(f"The last known location of {phone_number} is: {last_location}")
