from types import NoneType

class Parser:
    @staticmethod
    def NumericTryParse(amount: str):
        try:
            value = amount.strip()
            if (value.isdigit()
                    or (ord(value[0]) == ord('-') and value[1:].isdigit())):
                return int(value)
            elif '.' in value:
                return float(value)
            return None
        except ValueError as ve:
            return None