class Parser:
    @staticmethod
    def IntTryParse(value:str):
        if isinstance(value, int):
            return int(value)
        return None

    @staticmethod
    def FloatTryParse(value:str):
        if isinstance(value, float):
            return float(value)
        return None
        