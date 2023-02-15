from flask import Flask, request
from flask_cors import CORS
import json
from .adapters.openai import get_recommendations


app = Flask(__name__)
CORS(app)


@app.route('/api/v1/recommendation', methods=['POST'])
def write_review():
    """Creates a list of recommendations based on interest"""
    city = request.json['city']
    interests = request.json['interests']
    count = request.json.get('count', 10)

    return json.dumps({
        "data": {
            "recommendations": get_recommendations(city, interests, count)
        }
    }, indent=4)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
