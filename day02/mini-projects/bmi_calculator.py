# BMI Calculator

weight_input = input("Weight (kg): ").strip()
height_input = input("Height (m): ").strip()

if not weight_input or not height_input:
    print("Missing input. Skipping BMI calculation.")
else:
    weight = float(weight_input)
    height = float(height_input)

    if weight <= 0 and height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        bmi = weight / (height ** 2)
        print(f"\n📏 Your BMI: {bmi:.1f}")

        if bmi < 18.5:
            category = "Underweight"
            tip = "Consider consulting a nutritionist."
        elif bmi < 25:
            category = "Normal weight"
            tip = "Keep up the good work!"
        elif bmi < 30:
            category = "Overweight"
            tip = "Regular exercise can help."
        else:
            category = "Obese"
            tip = "Consider consulting a healthcare provider."

        print(f"   Category: {category}")
        print(f"   Tip: {tip}")