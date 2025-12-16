#Question 1

inventory = {
    "Tomatoes": {"stock":150, "price_per_unit": 5.0},
    "Onions": {"stock":80, "price_per_unit": 3.5},
    "Garden Eggs": {"stock":200, "price_per_unit": 1.0}
}

while True:
    print("Welcome to Aunty Gifty's Vegetables.")
    print("Our Items For Sale.")
    print("1. Tomatoes")
    print("2. Onions")
    print("3. Garden Eggs")
    print("4. exit")
    option = input("Enter item name to purchase or 'exit': ")

    if option == "exit":
        print("Closing sales. Total transactions completed.")
        break
        
    elif option in inventory :
        amount = int(input("Enter Quantity To Buy: "))
        total_cost = amount * inventory[option]["price_per_unit"]
        total_cost = round(total_cost, 2)
        
        if amount > inventory[option]["stock"]:
            print(f"Sorry, only {inventory[option]['stock']} units of {option} remaining. ")
        else:
            inventory[option]["stock"] -= amount
            print(f"Sale successful! Cost: GHS {total_cost}. \n{inventory[option]['stock']} units of {option} remaining. ")
            
    else:
        print("Item not found in stock. Check spelling.")

 #Question 2
       
fixed_monthly_charge = 15.00

consumption = float(input("Total water consumption for the month (in cubic meters): "))

if consumption >= 0 and consumption <= 15:rate = 0.90

elif consumption >= 16 and consumption <= 30:rate = 1.20
    
elif consumption > 30: rate = 1.80
    
else: 
    print("Invalid input, please try again.")
    rate = 0
    
total_bill = fixed_monthly_charge + consumption * rate
total_cost = round(total_bill, 2)

print("--- Monthly Water Bill Summary ---")
print(f"Consumption: {consumption} cubic meters")
print("fixed monthly charge: GHS15.00")
print(f"Consumption cost: GHS {round(consumption * rate, 2)}")
print(f"Total cost: GHS{total_cost}")



#Question 3
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
speed_limit = 100
speeding_violations = []

for speed in recorded_speeds:
    if speed > speed_limit:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {speed_limit} km/h.")
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
violations_recorded = len(speeding_violations)
percentage_speeding = (violations_recorded / total_vehicles) * 100

print("\nTraffic Speed Data")
print(f"Total number of vehicles recorded: {total_vehicles}")
print(f"Total number of speeding violations: {violations_recorded}")
print(f"Percentage of speeding vehicles: {round(percentage_speeding, 2)}%")
print(f"Average speed: {round(sum(recorded_speeds) / total_vehicles, 2)} km/h")

focused_segment = recorded_speeds[2:8]
print(f"Speeds for focused inspection segment (3rd to 8th vehicle): {focused_segment}")
        
        
