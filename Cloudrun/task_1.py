import typing


class Date4Test:
    _days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _days_from_year_begin_months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    # for i in range(0, 12):
    #     days_from_year_to_this_month = 0
    #     for j in range(0, i):
    #         days_from_year_to_this_month += _days_in_months[j]
    #     _days_from_year_begin_months[i] = days_from_year_to_this_month

    def __init__(self, year: int, month: int, day: int) -> None:
        super().__init__()
        if year < 0:
            raise ValueError("BC not supported")
        if month < 1 or month > 12:
            raise ValueError(f"incorrect month {month}. Expected from 1 to 12")
        max_day_expected = (
            self._days_in_months[month - 1] + 1 if month == 2 else self._days_in_months[month - 1]
        )
        if day < 1 or day > max_day_expected:
            raise ValueError(
                f"incorrect day {day}. Expected from 1 to {max_day_expected} for month {month} year {year}"
            )
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self) -> bool:
        """
        Is year leap or not. Leap year is:
        * year divided to 4
        ** except years divided to 100
        *** except years divided to 400
        :return: True if leap year
        """
        if self.year % 4 != 0:
            return False
        if self.year % 100 != 0:
            return True
        if self.year % 400 != 0:
            return False
        return True

    @staticmethod
    def _leaps_anno_domini(year: int):
        return year // 4 - year // 100 + year // 400

    def _days_anno_domini(self) -> int:
        days_by_round_year = self.year * 365
        days_by_leap_years = self._leaps_anno_domini(self.year - 1)
        days_from_year_begin = self._days_from_year_begin_months[self.month - 1]
        day_if_leap_year = 1 if self.is_leap_year() and self.month > 2 else 0
        return (
            days_by_round_year
            + days_by_leap_years
            + days_from_year_begin
            + day_if_leap_year
            + self.day
        )

    @staticmethod
    def days_differ(start: "Date4Test", finish: "Date4Test") -> int:
        """
        Days between two dates
        """
        return finish._days_anno_domini() - start._days_anno_domini()


def test_is_leap():
    # as base
    assert Date4Test(2020, 1, 1).is_leap_year()
    assert not Date4Test(2021, 1, 1).is_leap_year()
    assert not Date4Test(2022, 1, 1).is_leap_year()

    assert not Date4Test(0, 1, 1).is_leap_year()
    assert Date4Test(4, 1, 1).is_leap_year()
    assert not Date4Test(0, 1, 1).is_leap_year()
    assert not Date4Test('0', 1, 1).is_leap_year()
    assert not Date4Test(2020, 2, 30).is_leap_year()


def test_days_differ():
    # # as base
    assert Date4Test.days_differ(Date4Test(2022, 6, 29), Date4Test(2022, 6, 30)) == 1
    assert Date4Test.days_differ(Date4Test(2022, 1, 1), Date4Test(2022, 1, 31)) == 30
    assert Date4Test.days_differ(Date4Test(2022, 1, 1), Date4Test(2022, 2, 1)) == 31

    assert Date4Test.days_differ(Date4Test(2020, 2, 1), Date4Test(2020, 3, 1)) == 29
    assert Date4Test.days_differ(Date4Test(2022, 1, 1), Date4Test(2022, 1, 1)) == 0
    assert Date4Test.days_differ(Date4Test(2023, 1, 1), Date4Test(2022, 1, 1))
    assert Date4Test.days_differ(Date4Test(2019, 12, 31), Date4Test(2020, 2, 29)) == 60
    assert Date4Test.days_differ(Date4Test(0, 1, 1), Date4Test(0, 2, 1)) == 31
    assert Date4Test.days_differ(Date4Test(0, 0, 0), Date4Test(0, 0, 0))
    assert Date4Test.days_differ(Date4Test(2022, 1, 32), Date4Test(2022, 2, 30))
