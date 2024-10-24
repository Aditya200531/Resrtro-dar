![logo](https://github.com/user-attachments/assets/ade83e46-8ff9-4650-b33a-c5c60cab8a3b)

# Restro-Radar

Restro-Radar is a modern web application that helps users find nearby restaurants based on their location. Using the power of geolocation and an interactive map, it displays restaurants along with their hygiene ratings, reviews, and more.

---

## Screenshots
![image](https://github.com/user-attachments/assets/fda2bf03-4e71-42f4-86df-0915f519252e)
![image](https://github.com/user-attachments/assets/000adba8-9de7-4754-9d23-9c8e5146e800)
![image](https://github.com/user-attachments/assets/3df0832b-e8e8-43b2-b846-a38fde7fd312)

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
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
git clone https://github.com/Aditya200531/Restro-Radar/tree/main
```

---

## Future Enhancements
- Email Alerts: Implement an email notification system using SendGrid or a similar service. This will alert public health officials or restaurant managers when multiple negative sentiment reviews are detected within a short time period.
- Advanced Sentiment Analysis: Further refine the sentiment analysis by fine-tuning the spaCy model or switching to more advanced models like BERT to increase the accuracy of detecting foodborne illness-related reviews.
- Scalability: Expand the system’s capacity to monitor multiple regions or handle a larger volume of reviews using cloud-based infrastructure like AWS or Google Cloud.
- Mobile Version: Develop a mobile-friendly version of the platform to allow health officials to monitor outbreaks and receive alerts on the go.

---

