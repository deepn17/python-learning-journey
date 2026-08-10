"""
1. 1. Mad Libs Generator — Ask for a noun, a verb, an adjective, and a place.
Print a silly sentence using all four. Example: "The purple elephant danced gracefully at the supermarket."
"""
print(f"\n--- Mad Libs Generator")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")

print(f"The {adjective} {noun} {verb} at the {place}")

"""
2. Restaurant Bill Splitter — Input the total bill, number of people, and tip percentage. 
Compute and print how much each person owes, formatted to 2 decimal places. 
(Sanity check: $84.50 bill, 3 people, 18% tip → $33.24 each.)
"""
total_bill = float(input("Enter the total bill: "))
num_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

tip_amount = total_bill * tip_percentage / 100
final_bill = total_bill + tip_amount
split_amount = final_bill / num_of_people

print(f"Split among {num_of_people} a bill of ${total_bill:.2f} with a tip at {tip_percentage}% comes to ${split_amount:.2f} per person")
