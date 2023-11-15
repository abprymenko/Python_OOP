class DigitVisitor:
    @staticmethod
    def IntTryParse(value:str):
        try:
            return int(value)
        except ValueError as ve:
            raise ve
    @staticmethod
    def FloatTryParse(value:str):
        try:
            return float(value)
        except ValueError as ve:
            raise ve