class DigitVisitor:
    @staticmethod
    def IntTryParse(value:str):
        try:
            if isinstance(value, int):
                return int(value)
            return None
        except ValueError as ve:
            raise ve
    @staticmethod
    def FloatTryParse(value:str):
        try:
            if isinstance(value, float):
                return float(value)
            return None
        except ValueError as ve:
            raise ve