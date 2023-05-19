candy_colors = ['baby pink', 'powder blue', 'cloud white', 'yellow sunshine']
sweet_snacks = ['ice cream', 'vanilla milkshake']

# len()
print(len(candy_colors)) # 4

# Grabbing a specific element from the list - list[0]
print(candy_colors[1]) # powder blue

# last item - list[-1]
print(candy_colors[-1]) # yellow sunshine

# grabbing a range of values - list[0:2] - first index is inclusive, second is not
print(candy_colors[0:2]) # ['baby pink', 'powder blue']

# slicing - list[2:]
print(candy_colors[2:]) # ['cloud white', 'yellow sunshine']

# ~~~~~~~ modifying lists

# Adding an item to the end of the list - .append('item')
candy_colors.append('grassy green')
print(candy_colors)

# Removing values - .remove('item'), .pop()
candy_colors.remove('grassy green')
print(candy_colors)

# Adding an item at a particular position - .insert(0, 'item')
candy_colors.insert(1, 'lavender lilac')
print(candy_colors)

# When we want to add multiple values to the list - .extend(list2)
candy_colors.extend(sweet_snacks)
print(candy_colors)
    # If we insert a list to another list, instead of inserting the items, the list will be added to that position
candy_colors.insert(0, sweet_snacks)
print(candy_colors)
candy_colors.remove(['ice cream', 'vanilla milkshake'])

# ~~~~~~~ sorting lists

nums = [1, 5, 2, 3, 4]

# Sorts the list - sorted(list) - DOESN'T ALTER THE LIST
print(sorted(nums)) # [1, 2, 3, 4, 5]

# Sorting the list - .sort() - ALTERS THE LIST
nums.sort()
print(nums) # [1, 2, 3, 4, 5]

# Reversing the list - .reverse()
nums.reverse()
print(nums) # [5, 4, 3, 2, 1]

# Sorts the list and displays it in reverse order - .sort(reverse=True) - ALTERS THE LIST
nums.sort(reverse=True)
print(nums) # [5, 4, 3, 2, 1]

print(max(nums)) # 5
print(min(nums)) # 1
print(sum(nums)) # 15

# Finding the index of an item in a list - .index('item')
print(candy_colors.index('baby pink')) # 0

# Checking if an item is in a list - 'item' in list
print('grassy green' in candy_colors) # False

# ~~~~~~~ Looping values

# Looping through the list
for color in candy_colors:
    print(color)

# Function that returns the index and the value in the loop
for index, color in enumerate(candy_colors):
    print(index, color)

# Function that returns the index and the value in the loop, and starts at a particular position
for index, color in enumerate(candy_colors, start=1):
    print(index, color)

# ~~~~~~~ Join/split

# Joining the values of a list into a single string
candy_colors_str = ' - '.join(candy_colors)
print(candy_colors_str)

# Splitting a string and making a list out of its values
new_candy_colors = candy_colors_str.split(' - ')
print(new_candy_colors)

# ~~~~~~~ Sets

# Most used to: test whether a value is part of a set, remove duplicates
# Sets perform the 'item' in Set operation more efficiently than lists and tuples
# Doesn't care about order
# Intersection - .intersection(set2)
# Everything that's on set1 and NOT on set2 - .difference(set2)
# Union - .union(set2)
candy_colors_set = {'baby pink', 'powder blue', 'lavender lilac', 'cloud white', 'lavender lilac'}
print(candy_colors_set)

# ~~~~~~~ Empty lists, tuples and sets

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dictionary
empty_set = set()