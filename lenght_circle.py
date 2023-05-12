import math
k=10.90789
class AreaCircle:
    def __init__(self, radius: int) -> None:
        self.radius: int = radius
    def get_value(self) -> float:
        self.value: float = math.pi * self.radius**2
        return self.value
if __name__ == "__main__":
    RADIUS_CIRCLE: int = 5
    area_circle: AreaCircle = AreaCircle(RADIUS_CIRCLE)
    value_area_circle: float = area_circle.get_value()
    print(f"{value_area_circle:0.2f}\t{k:0.2f}")


