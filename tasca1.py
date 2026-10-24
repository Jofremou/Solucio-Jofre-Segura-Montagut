
import csv

# Llegim els productes i guardem el seu preu associat a l'ID
products = {}

with open("products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products[row["id"]] = float(row["cost"])


# Llegim les comandes i calculem el cost total de cadascuna
with open("orders.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Creem l'arxiu order_prices.csv si no existeix
    with open("order_prices.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=["id", "euros"])
        writer.writeheader()

        # Per cada fila, separa els numeros amb split, els busca a products.csv i escriu el total a order_prices.csv
        for row in reader:
            product_ids = row["products"].split()

            total = sum(products[product_id] for product_id in product_ids)

            writer.writerow({
                "id": row["id"],
                "euros": total
            })
