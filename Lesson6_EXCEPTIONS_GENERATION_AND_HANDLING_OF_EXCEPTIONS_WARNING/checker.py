from types import NoneType
from builderror import BuildError


class Checker:
    @staticmethod
    def Check(amount:int, limit:int):
        if isinstance(amount, NoneType):
           raise TypeError("Please enter a numeric value for amount.\nUse please dot symbol such as '.' for typing the float value.")
        if not amount > 0:
            raise ValueError(f'Amount must be greater than 0.\nYour entered amount = {amount}.')
        if amount > limit:
            raise BuildError(amount, limit)
        return True