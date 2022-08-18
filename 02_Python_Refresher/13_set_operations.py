cities = {"Toronto", "Edmonton", "Calgary"}
alberta = {"Edmonton", "Calgary"}
ontario = cities.difference(alberta)
print(ontario)

ontario2 = {"Toronto"}
alberta2 = {"Edmonton", "Calgary"}
cities2 = ontario2.union(alberta2)
print(cities2)

art = {"Bob", "Jen", "Rolf", "Ann"}
science = {"Bob", "Adam", "Jen", "Chris"}
both = art.intersection(science)
print(both)
