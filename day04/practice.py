# PRACTICE 1: Reverse a List
# GOAL: Reverse a list WITHOUT using .reverse() or slicing.
# EXAMPLE: [1, 2, 3, 4] → [4, 3, 2, 1]

# using a new list
numbers = [1, 2, 3, 4]
reverse_list = []
for num in range(len(numbers)-1, -1, -1):
    reverse_list.append(numbers[num])

print(reverse_list)

# using insert(0, ...)
numbers = [1, 2, 3, 4]
reversed_numbers = []

for number in numbers:
    reversed_numbers.insert(0, number)

print(reversed_numbers)

# PRACTICE 2: Second-Largest
# GOAL: Find the second-largest number in a list.
# HINTS: sort a copy, or track top two with a loop
# EXAMPLE: [3, 7, 2, 9, 5] → 7
# with sort
num_list = [3, 7, 2, 9, 5]
sort_list = num_list.copy()
sort_list.sort()
print(sort_list[-2])

# with track top two with a loop
largest = float("-inf")
second_largest = float("-inf")

for number in num_list:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print(second_largest)

# PRACTICE 3: Merge Two Lists
# GOAL: Merge two sorted lists into one sorted list.
# HINTS: combine with +, then sort; or use two pointers
# EXAMPLE: [1, 3, 5] + [2, 4, 6] → [1, 2, 3, 4, 5, 6]
# with combine with + and sort
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = list1 + list2
merged.sort()
print(merged)

# with 2 pointer approach
list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged = []

i = 0
j = 0

while i < len(list1) and j <  len(list2):

    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list1):
    merged.append(list2[j])
    j += 1

print(merged)

# PRACTICE 4: Common Elements
# GOAL: Find the elements common to two lists (intersection).
# HINTS: convert both to sets and use &
# EXAMPLE: [1, 2, 3, 4] and [3, 4, 5, 6] → {3, 4}

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

print(common)

# PRACTICE 5: Dictionary Inversion
# GOAL: Swap keys and values in a dictionary (assume values unique).
# HINTS: loop over items(), build a new dict
# EXAMPLE: {"a": 1, "b": 2} → {1: "a", 2: "b"}
original = {"a": 1, "b": 2}
inverted = {}

for key, value in original.items():
    inverted[value] = key

print(inverted)

# PRACTICE 6: Flatten a Nested List
# GOAL: Turn a list of lists into a single flat list.
# HINTS: nested loop, or a list comprehension with two fors
# EXAMPLE: [[1, 2], [3, 4], [5]] → [1, 2, 3, 4, 5]
nested_list = [[1, 2], [3, 4], [5]]

flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)