# CHALLENGE 1: List Statistics
# GOAL: Ask the user for 5 numbers, store them in a list, then print
# the sum, average, minimum, and maximum.
# EXAMPLE:
#   Enter number 1: 10
#   Enter number 2: 20
#   Enter number 3: 30
#   Enter number 4: 40
#   Enter number 5: 50
#   Sum = 150, Average = 30.0, Min = 10, Max = 50


num_list = []
counter = 5
num = 1

while num <= 5:
    nums = int(input(f"Enter number {num}: "))
    num_list.append(nums)
    num += 1

sum_of_numbers = sum(num_list)
avg_of_numbers = sum_of_numbers / len(num_list)
min_of_numbers = min(num_list)
max_of_numbers = max(num_list)

print(f"Sum: {sum_of_numbers}")
print(f"Average: {avg_of_numbers}")
print(f"Minimum: {min_of_numbers}")
print(f"Maximum: {max_of_numbers}")

# CHALLENGE 2: Remove Duplicates
# GOAL: Take a list with duplicates and return a new list with only
#       unique items, preserving order.

# EXAMPLE:
#   Input:  [1, 2, 2, 3, 4, 4, 5]
#   Output: [1, 2, 3, 4, 5]


numbers = [1, 2, 2, 3, 4, 4, 5]

seen = set()
unique_numbers = []

for number in numbers:
    if number not in seen:
        seen.add(number)
        unique_numbers.append(number)

print(unique_numbers)

# CHALLENGE 3: Word Frequency Counter
# GOAL: Take a sentence and count how many times each word appears.
#       Print each word and its count.

# EXAMPLE:
#   Enter a sentence: the cat and the dog
#   the: 2
#   cat: 1
#   and: 1
#   dog: 1

freq = {}
sentence = input("Enter a sentence: ")

for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word}: {count}")

# CHALLENGE 4: To-Do List Manager
# GOAL: Build a menu-driven to-do list. The user can add, view,
#       remove, and quit. Keep the list in memory.

# EXAMPLE:
#   1. Add task
#   2. View tasks
#   3. Remove task
#   4. Quit
#   Choose: 1
#   Task: Buy milk

task_list = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    selection = input("Enter the number from (1 - 4) for what you want to do: ").strip()

    if selection == "1":
        add_task = input("Add a Task: ").strip()
        task_list.append(add_task)
    elif selection == "2":
        for index, task in enumerate(task_list):
            print(f"#{index + 1}: {task}")
    elif selection == "3":
        for index, task in enumerate(task_list):
            print(f"#{index + 1}: {task}")

        remove_task = int(input("Enter the task id you want to remove: "))
        if remove_task < 1 or remove_task > len(task_list):
            print("Enter a valid id that you see for the task.")
        else:
            task_list.pop(remove_task - 1)
    elif selection == "4":
        break
    else:
        print("Please enter a valid choice between (1 - 4)")

# CHALLENGE 5: Student Gradebook
# GOAL: Store student names and their scores in a dictionary. Then
#       print each student, their score, and the class average.
#
# EXAMPLE:
#   Enter student name (or 'done'): Alice
#   Enter Alice's score: 85
#   Enter student name (or 'done'): Bob
#   Enter Bob's score: 92
#   Enter student name (or 'done'): done
#   Alice: 85
#   Bob: 92
#   Class average: 88.5

student_stats = {}
while True:
    student_name = input("Enter student name (or 'done'): ").lower().strip()
    if student_name == 'done':
        break
    else:
        student_score = int(input(f"Enter {student_name}'s score: "))
        student_stats[student_name] = student_score

for key, value in student_stats.items():
    print(f"{key.capitalize()}: {value}")
class_avg = sum(student_stats.values()) / len(student_stats.keys())
print(f"Class average: {class_avg}")

# CHALLENGE 6: Matrix Transpose
# GOAL: Given a 2D list (matrix), return its transpose (rows become
#       columns and columns become rows).
# solve it with nested loops, and also with zip(*matrix)
# EXAMPLE:
#   Input:  [[1, 2, 3],
#            [4, 5, 6]]
#   Output: [[1, 4],
#            [2, 5],
#            [3, 6]]

# with nested loops
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for col in range(len(matrix[0])):
    new_row = []

    for row in range(len(matrix)):
        new_row.append(matrix[row][col])

    transpose.append(new_row)

print(transpose)

# with zip
transpose = [list(row) for row in zip(*matrix)]
print(transpose)