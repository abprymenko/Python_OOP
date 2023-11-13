class Restrict:
    def RestrictedFunction(self):
        return "This function is restricted for import."

if __name__ == "__main__":
    restrict = Restrict()
    print(restrict.RestrictedFunction())