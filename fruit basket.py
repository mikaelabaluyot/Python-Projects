#Create two sets representing your favorite fruits and your best friend's favorite fruits.
#Print the union of the two sets would look like.
#Print the intersection of the two sets.




my_fruits = {'watermelon', 'mandarin', 'apple', 'grapes'}
her_fruits = {'papaya', 'apple', 'melon', 'dragonfruit', 'granadilla'}

union_fruits = my_fruits.union(her_fruits)

difference_fruits = my_fruits.difference(her_fruits)

intersection_fruits = my_fruits.intersection(her_fruits)

print("our fruits: ", union_fruits)
print("difference fruits: ", difference_fruits)
print("similar fruits: ",intersection_fruits)
