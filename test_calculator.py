from datetime import datetime
from calculator import ParkingFeeCalculator


PFC = ParkingFeeCalculator()


class TestParkingFeeCalculator:

    def test_15_mins_free(self):
        start = datetime(2024, 1, 1, 0, 0, 0)
        end = datetime(2024, 1, 1, 0, 14, 59)

        actual = PFC.calculate(start, end)

        assert actual == 0
