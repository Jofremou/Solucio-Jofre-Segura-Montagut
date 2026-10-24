import csv

# Llegim els productes i guardem el seu preu associat a l'ID
products = {}

with open("products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products[row["id"]] = float(row["cost"])


# Llegim els clients i inicialitzem la seva despesa a zero
customers = {}

with open("customers.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customers[row["id"]] = {
            "firstname": row["firstname"],
            "lastname": row["lastname"],
            "total_euros": 0.0
        }


# Calculem el total de cada comanda i l'acumulem al client
with open("orders.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer_id = row["customer"]
        product_ids = row["products"].split()

        total = sum(products[product_id] for product_id in product_ids) # Mateix càlcul que a la Tasca 1

        customers[customer_id]["total_euros"] += total


# Ordenem els clients per despesa, de major a menor
ranking = sorted(
    customers.items(),
    key=lambda item: item[1]["total_euros"],
    reverse=True
)


# Finalment, generem el fitxer customer_ranking.csv
with open("customer_ranking.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["id", "firstname", "lastname", "total_euros"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for customer_id, data in ranking:
        writer.writerow({
            "id": customer_id,
            "firstname": data["firstname"],
            "lastname": data["lastname"],
            "total_euros": data["total_euros"]
        })
