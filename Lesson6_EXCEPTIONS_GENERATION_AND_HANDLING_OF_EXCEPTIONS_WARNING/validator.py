from builderror import BuildError
class Validator:
    @staticmethod
    def Check(amount:int, limit:int):
        if(not amount > 0):
            raise ValueError(f'Amount must be greater than 0. Amount = {amount}')
        if(amount > limit):
            raise BuildError(amount, limit)
        return True