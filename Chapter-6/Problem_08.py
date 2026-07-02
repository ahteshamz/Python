# A contractor is ordering truckloads of gravel for a road project.
# Each truckload costs ₹4,500.
# Write a Python program that:
# Asks the user to enter the number of truckloads required. Calculates the total cost using a loop. If the number of truckloads is more than 20, apply a 10% discount. If the number of truckloads is more than 50, apply a 15% discount. Prints: Original cost Discount amount Final cost after discount


cost_per_truck = 4500

truckloads = int(input("Enter the number of truckloads required: "))

original_cost = 0
for i in range(truckloads):
    original_cost += cost_per_truck

if truckloads > 50:
    discount_rate = 0.15
elif truckloads > 20:
    discount_rate = 0.10
else:
    discount_rate = 0.0

discount_amount = original_cost * discount_rate
final_cost = original_cost - discount_amount

# Print results
print("Original cost: ₹", original_cost)
print("Discount amount: ₹", discount_amount)
print("Final cost after discount: ₹", final_cost)
