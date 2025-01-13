from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def setup_schema(tx):
    tx.run("CREATE CONSTRAINT person_name_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE;")
    tx.run("CREATE INDEX person_name_index IF NOT EXISTS FOR (p:Person) ON (p.name);")
    tx.run("CREATE INDEX post_timestamp_index IF NOT EXISTS FOR (p:Post) ON (p.timestamp);")

with driver.session() as session:
    session.write_transaction(setup_schema)

print("Schema setup completed.")
driver.close()
