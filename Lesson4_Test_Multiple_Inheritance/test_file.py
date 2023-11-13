try:
    from Lesson4_Multiple_Inheritance import ColorBox
    color_box = ColorBox(10, 20, 'red')
    print(color_box)
except ImportError as ie:
    print(ie)