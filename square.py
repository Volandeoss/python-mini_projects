class AreaSquare:
    def __init__(self, side: int) -> None:
        self.side: int = side 

    def get_value(self) -> int:
        self.value: int = self.side**2
        return self.value

if __name__ == "__main__":
    SIDE_SQUARE: int = 5
    area_square: AreaSquare = AreaSquare(SIDE_SQUARE)
    value_area_square: int = area_square.get_value()
    print(f"{value_area_square}")

  
