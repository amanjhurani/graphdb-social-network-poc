import requests
import random
import time

# API endpoint for adding posts
API_URL = 'http://localhost:8111/post'

# List of names
names = [
    "Alice", "Tom", "Rohan", "Aman", "Raj", "Deepak", "Harsh", "Ansh", "Rahul", 
    "Alexander", "Benjamin", "Christopher", "Daniel", "Elijah", "Finn", "Gabriel", 
    "Henry", "Isaac", "James", "Leo", "Max", "Oliver", "Ryan", "Theodore"
]

# Predefined tech-related posts
tech_posts = [
    "Exploring the future of AI and its impact on society.",
    "The benefits of using Python for data analysis.",
    "Blockchain technology is revolutionizing industries.",
    "Top 5 programming languages to learn in 2025.",
    "How cloud computing is transforming businesses.",
    "The rise of quantum computing and its applications.",
    "Cybersecurity tips to stay safe online.",
    "Machine learning models for image recognition.",
    "Building scalable web applications with Node.js.",
    "IoT devices and their role in smart homes.",
    "The importance of open-source contributions.",
    "5G technology and its potential use cases.",
    "Understanding DevOps practices for faster delivery.",
    "The evolution of mobile app development.",
    "Challenges in big data processing and solutions.",
    "An introduction to AR and VR technologies.",
    "How edge computing complements cloud services.",
    "The significance of ethical AI development.",
    "Best practices for software testing and QA.",
    "A guide to version control with Git.",
    "Data visualization techniques for impactful storytelling.",
    "The role of AI in personalized education.",
    "Developing mobile apps with Flutter and Dart.",
    "How autonomous vehicles use deep learning.",
    "Innovations in battery technology for sustainable energy.",
    "Best tools for project management in tech teams.",
    "How Kubernetes simplifies container orchestration.",
    "Exploring the future of robotics in healthcare.",
    "The impact of technology on climate change solutions.",
    "How VR is enhancing remote collaboration.",
    "An overview of functional programming concepts.",
    "The rise of serverless architecture in cloud computing.",
    "Quantum cryptography and secure communications.",
    "The importance of diversity in tech innovation.",
    "Understanding AI biases and how to mitigate them.",
    "How APIs are shaping the future of software integration.",
    "The journey from monolith to microservices.",
    "Key trends in SaaS product development.",
    "How natural language processing is changing search engines.",
    "The ethics of surveillance technology in smart cities.",
    "The benefits of adopting a CI/CD pipeline.",
    "How tech startups can scale effectively.",
    "Augmented reality in retail: A game-changer.",
    "The future of tech jobs in the age of automation.",
    "Top tools for mastering data engineering.",
    "The role of edge AI in real-time decision-making.",
    "How to secure IoT devices in a connected world.",
    "The use of AI in detecting financial fraud.",
    "Exploring the evolution of programming frameworks.",
    "The intersection of biology and technology: Bioinformatics.",
    "The rise of AI-powered virtual assistants in daily life."
]

# Function to make an API call to add a post
def add_post(person, content):
    data = {"person": person, "content": content}
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"Post added by {person}: {content}")
        else:
            print(f"Failed to add post by {person}: {response.text}")
    except Exception as e:
        print(f"Error adding post by {person}: {e}")

# Generate 200 posts ensuring each person has at least one post

def generate_posts(names, tech_posts, total_posts):
    posts_created = 0
    
    # Ensure each person has at least one post
    for name in names:
        content = random.choice(tech_posts)
        add_post(name, content)
        posts_created += 1
        
    # Create remaining posts randomly
    while posts_created < total_posts:
        person = random.choice(names)
        content = random.choice(tech_posts)
        add_post(person, content)
        posts_created += 1
        
        # Avoid overwhelming the API
        time.sleep(0.1)

# Start generating posts
total_posts = 200
generate_posts(names, tech_posts, total_posts)
