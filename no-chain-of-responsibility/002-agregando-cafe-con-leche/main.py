

def make_coffee(coffee_requests):
    if coffee_requests not in ("Cafe simple", "Cafe con leche"):
        raise TypeError("Se ingreso un tipo de cafe no valido.")

    result = []
    if coffee_requests in ("Cafe simple", "Cafe con leche"):
        print("Agregando cafe...")
        result.append("cafe")

    if coffee_requests == "Cafe con leche":
        print("Agregando leche...")
        result.append("leche")

    return result


if __name__ == "__main__":
    requests = ["Cafe simple", "Cafe simple", "Cafe con leche", "Mocha", "Leche simple"]

    for request in requests:
        print("Llega un cliente....")
        try:
            result = make_coffee(request)
            print(f"lo que se entrega al cliente es: {result}")
        except TypeError:
            print(f"Perdon cliente, pero no tenemos de {request}, vuelva pronto.")
        print("El cliente se va.")

