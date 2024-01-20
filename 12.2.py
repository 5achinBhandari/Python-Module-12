import requests


def kelvin_to_celsius(kelvin_temp):
    """Convert temperature from Kelvin to Celsius."""
    return kelvin_temp - 273.15


def fetch_weather_data(city_name, api_key):
    """Fetch weather data for a given city using the OpenWeather API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Create the parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
    }

    try:
        # Send a GET request to the API endpoint
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract weather description and temperature from the response
            weather_description = data['weather'][0]['description']
            temperature_kelvin = data['main']['temp']
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)

            return weather_description, temperature_celsius
        else:
            return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def main():
    # Replace 'YOUR_API_KEY_HERE' with your actual OpenWeather API key
    api_key = 'YOUR_API_KEY_HERE'

    # Ask the user to input the name of the municipality
    city_name = input("Enter the name of the municipality: ").strip()

    # Fetch weather data for the given municipality
    weather_description, temperature_celsius = fetch_weather_data(city_name, api_key)

    # Print the weather condition description and temperature in Celsius
    if weather_description and temperature_celsius is not None:
        print(f"Weather Condition in {city_name}: {weather_description}")
        print(f"Temperature in {city_name}: {temperature_celsius:.2f}Â°C")
    else:
        print("Failed to fetch weather data. Please try again later.")


if __name__ == "__main__":
    main()