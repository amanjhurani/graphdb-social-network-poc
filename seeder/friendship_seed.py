import requests
import random
import itertools
import time

# API endpoint
API_URL = 'http://localhost:8111/friendship'

# List of names
names = [
    "Alice", "Tom", "Rohan", "Aman", "Raj", "Deepak", "Harsh", "Ansh", "Rahul", 
    "Alexander", "Benjamin", "Christopher", "Daniel", "Elijah", "Finn", "Gabriel", 
    "Henry", "Isaac", "James", "Leo", "Max", "Oliver", "Ryan", "Theodore"
]

# Function to make an API call to establish a friendship
def make_friendship(person1, person2):
    data = {"person1": person1, "person2": person2}
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"Friendship created between {person1} and {person2}")
        else:
            print(f"Failed to create friendship between {person1} and {person2}: {response.text}")
    except Exception as e:
        print(f"Error creating friendship between {person1} and {person2}: {e}")

# Generate random friendships
max_levels = 6

# Helper function to create friendships up to the specified levels
def generate_friendships(names, levels):
    for level in range(levels):
        print(f"Creating level {level + 1} friendships...")
        # Shuffle names to create random pairs
        random.shuffle(names)
        for i in range(0, len(names) - 1, 2):
            person1, person2 = names[i], names[i + 1]
            make_friendship(person1, person2)

        # Introduce random new friends to deepen connections
        for _ in range(len(names) // 2):
            person1, person2 = random.sample(names, 2)
            make_friendship(person1, person2)

        # Simulate delay between levels to avoid overwhelming the API
        time.sleep(2)

# Start generating friendships
generate_friendships(names, max_levels)
