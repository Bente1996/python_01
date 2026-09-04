#!/usr/bin/env python3

from sys import stderr

class Plant:
    def __init__(
        self, name: str, height: float, age: int, plant_type: str,
        grow_rate: float = 0.0,
    ) -> None:
        self._name = name
        self._height = 0
        self.set_height(height)
        self._age = 0
        self.set_age(age)
        self._grow_rate = grow_rate
        self._plant_type = plant_type
        self._statistics_manager = self.Statistical_data(self._plant_type)

    def grow(self) -> float:
        self._statistics_manager.increment_grow()
        self._height += self._grow_rate
        return round(self._height, 3)

    def age(self) -> None:
        self._statistics_manager.increment_age()
        self._age += 1

    def show(self) -> None:
        self._statistics_manager.increment_show()
        print(self)

    def __repr__(self) -> str:
        return (
            f"{self._name}: {round(self._height, 3)}cm tall, "
            f"{self._age} days old"
        )

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height} cm")
        else:
            print(
                f"{self._name}: Error, height can't be negative", file=stderr
            )
            print("Height update rejected", file=stderr)

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative", file=stderr)
            print("Age update rejected", file=stderr)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def age_checker(days :int) -> str:
        if days > 365:
            return f"Is {days} days more than a year? -> True"
        else:
            return f"Is {days} days more than a year? -> False"

#    def create_anonymous_plant() -> None:
#
    class Statistical_data:
        def __init__(self, plant_type: str) -> None:
            self._age = 0
            self._grow = 0
            self._show = 0
            self._plant_type = plant_type

        def increment_grow(self) -> None:
            self._grow += 1

        def increment_age(self) -> None:
            self._age += 1

        def increment_show(self) -> None:
            self._show += 1

        def show_data(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")
            if self._plant_type == "Tree":
                print(produce_shade()) ## hier gebleven




#class Seed(Flower):


class Flower(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        colour: str,
        plant_type: str = "Flower",
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, plant_type, grow_rate=grow_rate)
        self._colour = colour
        self._in_bloom = False

    def __repr__(self) -> str:
        blooming = "is blooming beautifully"
        not_blooming = "has not bloomed yet"
        return (
            f"{super().__repr__()}\n"
            f"Colour: a beautiful {self._colour} colour\n"
            f"{self._name} {blooming if self._in_bloom else not_blooming}"
        )

    def get_colour(self) -> str:
        return self._colour

    def bloom(self) -> None:
        self._in_bloom = True

    class Statistical_data(Plant.Statistical_data):
        def show_data(self) -> None:
            print("im a flower")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        trunk_diameter: float,
        plant_type: str = "Tree",
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, plant_type, grow_rate=grow_rate)
        self._trunk_diameter = trunk_diameter

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self._trunk_diameter}cm thick"

    def produce_shade(self) -> None:
        print(
            f"{self._name} tree now produces shade of {self._height}"
            f"cm long and {self._trunk_diameter}cm wide"
        )

    class Statistical_data(Plant.Statistical_data):
        def show_data(self) -> None:
            print("im a flower")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        harvest_season: int | str,
        plant_type: str = "Vegetable",
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, plant_type, grow_rate=grow_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}\nHarvest season: {self._harvest_season}"
            f"\nNutritional value: {self._nutritional_value}"
        )

    def ripen(self) -> None:
        super().grow()
        super().age()
        self._nutritional_value += 1


if __name__ == "__main__":
    rose = Flower("Rose", 10, 15, "red", 0.3)
    walnut = Tree("Walnut", 40000, 70, 80)
    plant = Plant("Plant", 0, 0, "")
    statistical_data = plant.Statistical_data("")

    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print(Plant.age_checker(30))
    print(Plant.age_checker(400))

    print("=== Flower")
    statistical_data.show_data()
    rose.show()
    print("[statistics for Rose]")
    rose._statistics_manager.show_data()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose._statistics_manager.show_data()

    print("=== Tree")
    walnut.show()
    print("[statistics for walnut tree]")
    walnut._statistics_manager.show_data()
