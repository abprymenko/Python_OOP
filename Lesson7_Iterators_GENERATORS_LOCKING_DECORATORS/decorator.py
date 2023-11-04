class Checker:
    def Check(self, *exc_type):
        def Check(function):
            def Check(*args, **kwargs):
                try:
                    print(function(*args, **kwargs))
                except (exc_type) as ex:
                    raise ex
                else:
                    print("No exception")
            return Check
        return Check
    @Check(NameError, TypeError, SyntaxError, ZeroDivisionError, Exception)
    def Calculate(self, expresion):
        return eval(expresion)