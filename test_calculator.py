from datetime import datetime
from calculator import ParkingFeeCalculator


PFC = ParkingFeeCalculator()


class TestParkingFeeCalculator:

    def test_15_mins_free(self):
        start = datetime(2024, 1, 1, 0, 0, 0)
        end = datetime(2024, 1, 1, 0, 14, 59)

        actual = PFC.calculate(start, end)

        assert actual == 0

    def test_over_15min_NOT_free(self):
        start = datetime(2024, 1, 1, 0, 0, 0)
        end = datetime(2024, 1, 1, 0, 15, 1)

        actual = PFC.calculate(start, end)

        assert actual != 0

    def test_over_30min__R__pay_60(self):
        start = datetime(2024, 1, 1, 0, 0, 0)
        end = datetime(2024, 1, 1, 0, 30, 1)

        actual = PFC.calculate(start, end)

        assert actual == 60

    def test_over_60min__R__pay_90(self):
        start = datetime(2024, 1, 1, 0, 0, 0)
        end = datetime(2024, 1, 1, 1, 0, 1)

        actual = PFC.calculate(start, end)

        assert actual == 90

    def test_over_150min__R__pay_150(self):
        pass
