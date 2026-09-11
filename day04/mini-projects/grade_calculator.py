print("=" * 50)
print("Grade Calculator")
print("=" * 50)

grades = {}

while True:
    name = input("\nStudent name (or 'done'): ").strip()
    if name.lower() == 'done':
        break
    score = int(input(f"{name}'s score (0 - 100): "))
    grades[name] = score

if not grades:
    print("No students entered.")
else:
    scores = list(grades.values())
    print("\n--- Results ---")
    for name, score in grades.items():
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"
        print(f"{name:<12} {score:>3}  {letter}")

    print(f"\nClass Average: {sum(scores) / len(scores):.1f}")
    print(f"Highest: {max(scores)}  Lowest: {min(scores)}")