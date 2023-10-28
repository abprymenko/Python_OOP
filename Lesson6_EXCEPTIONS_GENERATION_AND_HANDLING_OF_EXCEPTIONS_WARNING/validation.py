from builterror import BuildError
class Validator:
    def Check(self, amount:int, limit:int):
        if(amount > limit):
            raise BuildError(amount, limit)
        return True