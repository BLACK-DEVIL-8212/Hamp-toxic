import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

def get_phone_number_info(phone_number):
    parsed_number = phonenumbers.parse(phone_number, None)
    region = geocoder.description_for_number(parsed_number, "en")
    carrier_name = carrier.name_for_number(parsed_number, "en")
    is_valid = phonenumbers.is_valid_number(parsed_number)
    is_possible = phonenumbers.is_possible_number(parsed_number)
    
    number_info = {
        "Phone Number": phone_number,
        "Valid": is_valid,
        "Possible": is_possible,
        "Region": region,
        "Carrier": carrier_name
    }
    
    return number_info

# Example usage
phone_number = "+911234567890"  # Replace with the phone number you want to get information about
phone_info = get_phone_number_info(phone_number)

for key, value in phone_info.items():
    print(f"{key}: {value}")

def get_coordinates(phone_number):
    parsed_number = phonenumbers.parse(phone_number, "US")  # Change "US" to the appropriate country code
    location = geocoder.description_for_number(parsed_number, "en")

    geolocator = Nominatim(user_agent="phone_locator")
    address = geolocator.geocode(location)
    if address is not None:
        coordinates = (address.latitude, address.longitude)
        return coordinates
    else:
        return None

# Example usage
phone_number = "+911234567890"  # Replace with the phone number you want to locate
coordinates = get_coordinates(phone_number)

if coordinates is not None:
    latitude, longitude = coordinates
    print(f"The coordinates of the phone number {phone_number} are: Latitude: {latitude}, Longitude: {longitude}")
else:
    print(f"No coordinates found for the phone number {phone_number}")