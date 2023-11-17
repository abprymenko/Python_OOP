class CalcManager:
    @staticmethod
    def Add(a: int, b: int) -> int:
        """
        The function adds two numbers together.
        :param a: First digit
        :param b: Second digit
        :return: The result of adding a and b
        For running this test right click on the name of method
        and select Run 'Doctest Add' or Ctrl + Shift + 10
        Examples for doctest:
        >>> CalcManager.Add(2, 2)
        4
        >>> CalcManager.Add(2, 2)
        5
        >>> CalcManager.Add(2, 2)
        3
        """
        return a + b
    @staticmethod
    def AddArgsKWArgs(*args, **kwargs) -> int:
        """
        The function that adds all parameter values.
        :param args:
        :param kwargs:
        :return: The result of adding all parameter values.
        """
        result : int = 0
        for _ in args:
            result += _
        for _ in kwargs.values():
            result += _
        return result

    @staticmethod
    def Div(a:int, b:int) -> float:
        """
        The function of dividing the number a by the number b.
        :param a: First digit.
        :param b: Second digit.
        :return: The result of division a and b.
        """
        try:
            return a / b
        except:
            raise

if __name__ == "__main__":
    import doctest
    #True - if you want to get more information about testing. By default False.
    doctest.testmod(verbose=True)
