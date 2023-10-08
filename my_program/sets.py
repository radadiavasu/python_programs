art_friends = {"vasu", "kunj", "vansh", "jay"}
science_friends = {"kshtij", "vasu", "dhruvil", "parth"}

# art_but_not_friends = art_friends.difference(science_friends) # print only who are in art
# science_but_not_friends = science_friends.difference(art_friends) # print only who are in science

# art_but_not_friends = art_friends.symmetric_difference(science_friends)
# science_but_not_friends = science_friends.symmetric_difference(art_friends)

art_but_not_friends = art_friends.union(science_friends) # Remove duplicate elements

print(art_but_not_friends)
# print(science_but_not_friends)