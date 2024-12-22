from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# Para python mayor o igual a la version 3.11
# from typing import Self
# Para python menor a la version 3.11
from typing_extensions import Self


@dataclass
class CoffeeRequest:
    coffee_type: str
    coffee: bool = False
    milk: bool = False
    chocolate: bool = False
    cinnamon: bool = False
    ingredients: list = field(default_factory=list)
    sweetener: str = None


class CoffeeHandler(ABC):
    @abstractmethod
    def set_next(self, handler: Self) -> Self: ...

    @abstractmethod
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest: ...


class CoffeeHandlerBase(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: Self) -> Self:
        self._next_handler = handler
        return handler

    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if self._next_handler:
            return self._next_handler.handle(coffee_request)
        return coffee_request


class Coffee(CoffeeHandlerBase):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.coffee:
            coffee_request.ingredients.append("Cafe")
            print("Agregando cafe...")

        return super().handle(coffee_request)


class Milk(CoffeeHandlerBase):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.milk:
            coffee_request.ingredients.append("Leche")
            print("Agregando leche...")

        return super().handle(coffee_request)


class Chocolate(CoffeeHandlerBase):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.chocolate:
            coffee_request.ingredients.append("Chocolate")
            print("Agregando chocolate...")

        return super().handle(coffee_request)


class Cinnamon(CoffeeHandlerBase):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.cinnamon:
            coffee_request.ingredients.append("Canela")
            print("Agregando Canela...")

        return super().handle(coffee_request)


# Estrategia para realizar el agitado del cafe.
class StirringStrategy(ABC):
    @abstractmethod
    def stir(self):
        pass


class NormalStir(StirringStrategy):
    def stir(self):
        print("Batido normal...")


class ThoroughStir(StirringStrategy):
    def stir(self):
        print("Batido fuerte...")


class NoStir(StirringStrategy):
    def stir(self):
        print("No es necesario un batido...")


class StirringStrategyFactory:
    @staticmethod
    def create_strategy(sweetener_type):
        if sweetener_type == "Azucar normal":
            return NormalStir()
        elif sweetener_type == "Azucar rubia":
            return ThoroughStir()
        elif sweetener_type == "Stevia":
            return NoStir()
        else:
            return NoStir()


class Sweetener(CoffeeHandlerBase):
    def handle(self, coffee_request: CoffeeRequest) -> CoffeeRequest:
        if coffee_request.sweetener:
            coffee_request.ingredients.append(coffee_request.sweetener)
            print(f"Endulzando con {coffee_request.sweetener}...")

            stirring_strategy = StirringStrategyFactory.create_strategy(
                coffee_request.sweetener
            )
            stirring_strategy.stir()

        return super().handle(coffee_request)


class CoffeeFactory:
    @staticmethod
    def create_coffee(coffee_type, sweetener_requests):
        if coffee_type == "Mocha":
            return CoffeeRequest(
                coffee_type,
                coffee=True,
                milk=True,
                chocolate=True,
                sweetener=sweetener_requests,
            )
        elif coffee_type == "Cafe simple":
            return CoffeeRequest(coffee_type, coffee=True, sweetener=sweetener_requests)
        elif coffee_type == "Cafe con canela":
            return CoffeeRequest(
                coffee_type,
                coffee=True,
                milk=True,
                cinnamon=True,
                sweetener=sweetener_requests,
            )
        elif coffee_type == "Cafe con leche":
            return CoffeeRequest(
                coffee_type, coffee=True, milk=True, sweetener=sweetener_requests
            )
        elif coffee_type == "Leche sola":
            return CoffeeRequest(coffee_type, milk=True, sweetener=sweetener_requests)
        else:
            raise TypeError(f"Se ingreso un tipo de cafe no valido: {coffee_type}")


def make_coffee(coffee_requests, sweetener_requests):
    request_caffee = CoffeeFactory.create_coffee(coffee_requests, sweetener_requests)

    coffee_handler = Coffee()
    milk_handler = Milk()
    chocolate_handler = Chocolate()
    cinnamon_handler = Cinnamon()
    sweetener_handler = Sweetener()

    coffee_handler.set_next(milk_handler).set_next(chocolate_handler).set_next(
        cinnamon_handler
    ).set_next(sweetener_handler)

    request_caffee = coffee_handler.handle(request_caffee)

    return request_caffee.ingredients


if __name__ == "__main__":
    requests = [
        {"coffee_type": "Cafe simple", "sweetener": "Azucar normal"},
        {"coffee_type": "Cafe simple"},
        {"coffee_type": "Cafe con leche"},
        {"coffee_type": "Mocha", "sweetener": "Azucar normal"},
        {"coffee_type": "Leche sola", "sweetener": "Stevia"},
        {"coffee_type": "Cafe con canela", "sweetener": "Azucar rubia"},
        {"coffee_type": "Cafe con canela y chocolate", "sweetener": "Azucar normal"},
    ]

    for request in requests:
        print("Llega un cliente....")
        coffee_type = request.get("coffee_type")
        sweetener = request.get("sweetener")
        try:
            result = make_coffee(coffee_type, sweetener)
            print(f"lo que se entrega al cliente es: {result}")
        except TypeError:
            print(f"Perdon cliente, pero no tenemos de {coffee_type}, vuelva pronto.")
        print("El cliente se va.")
