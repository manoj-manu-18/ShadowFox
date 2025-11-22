#.You and your partner are planning a trip, and you want to track expenses Create two dictionaries, one for your expenses and one for your partner's expenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts.
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses: $", your_total)
print("Partner's total expenses: $", partner_total)

if your_total > partner_total:
    print("You spent more money overall.")
elif your_total < partner_total:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount.")

max_difference = 0
category_with_max_difference = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        category_with_max_difference = category

print(f"The category with the most significant difference is '{category_with_max_difference}' with a difference of ${max_difference}.")
        