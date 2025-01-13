from flask import Flask, request, jsonify
from neo4j import GraphDatabase

# Initialize Flask app
app = Flask(__name__)

# Neo4j Database connection details
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Create a new person
def create_person(tx, name):
    tx.run("MERGE (p:Person {name: $name})", name=name)

# Create a friendship between two people
def create_friendship(tx, person1, person2):
    tx.run(
        "MATCH (a:Person {name: $person1}), (b:Person {name: $person2})\n"
        "MERGE (a)-[:FRIEND]->(b)",
        person1=person1,
        person2=person2,
    )

# Create a post for a person
def create_post(tx, person, content):
    tx.run(
        "MATCH (p:Person {name: $person})\n"
        "CREATE (p)-[:POSTED]->(:Post {content: $content, timestamp: timestamp()})",
        person=person,
        content=content,
    )

def fetch_posts(tx, person, level):
    query = (
        "MATCH (p:Person {name: $person})-[:FRIEND*1..%d]-(friend:Person)-[:POSTED]->(post:Post)\n"
        "RETURN DISTINCT friend.name AS friend, post.content AS content, post.timestamp AS timestamp, id(post) AS post_id, id(friend) AS friend_id\n"
        "ORDER BY post.timestamp DESC"
    ) % level
    result = tx.run(query, person=person)
    return [
        {
            "friend": record["friend"],
            "content": record["content"],
            "timestamp": record["timestamp"],
            "post_id": record["post_id"],
            "friend_id": record["friend_id"]
        }
        for record in result
    ]
@app.route("/person", methods=["POST"])
def add_person():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    with driver.session() as session:
        session.write_transaction(create_person, name)
    return jsonify({"message": "Person created successfully"})

@app.route("/friendship", methods=["POST"])
def add_friendship():
    data = request.json
    person1 = data.get("person1")
    person2 = data.get("person2")
    if not person1 or not person2:
        return jsonify({"error": "Both person1 and person2 are required"}), 400

    with driver.session() as session:
        session.write_transaction(create_friendship, person1, person2)
    return jsonify({"message": "Friendship created successfully"})

@app.route("/post", methods=["POST"])
def add_post():
    data = request.json
    person = data.get("person")
    content = data.get("content")
    if not person or not content:
        return jsonify({"error": "Person and content are required"}), 400

    with driver.session() as session:
        session.write_transaction(create_post, person, content)
    return jsonify({"message": "Post created successfully"})

@app.route("/feed", methods=["GET"])
def get_feed():
    person = request.args.get("person")
    level = request.args.get("level", default=5, type=int)

    if not person:
        return jsonify({"error": "Person is required"}), 400

    with driver.session() as session:
        posts = session.read_transaction(fetch_posts, person, level)

    return jsonify(posts)




if __name__ == "__main__":
    app.run(port=8111)
