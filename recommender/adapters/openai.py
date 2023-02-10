import openai
import json
from ..settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def parse_response(response):
    """
    Parses OpenAI completion API response text
    """
    return response['choices'][0].get('text').replace('\n', '') if 'choices' in response else ''


def create_review(restaurant_name, points):
    """
    Creates a review for the restaurant
    """
    formatted_name = f"Name: {restaurant_name}"
    prompt = f"Write a restaurant review based \
         on these notes:\n\n{formatted_name}\n{points}\n\n:Review:"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return parse_response(response)


def get_recommendations(city, interests, count=10):
    """
    Creates a list of recommendations based on the interests and the city
    """

    interest_serialised = '\n'.join([
        f"- {interest}" for interest in interests])

    prompt = f"""Recommend top {count} places to visit in {city} based on below interests in JSON format with name, description and the interest fields:
{interest_serialised}
        """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    parsed_response = parse_response(response)
    print(parsed_response)
    return json.loads(parsed_response)
