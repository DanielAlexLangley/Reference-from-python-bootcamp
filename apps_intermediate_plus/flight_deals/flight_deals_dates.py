
import datetime


class Dates:
    # This class is responsible for determining the dates for tomorrow and six months from now.

    def __init__(self):
        self.today = datetime.datetime.today()

    def get_tomorrow(self):
        tomorrow = self.today + datetime.timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime(f"%d" + "/" + "%m" + "/" + "%Y")
        return tomorrow_formatted

    def get_six_months(self):
        six_months = self.today + datetime.timedelta(days=183)
        six_months_formatted = six_months.strftime(f"%d" + "/" + "%m" + "/" + "%Y")
        return six_months_formatted
