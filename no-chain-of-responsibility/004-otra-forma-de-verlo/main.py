from abc import ABC, abstractmethod

# Para python mayor o igual a la version 3.11
# from typing import Self
# Para python menor a la version 3.11
from typing_extensions import Self


class CoffeeRequest:
    def __init__(
        self, coffee_type, coffee=False, milk=False, chocolate=False, cinnamon=False
    ):
        self.type = coffee_type
        self.ingredients = []
        self.coffee = coffee
        self.milk = milk
        self.chocolate = chocolate
        self.cinnamon = cinnamon


class CoffeeHandler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: Self) -> Self:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        pass


class Coffee(CoffeeHandler):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.coffee:
            coffee_request.ingredients.append("Cafe")
            print("Agregando cafe...")

        if self._next_handler:
            self._next_handler.handle(coffee_request)


class Milk(CoffeeHandler):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.milk:
            coffee_request.ingredients.append("Leche")
            print("Agregando leche...")

        if self._next_handler:
            self._next_handler.handle(coffee_request)


class Chocolate(CoffeeHandler):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.chocolate:
            coffee_request.ingredients.append("Chocolate")
            print("Agregando chocolate...")

        if self._next_handler:
            self._next_handler.handle(coffee_request)


class Cinnamon(CoffeeHandler):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.cinnamon:
            coffee_request.ingredients.append("Canela")
            print("Agregando Canela...")

        if self._next_handler:
            self._next_handler.handle(coffee_request)


class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type):
        if coffee_type == "Mocha":
            return CoffeeRequest(coffee_type, coffee=True, milk=True, chocolate=True)
        elif coffee_type == "Cafe simple":
            return CoffeeRequest(coffee_type, coffee=True)
        elif coffee_type == "Cafe con canela":
            return CoffeeRequest(coffee_type, coffee=True, milk=True, cinnamon=True)
        elif coffee_type == "Cafe con leche":
            return CoffeeRequest(coffee_type, coffee=True, milk=True)
        elif coffee_type == "Leche sola":
            return CoffeeRequest(coffee_type, milk=True)
        else:
            raise TypeError(f"Se ingreso un tipo de cafe no valido: {coffee_type}")


def make_coffee(coffee_requests):
    request_caffee = CoffeeFactory.create_coffee(coffee_requests)

    coffee_handler = Coffee()
    milk_handler = Milk()
    chocolate_handler = Chocolate()
    cinnamon_handler = Cinnamon()

    coffee_handler.set_next(milk_handler).set_next(chocolate_handler).set_next(
        cinnamon_handler
    )

    coffee_handler.handle(request_caffee)

    return request_caffee.ingredients


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
