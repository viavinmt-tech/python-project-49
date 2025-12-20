def dec(funk):
    def wrapper():
        print('Begin')
        funk()
        print('end...')
    return wrapper
@dec
def hi():
    print('Hi!')

hi()

