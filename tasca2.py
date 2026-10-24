import csv

# Inicialitzem un diccionari per a cada producte
product_customers = {}

with open("products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product_customers[row["id"]] = set() # Inicialitzem amb set() per evitar duplicats

# Llegim ordres i associem els customers amb els seus productes
with open("orders.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer_id = row["customer"]
        product_ids = row["products"].split()

        for product_id in product_ids:
            product_customers[product_id].add(customer_id)


# Generem product_customers.csv
with open("product_customers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "customer_ids"]
    )
    writer.writeheader()

    for product_id, customer_ids in product_customers.items():
        writer.writerow({
            "id": product_id,
            "customer_ids": " ".join(sorted(
                customer_ids, key=int
            ))
        })
