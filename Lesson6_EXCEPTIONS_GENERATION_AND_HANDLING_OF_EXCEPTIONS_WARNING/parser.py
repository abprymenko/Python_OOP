from visitor import Parser

class Parser:
    @staticmethod
    def ParseDigit(amount: str):
        while True:
            try:
                return DigitVisitor.IntTryParse(amount)
            except ValueError:
                try:
                    return DigitVisitor.FloatTryParse(amount)
                except ValueError:
                    amount = input("Enter amount as digit: ")
            except Exception as ex:
                raise ex