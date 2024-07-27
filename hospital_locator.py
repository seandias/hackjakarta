import math
import heapq

# Function to calculate the distance between Hospital and User
def haversine(lat1, lon1, lat2, lon2):
    # Converting latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers.
    r = 6371
    return c * r

# List of hospitals with their coordinates (latitude, longitude)
hospitals = [
    {"name": "Hospital A", "latitude": -6.200000, "longitude": 106.816666},
    {"name": "Hospital B", "latitude": -6.174465, "longitude": 106.822745},
    {"name": "Hospital C", "latitude": -6.208763, "longitude": 106.845599},
    {"name": "Hospital D", "latitude": -6.241587, "longitude": 106.989570}
]

# Function to find the nearest hospitals
def find_nearest_hospitals(user_lat, user_lon, hospitals, k=3):
    # Calculate the distance to each hospital
    distances = []
    for hospital in hospitals:
        distance = haversine(user_lat, user_lon, hospital["latitude"], hospital["longitude"])
        distances.append((distance, hospital))
    
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
    print(f"{hospital['name']}")


