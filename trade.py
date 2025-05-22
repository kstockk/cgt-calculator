import datetime

class Trade:
    def __init__(self, date, type, ticker, qty, price, brokerage, gst, is_drp=False) -> None:
        day, month, year = [int(x) for x in date.split("/")]
        self.date = datetime.date(year=year, month=month, day=day)
        self.type = type.upper()
        self.ticker = ticker.strip().upper()
        self.qty = int(qty)
        self.unit_price = self.clean_money(price)
        self.brokerage = self.clean_money(brokerage) + self.clean_money(gst)
        self.price = self.unit_price * self.qty + self.brokerage
        self.is_drp = is_drp == "Y"

    def clean_money(self, n):
        return float(n.replace("$", "").replace("AU", ""))

    def __str__(self):
        return f'{self.date}: {self.type} {self.ticker} {self.qty} at ${self.unit_price} with ${self.brokerage} brokerage for ${self.price}'
