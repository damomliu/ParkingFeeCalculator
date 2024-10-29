from datetime import datetime
from dateutil.parser import parse
from calculator import ParkingFeeCalculator


class TestParkingFeeCalculator:
    pfc: ParkingFeeCalculator
    start_time: datetime
    end_time: datetime
    actual_fee: int

    def setup_method(self):
        self.pfc = ParkingFeeCalculator()

    def given_parking_start_at(self, start: str):
        self.start_time = parse(start)

    def given_parking_end_at(self, end: str):
        self.end_time = parse(end)

    def calculate(self):
        self.actual_fee = self.pfc.calculate(self.start_time, self.end_time)

    def should_pay(self, expected: int):
        assert self.actual_fee == expected

    def test_15_mins_free(self):
        self.given_parking_start_at("2024-1-2T0:0:0")
        self.given_parking_end_at("2024-1-2T0:15:00")
        self.calculate()
        self.should_pay(0)

    def test_over_15min_NOT_free(self):
        self.given_parking_start_at("2024-1-2T0:0:0")
        self.given_parking_end_at("2024-1-2T0:15:01")
        self.calculate()
        assert self.actual_fee > 0

    def test_within_30min__R__pay_30(self):
        self.given_parking_start_at("2024-1-2T0:0:0")
        self.given_parking_end_at("2024-1-2T0:30:00")
        self.calculate()
        self.should_pay(30)

    def test_over_30min__R__pay_60(self):
        self.given_parking_start_at("2024-1-2T0:0:0")
        self.given_parking_end_at("2024-1-2T0:30:01")
        self.calculate()
        self.should_pay(60)

    def test_over_60min__R__pay_90(self):
        self.given_parking_start_at("2024-1-2T0:0:0")
        self.given_parking_end_at("2024-1-2T01:00:01")
        self.calculate()
        self.should_pay(90)

    def test_over_150min__R__pay_150(self):
        self.given_parking_start_at("2024-1-2T0:0:0")
        self.given_parking_end_at("2024-1-2T02:30:01")
        self.calculate()
        self.should_pay(150)
