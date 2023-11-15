class Calculator(object):
    def __Check(self, *exc_type):
        '''
        Callback Functions: Closures are commonly used in event handling and callback scenarios,
        allowing functions to carry additional context.
        :param exc_type:
        :return: Check(function)
        '''
        def Check(function):
            '''
            :param function: For example, use :meth:`~Calculator.Calculate`
            :return: Check(*args, **kwargs)
            '''
            def Check(*args, **kwargs):
                '''
                :param args: tuple (value:Any, ..., ...)
                :param kwargs: dict {"key:str":"value:Any"}
                :return: function result
                '''
                try:
                    return function(*args, **kwargs)
                except (exc_type) as ex:
                    raise ex
            return Check
        return Check

    @__Check(NameError, TypeError, SyntaxError, ZeroDivisionError, Exception)
    def Calculate(self, expresion):
        return eval(expresion)