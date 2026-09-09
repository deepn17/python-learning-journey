# COMMON MISTAKES TO AVOID
----------------------------------------------------------------------
fruits = ["apple", "banana"]
fruits.append("cherry", "date")     wrong  
append takes only ONE argument, so for multiple use extend
fruits.append("cherry")
fruits.extend(["cherry", "date"])
----------------------------------------------------------------------
result = nums.sort()               
nums.sort()                        
sort() returns None, so first sort() nums and then use the sorted nums
----------------------------------------------------------------------
single = (5)  this is an int, not a tuple
single = (5,) trailing comma makes a tuple
----------------------------------------------------------------------
person = {"name": "Alice"}
print(person["age"])    KeyError if key missing
print(person.get("age"))  returns None safely
----------------------------------------------------------------------
s = {1, 2, 3}
print(s[0])                        # sets have no order/index
for item in s: print(item)         # loop instead
----------------------------------------------------------------------
nums = [1, 2, 3]
nums[3] = 4                        # IndexError: out of range
nums.append(4)                     # use append to grow
----------------------------------------------------------------------
a = [1, 2, 3]
b = a                              # b is the SAME list, not a copy
b.append(4)
print(a)                           # [1, 2, 3, 4]  ← a changed too!
so first copy the list with copy() method
b = a.copy()                       # or b = a[:]  → real copy
----------------------------------------------------------------------