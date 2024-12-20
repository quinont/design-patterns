def make_coffee(coffee_requests):
    if coffee_requests not in (
        "Cafe simple",
        "Cafe con leche",
        "Mocha",
        "Leche sola",
        "Cafe con canela",
    ):
        raise TypeError("Se ingreso un tipo de cafe no valido.")

    result = []
    if coffee_requests in ("Cafe simple", "Cafe con leche", "Mocha", "Cafe con canela"):
        print("Agregando cafe...")
        result.append("cafe")

    if coffee_requests in ("Cafe con leche", "Mocha", "Cafe con canela", "Leche sola"):
        print("Agregando leche...")
        result.append("leche")

    if coffee_requests in ("Mocha"):
        print("Agregando chocolate...")
        result.append("chocolate")

    if coffee_requests in ("Cafe con canela"):
        print("Agregando canela...")
        result.append("canela")

    return result


if __name__ == "__main__":
    requests = [
        "Cafe simple",
        "Cafe simple",
        "Cafe con leche",
        "Mocha",
        "Leche sola",
        "Cafe con canela",
        "Cafe con canela y chocolate",
    ]

    for request in requests:
        print("Llega un cliente....")
        try:
            result = make_coffee(request)
            print(f"lo que se entrega al cliente es: {result}")
        except TypeError:
            print(f"Perdon cliente, pero no tenemos de {request}, vuelva pronto.")
        print("El cliente se va.")
