
# 1. Adding Elements


# append(item) = Adds an item to the end of the list.

fruits = ['apple', 'banana']
fruits.append('cherry')
print("List After The append() function: " + str(fruits))  # Output: ['apple', 'banana', 'cherry']



# extend(iterable) = adding another list to the existing list

fruits = ['apple', 'banana']
fruits.extend(['cherry', 'coconut'])
fruits.extend(['pineapple', 'orange'])
print("List After The 2 extend() functions: " + str(fruits))  # Output: ['apple', 'banana', 'cherry', 'date']



# insert(index, item) = Inserts an item at a specific index.

# fruits = ['apple', 'banana']
fruits.insert(0, 'pawpaw')
print("List After The insert(index, item) function: " + str(fruits))  # Output: ['apple', 'cherry', 'banana']



# 2. Removing Elements


# remove(item) = Removes the first occurrence of the specified item.

fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print("List After The remove() function: " + str(fruits))  # Output: ['apple', 'cherry', 'banana']



# pop([index]) = Removes and returns the item at the specified index. Defaults to the last item if no index is provided.

fruits = ['apple', 'banana', 'cherry']
removed = fruits.pop()
print("The Removed Item From The List Is: " + removed)  # Output: 'cherry'
print("List After The pop() function: " + str(fruits))   # Output: ['apple', 'banana']



# clear() = Removes all items from the list.

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print("List After The clear() function: " + str(fruits))  # Output: []



# 3. Finding and Counting


# index(item, [start, [end]]) = Returns the index of the first occurrence of the item. Optional "start" and "end" specify the range to search.

fruits = ['apple', 'banana', 'cherry', 'banana']
print("The New List After The clear() Function Is: " + str(fruits))
print("The Index Of The First Occurrence Of The Banana In Our List: " + str(fruits.index('banana'))) # Output: 1
print("The Index Of The Second Occurrence Of The Banana In Our List: " + str(fruits.index('banana', 2)))       # Output: 3



# count(item) = Counts the number of occurrences of the specified item.

fruits = ['apple', 'banana', 'cherry', 'banana']
print("Counting The Occurrences Of The Banana Fruit In The List With The count() Function: " + str(fruits.count('banana')))  # Output: 2



# 4. Reordering


# sort(key=None, reverse=False) = Sorts the list in ascending order. Use the key parameter for custom sorting and reverse=True for descending order.

numbers = [3, 1, 4, 1, 5]
numbers.sort()
print("List After The sort() function: " + str(numbers))  # Output: [1, 1, 3, 4, 5]

numbers.sort(reverse=True)
print("List After The sort(reverse=True) function: " + str(numbers))  # Output: [5, 4, 3, 1, 1]

# Custom sorting by absolute value
numbers = [-3, -1, 4, 1, -5]
numbers.sort(key=abs)
print("List After The sort(key=abs) function: " + str(numbers))  # Output: [-1, 1, -3, 4, -5]



# reverse() = Reverses the order of the list in place.

numbers = [1, 2, 3, 4]
numbers.reverse()
print("List After The reverse() function: " + str(numbers))  # Output: [4, 3, 2, 1]



# 5. Copying


# copy() = Returns a shallow copy of the list.

fruits = ['apple', 'banana', 'cherry']
copy_fruits = fruits.copy()
print("List After The copy() function: " + str(copy_fruits))  # Output: ['apple', 'banana', 'cherry']



# 6. Other Operations


# __len__() = Returns the length of the list (can also use len()).

fruits = ['apple', 'banana', 'cherry']
print("The Size Of The Given List Above, Using The len() Function: " + str(len(fruits)))  # Output: 3



# __getitem__(index) = Returns the element at a specific index (equivalent to list[index]).

fruits = ['apple', 'banana', 'cherry']
print("Getting The First Item By Using It's Index: " + str(fruits[1]))  # Output: 'banana'



# __setitem__(index, value) = Sets the value at a specific index (equivalent to list[index] = value).

fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'
print("Insertion Of An Item Using It's Index In The List: " + str(fruits))  # Output: ['apple', 'blueberry', 'cherry']



# __delitem__(index) = Deletes the item at a specific index (equivalent to del list[index]).

fruits = ['apple', 'banana', 'cherry']
del fruits[1]
print("Deleting An Item From A List Using It's Index: " + str(fruits))  # Output: ['apple', 'cherry']