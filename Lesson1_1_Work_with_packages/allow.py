class Allow:
    def AllowedFunction(self):
        print("This function is allowed for import.")

if __name__ == "__main__":
    print('When you run a program, Python sets the __name__ variable for the main module (main script) to the string "main".\n'
          'If this script is imported into another file, the __name__ for that file will be different\n'
          ' - it will be the name of the file or module itself.\n'
          'So, when we use the condition if __name__ == "__main__":,\n'
          'we are checking whether this script is being run directly (not imported).\n'
          ' This allows us to execute specific code only when the file is run, not when it is imported into another file.\n'
          'The lines written within the conditional statement will not be executed when your module is imported into another file.\n')