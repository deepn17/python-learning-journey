# ============================================================
# PRACTICE 1: Temperature Classifier
# ============================================================
# Classify a temperature (in °C) into one of:
#   Below 0:    "Freezing"
#   0 to 15:    "Cold"
#   16 to 25:   "Mild"
#   26 to 35:   "Warm"
#   Above 35:   "Hot"

temperature = float(input("Enter the temperature: "))

if temperature < 0:
    print("Freezing")
elif temperature < 16:
    print("Cold")
elif temperature < 26:
    print("Mild")
elif temperature < 36:
    print("Warm")
else:
    print("Hot")

# the above range has been selected based on temperature being float, if int, then the range would change, like 0 <= temperature <= 15, <=16 temperature <= 25 etc etc.

