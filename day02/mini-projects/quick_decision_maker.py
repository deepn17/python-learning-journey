# Quick Decision Maker
print("\n--- Quick Decision Maker ---")
print("Can't decide? Let me help!")
print("1. Should I go out?")
print("2. What should i eat?")
print("3. Should i study or relax?")

choice = input("Pick a dilemma (1-3): ").strip()

if choice == "1":
    weather = input("Is it raining? (yes/no): ").lower().strip()
    tired = input("Are you tired? (yes/no): ").lower().strip()

    if weather == "yes":
        print("🌧️  Stay in! It's raining outside.")
    elif tired == "yes":
        print("😴  Maybe rest today and go out tomorrow.")
    else:
        print("🌤️  Go out and enjoy the day!")

elif choice == '2':
    budget = input("Do you have a budget? (low/medium/high): ").lower().strip()

    if budget == "low":
        print("🍜  Try instant noodles or a homemade sandwich.")
    elif budget == "medium":
        print("🍕  How about pizza or a nice biryani?")
    elif budget == "high":
        print("🥩  Treat yourself to a fancy restaurant!")
    else:
        print("🤷  Let's just order whatever you're craving.")

elif choice == "3":
    energy = input("Energy level (low/medium/high): ").lower().strip()
    deadline = input("Is there a deadline? (yes/no): ").lower().strip()

    if deadline == "yes":
        print("📚  Deadline first! Study now, relax later.")
    elif energy == "low":
        print("🛋️  You're low on energy. Take a break and relax.")
    else:
        print("📖  You've got energy — make progress while you can!")

else:
    print("Invalid choice. The universe says: flip a coin! 🪙")
