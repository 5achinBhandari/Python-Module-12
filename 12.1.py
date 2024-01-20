import requests
import json


def fetch_random_chuck_norris_joke():
    # API endpoint for fetching a random Chuck Norris joke
    url = "https://api.chucknorris.io/jokes/random"

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Extract and return the joke text from the response
            return data.get('value', 'Failed to fetch joke :(')
        else:
            return "Failed to fetch joke. Please try again later."

    except Exception as e:
        return f"An error occurred: {e}"


def main():
    # Fetch a random Chuck Norris joke
    joke = fetch_random_chuck_norris_joke()

    # Print the joke text
    print(joke)


if __name__ == "__main__":
    main()
