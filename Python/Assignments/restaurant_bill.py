def calculate_restaurant_bill(meal_cost):
    service_charge = meal_cost * 0.10
    amount_after_service = meal_cost + service_charge
    tax = amount_after_service * 0.05
    tip_amount = amount_after_service * 0.05
    total = amount_after_service + tax + tip_amount

    print(f"Meal Cost: {meal_cost}")
    print(f"Service Charge (10%): {service_charge}")
    print(f"Amount after Service: {amount_after_service}")
    print(f"Tax (5%): {tax}")
    print(f"Tip (5%): {tip_amount}")
    print(f"Total Bill: {total}")

    return total


meal_cost = float(input("Enter the meal cost: "))
returned_total = calculate_restaurant_bill(meal_cost)
print(f"Return: {returned_total}")


