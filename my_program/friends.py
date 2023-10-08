freinds = input("Enter Three names Seprated by Commas (No Spaces, Please): ").split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

freinds_set = set(freinds)
people_nearby_set = set(people_nearby)

friends_nearby_set = freinds_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friends in friends_nearby_set:
    print(f'{friends} is nearby, Meet up with him')
    nearby_friends_file.write(f'{friends}\n')
    
nearby_friends_file.close()