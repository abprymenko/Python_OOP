from visitor import Parser

class Validator:
    @staticmethod
    def CheckDigit(amount: str):
        while True:
            try:
                value = Parser.IntTryParse(amount)
                if isinstance(value, None):
                    value = Parser.FloatTryParse(amount)
            except Exception as ex:
                raise ex
            finally:
                if isinstance(value, None):
                    amount = input("Enter amount as integer: ")
                else:
                    return value