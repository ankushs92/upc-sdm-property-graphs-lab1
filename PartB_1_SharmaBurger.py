from py2neo import Graph, Node, Relationship, Transaction, Database


db = Database
graph = Graph(user = "neo4j", password = "root")


author_ankush = Node("Author", name ="Ankush")
ankush_paper_1 = Node("Paper", name = "Paper 1 ")
ankush_paper_2 = Node("Paper", name = "Paper 2 ")
ankush_paper_3 = Node("Paper", name = "Paper 3 ")
ankush_paper_4 = Node("Paper", name = "Paper 4 ")
ankush_paper_5 = Node("Paper", name = "Paper 5 ")
conf1 = Node("Conf1", name="Conf1")
edition1_conf1 = Node("edition", name="edition1")
edition2_conf1 = Node("edition", name="edition2")
edition3_conf1 = Node("edition", name="edition3")
edition4_conf1 = Node("edition", name="edition4")
edition5_conf1 = Node("edition", name="edition5")


author_edition1 = Relationship(edition1_conf1, "has", author_ankush)
author_edition2 = Relationship(edition2_conf1, "has", author_ankush)
author_edition3 = Relationship(edition3_conf1, "has", author_ankush)

rel1 = Relationship(author_ankush, "Wrote", ankush_paper_1)
rel2 = Relationship(author_ankush, "Wrote", ankush_paper_2)
rel3 = Relationship(author_ankush, "Wrote", ankush_paper_3)
rel4 = Relationship(author_ankush, "Wrote", ankush_paper_4)
rel5 = Relationship(author_ankush, "Wrote", ankush_paper_5)

paper_1_conf1 = Relationship(ankush_paper_1, "Presented_at", conf1)
paper_2_conf1 = Relationship(ankush_paper_2, "Presented_at", conf1)
paper_3_conf1 = Relationship(ankush_paper_3, "Presented_at", conf1)
paper_4_conf1 = Relationship(ankush_paper_4, "Presented_at", conf1)
paper_5_conf1 = Relationship(ankush_paper_5, "Presented_at", conf1)

edition1_conf1_rel1 = Relationship(edition1_conf1, "PartOf", conf1)
edition2_conf1_rel2 = Relationship(edition2_conf1, "PartOf", conf1)
edition3_conf1_rel3 = Relationship(edition3_conf1, "PartOf", conf1)
edition4_conf1_rel4 = Relationship(edition4_conf1, "PartOf", conf1)
edition5_conf1_rel5 = Relationship(edition5_conf1, "PartOf", conf1)

tx = graph.begin()

tx.create(author_edition1)
tx.create(author_edition2)
tx.create(author_edition3)

tx.create(author_ankush)
tx.create(ankush_paper_1)
tx.create(ankush_paper_2)
tx.create(ankush_paper_3)
tx.create(ankush_paper_4)
tx.create(ankush_paper_5)

tx.create(rel1)
tx.create(rel2)
tx.create(rel3)
tx.create(rel4)
tx.create(rel5)

tx.create(conf1)

tx.create(paper_1_conf1)
tx.create(paper_2_conf1)
tx.create(paper_3_conf1)
tx.create(paper_4_conf1)
tx.create(paper_5_conf1)

tx.create(edition1_conf1)
tx.create(edition1_conf1_rel1)
tx.create(edition2_conf1)
tx.create(edition2_conf1_rel2)
tx.create(edition3_conf1)
tx.create(edition3_conf1_rel3)
tx.create(edition4_conf1)
tx.create(edition4_conf1_rel4)
tx.create(edition5_conf1)
tx.create(edition5_conf1_rel5)

tx.commit()


print(db)
print(graph)