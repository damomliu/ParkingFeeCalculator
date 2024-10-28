from datetime import datetime, timedelta


class ParkingFeeCalculator:
    """
        Topic: 如何製作一個「能上新聞的」停車費計算機
        https://youtube.com/playlist?list=PLvBh-90IwbPKFUUFw1PTezAVQqi0PUhTB&si=m_3gL1MK9nxfad6g

        停車場
        15分鐘內免費
        平日
            每小時 60 元 (以半小時計)
            當日上限 150 元 (隔日另計)
        例假日與國定假日
            每小時 100 元 (以半小時計)
            當日上限 2400 元 (隔日另計)
    """
    def calculate(self, start: datetime, end: datetime):
        delta = end - start

        if delta <= timedelta(minutes=15):
            return 0

        else:
            fee = self._get_regular_fee(delta)
            return min(fee, 150)

    def _get_regular_fee(self, delta):
        periods = int(delta / timedelta(minutes=30))
        fee = (periods + 1) * 30
        return fee
