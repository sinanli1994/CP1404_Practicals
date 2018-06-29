print("Electricity bill estimator")

price = float(input("Enter cents per kWh"))
usage = float(input("Enter daily use in kWh"))
days = int(input("Enter number of billing days"))

print("Estimated bill:$", price*usage*days/100)