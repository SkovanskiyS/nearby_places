import requests


def get_nearby_places(api_key, latitude, longitude, place_type):
    # Define the base URL for the Search API
    base_url = "https://geocode-maps.yandex.ru/1.x"

    # Define the parameters for the API request
    params = {
        "apikey": api_key,
        "kind": place_type,
        "ll": f"{longitude},{latitude}",  # Note the reversed order (longitude, latitude)
        "spn": "0.1,0.1",  # The "span" defines the search area (adjust this as needed)
        "lang": "en_US"  # Language for the response (English)
    }

    # Send the API request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the request was successful
    if data.get("features"):
        return data["features"]
    else:
        print("No places found nearby.")
        return []


def main():
    # Replace 'YOUR_API_KEY' with your actual Yandex Maps API key
    api_key = "e1b99a94-99a0-4b5f-adf2-da8f04b0bb84"

    # User's coordinates (latitude and longitude)
    user_latitude = 55.753930
    user_longitude = 37.620795

    # Type of place the user is searching for
    place_type = "museum"

    # Get nearby places
    places = get_nearby_places(api_key, user_latitude, user_longitude, place_type)

    if places:
        for place in places:
            name = place["properties"]["name"]
            address = place["properties"]["description"]
            print(f"{name} - {address}")
    else:
        print("No places found nearby.")


if __name__ == "__main__":
    main()
