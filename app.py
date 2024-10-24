from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = ''  # Use your actual Google Maps API key

HYGIENE_KEYWORDS = ['clean', 'safe', 'hygiene', 'healthy', 'fresh', 'good', 'great']
UNHYGIENIC_KEYWORDS = ['dirty', 'sick', 'unhygienic', 'bad', 'poor', 'ill']

def geocode_address(address):
    """Convert an address into latitude and longitude using Google Maps API."""
    url = f'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

def get_nearby_restaurants(latitude, longitude):
    """Fetch nearby restaurants using Google Places API."""
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': f'{latitude},{longitude}',
        'radius': 1000,  # Search within a 1 km radius
        'type': 'restaurant',
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        places_data = response.json()
        restaurant_details = []
        for place in places_data.get('results', []):
            place_id = place['place_id']
            name = place['name']
            geometry = place['geometry']
            
            # Fetch reviews for each restaurant
            details_url = f'https://maps.googleapis.com/maps/api/place/details/json'
            details_params = {
                'place_id': place_id,
                'fields': 'name,rating,reviews,geometry',
                'key': API_KEY
            }
            details_response = requests.get(details_url, params=details_params)
            if details_response.status_code == 200:
                details_data = details_response.json().get('result', {})
                reviews = details_data.get('reviews', [])[:10]  # Top 10 most recent reviews

                # Analyze reviews for hygiene and safety
                hygiene_score = analyze_reviews(reviews)
                
                restaurant_details.append({
                    'name': name,
                    'geometry': geometry,
                    'reviews': reviews,
                    'hygiene_score': hygiene_score  # Add hygiene score to details
                })
        return restaurant_details
    return []

def analyze_reviews(reviews):
    """Analyze reviews to determine hygiene and safety score."""
    score = 0
    total_reviews = len(reviews)

    for review in reviews:
        text = review.get('text', '').lower()
        for keyword in HYGIENE_KEYWORDS:
            if keyword in text:
                score += 1  # Increase score for hygiene-positive keywords
        for keyword in UNHYGIENIC_KEYWORDS:
            if keyword in text:
                score -= 1  # Decrease score for hygiene-negative keywords

    return score / total_reviews if total_reviews > 0 else 0  # Return average score

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET'])
def submit():
    address = request.args.get('address')
    latitude, longitude = geocode_address(address)
    
    if latitude is not None and longitude is not None:
        restaurants = get_nearby_restaurants(latitude, longitude)
        return render_template('results.html', latitude=latitude, longitude=longitude, restaurants=restaurants)
    else:
        return render_template('index.html', error="Location not found. Please try again.")


if __name__ == '__main__':
    app.run(debug=True)
