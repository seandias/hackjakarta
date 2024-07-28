import googlemaps
import heapq

API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

# List of hospitals with their coordinates (latitude, longitude)(dummy data)
hospitals = [
    {"name": "Hospital A", "latitude": -6.200000, "longitude": 106.816666},
    {"name": "Hospital B", "latitude": -6.174465, "longitude": 106.822745},
    {"name": "Hospital C", "latitude": -6.208763, "longitude": 106.845599},
    {"name": "Hospital D", "latitude": -6.241587, "longitude": 106.989570}
]

# Locate the nearest hospitals using Google Maps Distance Matrix API
def find_nearest_hospitals(user_lat, user_lon, hospitals, k=3):
    user_location = (user_lat, user_lon)
    hospital_locations = [(hospital["latitude"], hospital["longitude"]) for hospital in hospitals]

    # Get distances
    result = gmaps.distance_matrix(origins=[user_location], destinations=hospital_locations, mode="driving")

    # Parse results
    distances = []
    for i, row in enumerate(result['rows'][0]['elements']):
        distance = row['distance']['value']  # distance in meters
        distances.append((distance, hospitals[i]))

    # Find the k nearest hospitals
    nearest_hospitals = heapq.nsmallest(k, distances)
    return nearest_hospitals

# Example user location
user_lat = -6.21462
user_lon = 106.84513

# Find the nearest hospitals
nearest_hospitals = find_nearest_hospitals(user_lat, user_lon, hospitals)

# Return the nearest hospitals
for distance, hospital in nearest_hospitals:
    print(f"{hospital['name']} is {distance/1000:.2f} km away")
