friends = ["Rolf", "Sam", "Samanta", "Bob", "Alex"]
friends_clone = friends
friends_list = [friend for friend in friends]

print(friends)
print(friends_clone)
print(friends_list)
print(friends is friends_clone)
print(friends is friends_list)
print(friends == friends_clone)
print(friends == friends_list)
print(friends[2] is friends_list[2])
print("friends id: ", id(friends), "; friends_clone id: ", id(friends_clone), "; friends_list id: ", id(friends_list))