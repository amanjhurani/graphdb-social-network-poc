
# Social Feed Application with Flask and Neo4j

This is a simple social feed application built using **Flask** (Python) and **Neo4j** (graph database). It allows users to create persons, establish friendships, create posts, and fetch personalized feeds based on their social connections.

---

## Features

1. **Create Persons**: Add new users to the social network.
2. **Create Friendships**: Establish friendships between users.
3. **Create Posts**: Allow users to create posts.
4. **Fetch Feeds**: Retrieve a personalized feed of posts from friends and friends of friends (up to a specified level).

<img width="1380" alt="Screenshot 2025-01-14 at 12 48 09 AM" src="https://github.com/user-attachments/assets/0be5e602-97f5-4574-94a8-2f4ef510e917" />

---

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Neo4j**: Install and run a Neo4j database locally or use a cloud instance.
3. **Flask**: Install Flask and other dependencies.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/social-feed-app.git
   cd social-feed-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Neo4j:
   - Start your Neo4j instance.
   - Update the Neo4j connection details in the `app.py` file:
     ```python
     NEO4J_URI = "bolt://localhost:7687"
     NEO4J_USER = "neo4j"
     NEO4J_PASSWORD = "password"
     ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

   The application will start at `http://localhost:8111`.

---

## API Endpoints

### 1. Create a Person
- **Endpoint**: `POST /person`
- **Request Body**:
  ```json
  {
    "name": "Rohan"
  }
  ```
- **Example**:
  ```bash
  curl --location 'http://localhost:8111/person' \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "Rohan"
  }'
  ```

### 2. Create a Friendship
- **Endpoint**: `POST /friendship`
- **Request Body**:
  ```json
  {
    "person1": "Rohan",
    "person2": "Aman"
  }
  ```
- **Example**:
  ```bash
  curl --location 'http://localhost:8111/friendship' \
  --header 'Content-Type: application/json' \
  --data '{
    "person1": "Rohan",
    "person2": "Aman"
  }'
  ```

### 3. Create a Post
- **Endpoint**: `POST /post`
- **Request Body**:
  ```json
  {
    "person": "Rohan",
    "content": "The use of AI in detecting financial fraud."
  }
  ```
- **Example**:
  ```bash
  curl --location 'http://localhost:8111/post' \
  --header 'Content-Type: application/json' \
  --data '{
    "person": "Rohan",
    "content": "The use of AI in detecting financial fraud."
  }'
  ```

### 4. Fetch Feeds
- **Endpoint**: `GET /feed`
- **Query Parameters**:
  - `person`: The name of the person whose feed is to be fetched.
  - `level`: The depth of friendships to traverse (default: 5).
- **Example**:
  ```bash
  curl --location 'http://localhost:8111/feed?person=Rohan&level=2'
  ```
- **Response**:
  ```json
  [
    {
      "content": "The use of AI in detecting financial fraud.",
      "friend": "Aman",
      "friend_id": 3,
      "post_id": 223,
      "timestamp": 1736792711829
    },
    {
      "content": "The ethics of surveillance technology in smart cities.",
      "friend": "Isaac",
      "friend_id": 17,
      "post_id": 222,
      "timestamp": 1736792711390
    },
    {
      "content": "Machine learning models for image recognition.",
      "friend": "Rahul",
      "friend_id": 8,
      "post_id": 221,
      "timestamp": 1736792710951
    },
    {
      "content": "The rise of quantum computing and its applications.",
      "friend": "Max",
      "friend_id": 20,
      "post_id": 220,
      "timestamp": 1736792710514
    },
    {
      "content": "Innovations in battery technology for sustainable energy.",
      "friend": "Theodore",
      "friend_id": 23,
      "post_id": 219,
      "timestamp": 1736792710080
    }
  ]
  ```

---

## Example Workflow

1. **Create Persons**:
   - Create users like `Rohan`, `Aman`, `Isaac`, etc.

2. **Establish Friendships**:
   - Create friendships between users, e.g., `Rohan` is friends with `Aman`.

3. **Create Posts**:
   - Allow users to create posts, e.g., `Aman` posts about AI.

4. **Fetch Feeds**:
   - Fetch the feed for `Rohan` to see posts from his friends and friends of friends.

---

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **Neo4j**: A graph database for managing social connections.
- **Cypher**: Query language for Neo4j.
