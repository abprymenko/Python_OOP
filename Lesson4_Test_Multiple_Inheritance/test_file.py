try:
    from Lesson4_Multiple_Inheritance import ColorBox
    from colorama import Fore, Style
    redbox = ColorBox(10, 20, 'red', Fore.RED)
    bluebox = ColorBox(11, 21, 'blue', Fore.BLUE)
    yellowbox = ColorBox(12, 22, 'yellow', Fore.YELLOW)
    greenbox = ColorBox(13, 23, 'green', Fore.GREEN)
    magentabox = ColorBox(17, 27, 'magenta', '\033[0;35m')
    underlinebox = ColorBox(15, 25, 'underline', '\033[0;4m')
    invertedbox = ColorBox(16, 26, 'inverted', '\033[0;7m')
    print(f'{redbox.ColorAnsi}{redbox}')
    print(f'{bluebox.ColorAnsi}{bluebox}')
    print(f'{yellowbox.ColorAnsi}{yellowbox}')
    print(f'{greenbox.ColorAnsi}{greenbox}')
    print(magentabox.ColorAnsi + str(magentabox))
    print(f'{underlinebox.ColorAnsi}{underlinebox}')
    print(f'{invertedbox.ColorAnsi}{invertedbox}')
    print(f'{Style.RESET_ALL}No styles')
except ImportError as ie:
    print(ie)