# Check odd values
# ages = [45, 27, 72, 62, 20]
# odds = [age for age in ages if age % 2 == 1]

# Dictonaries comprehences

friends = ["Vasu", "Kunj", "Rolf", "Jay"]
friernds_set = [0, 3, 6, 8]

''' We can also use zip function in this code. zip function
    nothing but combine the above friends & friends_set. 
'''

define_friends = {
    friends[i]: friernds_set[i]
    for i in range(len(friends))
    if friernds_set[i] > 5
}
print(define_friends)