# Restro-Radar

Restro-Radar is a modern web application that helps users find nearby restaurants based on their location. Using the power of geolocation and an interactive map, it displays restaurants along with their hygiene ratings, reviews, and more.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

---

## Features
- **Geolocation-Based Search**: Automatically detects the user's location to suggest nearby restaurants.
- **Interactive Map**: Displays restaurant locations on an OpenStreetMap-based map.
- **Restaurant Information**: Provides details such as hygiene ratings, user reviews, and more.
- **Mobile-Responsive Design**: Optimized for use on both desktop and mobile devices.

---

## Technologies Used
- **Frontend**: 
  - HTML, CSS (with custom styles)
  - JavaScript (for geolocation and map interactivity)
  - Leaflet.js (for interactive map functionality)
  
- **Backend**: 
  - Python with Flask framework
  - Google Places API (for fetching restaurant data)
  
- **Other**: 
  - OpenStreetMap (for map rendering)

---

## Setup and Installation

### Prerequisites
1. Python 3.x
2. Flask: You can install Flask using pip:
    ```bash
    pip install flask
    ```

### Clone the Repository
```bash
git clone https://github.com/your-username/restro-radar.git
cd restro-radar
