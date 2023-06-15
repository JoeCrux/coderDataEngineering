import finnhub

# conexion API
finnhub_client = finnhub.Client(api_key="bqoji3nrh5rced4gaukg")

# datos API
lista = finnhub_client.company_earnings('TSLA', limit=5)
for e in lista:
    for x, y in e.items():
        print(x, y)