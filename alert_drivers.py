import googlemaps
import time
from datetime import datetime

API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

# Dummy data 
drivers = [
    {"id": "driver1", "location": "Jl. Sudirman, Jakarta"},
    {"id": "driver2", "location": "Jl. Thamrin, Jakarta"},
    {"id": "driver3", "location": "Jl. Gatot Subroto, Jakarta"},
]

ambulances = [
    {"id": "ambulance1", "location": "Jl. Sudirman, Jakarta"},
    {"id": "ambulance2", "location": "Jl. Thamrin, Jakarta"},
]

# Obtain the coordinates of a location
def get_coordinates(location):
    geocode_result = gmaps.geocode(location)
    return geocode_result[0]['geometry']['location']

# Calculate distance between two locations
def calculate_distance(loc1, loc2):
    distance_result = gmaps.distance_matrix(loc1, loc2, mode="driving")
    distance = distance_result['rows'][0]['elements'][0]['distance']['value']  # distance in meters
    return distance

# Continuously checks and alerts drivers
def alert_drivers():
    while True:
        alerts = []
        for ambulance in ambulances:
            ambulance_coords = get_coordinates(ambulance['location'])
            for driver in drivers:
                driver_coords = get_coordinates(driver['location'])
                if driver['location'].split(',')[0] == ambulance['location'].split(',')[0]:
                    distance = calculate_distance(driver_coords, ambulance_coords)
                    if distance <= 100:
                        alerts.append({
                            "driver_id": driver['id'],
                            "ambulance_id": ambulance['id'],
                            "distance": distance
                        })
        
        # Display alert
        for alert in alerts:
            print(f"Alert: Driver {alert['driver_id']} is on the same street as Ambulance {alert['ambulance_id']} and is {alert['distance']} meters away.")
        
        # Wait for a short interval (5 secs) before checking again
        time.sleep(5)  

# Start the alerting system
alert_drivers()
