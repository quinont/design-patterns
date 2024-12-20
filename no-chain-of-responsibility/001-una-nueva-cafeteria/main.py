

def make_coffee(coffee_requests):
    if coffee_requests != "Cafe simple":
        raise TypeError("Se ingreso un tipo de cafe no valido.")

    print("Agregando cafe...")
    return ["cafe"]


if __name__ == "__main__":
    requests = ["Cafe simple", "Cafe simple", "cafe con leche"]

    for request in requests:
        print("Llega un cliente....")
        try:
            result = make_coffee(request)
            print(f"lo que se entrega al cliente es: {result}")
        except TypeError:
            print(f"Perdon cliente, pero no tenemos de {request}, vuelva pronto.")
        print("El cliente se va.")

