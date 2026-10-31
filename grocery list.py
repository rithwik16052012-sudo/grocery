print("Grocery Billing Queue\n")

# PART 1: The five counters + billing control
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

# PART 2: The OUTER while loop (one customer per repeat)
while billing:
    name = input("Enter customer name: ")
    item_count = int(input(f"Hello {name}, How many items are you buying? "))

    # PART 3: Continue on a bad item count
    if item_count <= 0:
        print("Invalid item count. Please enter a positive number.\n")
        continue

    # PART 4: The INNER while loop setup
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input(f"Enter the name of item {item_number}: ")
        price = int(input(f"Enter the price of {item_name}: "))
        quantity = int(input(f"Enter the quantity of {item_name}: "))

        # PART 5: Item total and price band
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity. Please enter again.\n")
            continue

        item_total = price * quantity
        print(f"{item_name}: {quantity} x ${price} = ${item_total}")
        
        customer_total += item_total

        # Banding categorization based on price thresholds
        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    # PART 6: Finish the customer & ask about the next
    customers_served += 1
    total_sales += customer_total

    print(f"\nTotal bill for {name}: ${customer_total}")
    print("Billing complete\n")

    again = input("Next customer? (yes/no): ").strip().lower()
    if again != "yes":
        billing = False

# PART 7: The NESTED for report & summary metrics
print("\nGrocery Category Report")

# A structure pairing the band names with their item counts
bands = [
    ("Low price items", low_price_items),
    ("Medium price items", medium_price_items),
    ("High price items", high_price_items)
]

for band_name, count in bands:
    print(f"{band_name}: ", end="")
    for _ in range(count):
        print("*", end="")
    print()  # Moves to the next line after finishing the inner loop visualizations

print(f"Customers served: {customers_served}")
print(f"Total sales: ${total_sales}")
print("\nGrocery billing closed. Goodbye.")
