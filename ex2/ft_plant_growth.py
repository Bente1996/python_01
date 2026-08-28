#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            age: int,
            height: float,
            grow_rate: float = 0.3
        ) -> None:
        self.__name = name
        self.__age = age
        self.__height = height
        self.__grow_rate = grow_rate

    def grow(self) -> None:
        self.__height += self.__grow_rate

    def age(self) -> None:
        self.__age += 1

    def show(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return(
                f"{self.__name}: {self.__age} days old, "
                f"{round(self.__height, 3)}cm tall"
        )

def show_grow_age(plant: Plant) -> None:
    plant.show()
    plant.grow()
    plant.age()

def ft_plant_growth(name: str, age: int, height: float) -> None:
    plant_object = Plant(name, age, height)
    plant_object_2 = Plant(name + "_2", age, height, grow_rate = 0.2)
    for day in range(8):
        print(f"=== Day {day} ===")
        show_grow_age(plant_object)
        for element in [plant_object, plant_object_2]:
            element.show()
            element.grow()
            element.age()
        # plant_object.show()
        # plant_object_2.show()
        # plant_object_2.grow()
        # plant_object_2.age()
        # plant_object.grow()
        # plant_object.age()

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth("Rose", 30, 25.5)
