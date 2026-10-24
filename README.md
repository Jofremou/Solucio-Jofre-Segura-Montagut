# Descripció

Aquest repositori conté una solució per a la prova tècnica online per entrar a l'equip tècnic de sistemes de l'ICGC. Aquest README explica com funcionen les solucions i com executar-les.

## Estructura del projecte

- `customers.csv`: informació dels clients.
- `products.csv`: informació dels productes i els seus preus.
- `orders.csv`: informació de les comandes i els productes que contenen.
- `tasca1.py`: genera `order_prices.csv`.
- `tasca2.py`: genera `product_customers.csv`.
- `tasca3.py`: genera `customer_ranking.csv`.

## Requisits

- Python 3.
- No cal instal·lar llibreries externes, ja que les solucions utilitzen el mòdul `csv` de la biblioteca estàndard de Python.

Els scripts s'han d'executar des del directori que conté els fitxers Python i els CSV d'entrada.

## Tasca 1

L'objectiu d'aquesta tasca és calcular el cost total de cada ordre i guardar el resultat a `order_prices.csv`. 

La solució consisteix en llegir els ids al camp `products` de `orders.csv`, buscar el preu corresponent als ids a `products.csv` i escriure el resultat al nou csv. 

El codi es pot executar encara que s'hi afegeixin nous productes a posteriori, i aquest calcularà els preus un altre cop des de zero, evitant preus incorrectes si el codi s'executa múltiples vegades.

Per executar-ho, hi ha prou amb tenir python 3 al sistema, i executar la següent comanda:

```bash
python tasca1.py
```

## Tasca 2

L'objectiu d'aquesta tasca és calcular quins clients han comprat quins productes, i guardar el resultat a `product_customers.csv`. 

La solució consisteix en llegir les ordres associades a cada client a `orders.csv`, afegirles a un diccionari inicialitzat per evitar duplicars i escriure el resultat al nou csv. Aquest codi també es pot executar de nou encara que s'actualitzi la base de dades degut a que aquest evita que noves comandes afegeixin duplicats.

Per executar-ho, hi ha prou amb tenir python 3 al sistema, i executar la següent comanda:

```bash
python tasca2.py
```

## Tasca 3

L'objectiu d'aquesta tasca és crear un csv que ordeni de forma descendent pel camp `total_euros`, per saber quins clients gasten més en productes. 

La solució consisteix en llegir els ids al camp `products` de `orders.csv`, buscar el preu corresponent als ids a `products.csv`, calcular la despesa de la comanda en questió i guardar-la al total de despesa d'aquell client. Finalment, després d'ordenar el resultat obtingut, generem l'arxiu `customer_ranking.csv`.

He decidit no utilitzar l'arxiu `order_prices.csv` per a evitar l'actualització forçada d'aquest per a generar `customer_ranking.csv`, tot i que seria perfectament possible generar un codi que generés ambdós arxius aprofitant els càlculs.

Per executar-ho, hi ha prou amb tenir python 3 al sistema, i executar la següent comanda:

```bash
python tasca3.py
```

