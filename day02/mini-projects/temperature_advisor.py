# Temperature Advisor
temp_input = input("What's the temperature in °C? ").strip()

if not temp_input:
    print("No input. Skipping temperature check.")
else:
    temp = float(temp_input)

    if temp < 0:
        advice = "❄️  Freezing! Wear a heavy coat, gloves, and a scarf."
    elif temp < 10:
        advice = "🥶 Cold. A warm jacket is a good idea."
    elif temp < 20:
        advice = "🍂 Cool. A light jacket or hoodie should do."
    elif temp < 30:
        advice = "☀️  Pleasant. T-shirt weather!"
    elif temp < 40:
        advice = "🔥 Hot! Stay hydrated and wear sunscreen."
    else:
        advice = "🥵 Extremely hot! Stay indoors if possible."
    print(f"\n🌡️  {temp}°C → {advice}")
