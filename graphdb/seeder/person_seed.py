names = [
    "Alice", "Tom", "Rohan", "Aman", "Raj", "Deepak", "Harsh", "Ansh", "Rahul", 
    "Alexander", "Benjamin", "Christopher", "Daniel", "Elijah", "Finn", "Gabriel", 
    "Henry", "Isaac", "James", "Leo", "Max", "Oliver", "Ryan", "Theodore"
]

API_URL = 'http://localhost:8111/person'


# Function to make an API call to add a post
def add_post(person):
    data = {"name": person}
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"Post added by {person}: {content}")
        else:
            print(f"Failed to add post by {person}: {response.text}")
    except Exception as e:
        print(f"Error adding post by {person}: {e}")
        
        
for name in names:
    add_post(name)
    time.sleep(0.1)