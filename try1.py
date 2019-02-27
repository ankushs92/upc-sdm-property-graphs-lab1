from py2neo import Graph, Node, Relationship
g = Graph(password="wijntje")

a = Node("Person", name="Alice", age=33)
b = Node("Person", name="Bob", age=44)
KNOWS = Relationship.type("KNOWS")
g.merge(KNOWS(a, b), "Person", "name")
c = Node("Company", name="ACME")
c.__primarylabel__ = "Company"
c.__primarykey__ = "name"
WORKS_FOR = Relationship.type("WORKS_FOR")
g.merge(WORKS_FOR(a, c) | WORKS_FOR(b, c))
d = Node("Person", name="Dan", age=6)
g.merge(KNOWS(a,d),"Person", "name")

cursor = g.run("MATCH (n:Person) RETURN n.name")
while cursor.forward():
	print(cursor.current)