from datetime import datetime
from calculator import ParkingFeeCalculator


def test_15_mins_free():
    c = ParkingFeeCalculator()

    start = datetime(2024, 1, 1, 0, 0, 0)
    end = datetime(2024, 1, 1, 0, 14, 59)

    actual = c.calculate(start, end)

    assert actual == 0
