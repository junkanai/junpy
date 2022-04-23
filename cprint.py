def cprint(string, color):
    print(color(string))

def black(string):
    return '\033[30m' + string + '\033[0m'

def red(string):
    return '\033[31m' + string + '\033[0m'

def green(string):
    return '\033[32m' + string + '\033[0m'

def yellow(string):
    return '\033[33m' + string + '\033[0m'

def blue(string):
    return '\033[34m' + string + '\033[0m'

def magenta(string):
    return '\033[35m' + string + '\033[0m'

def cyan(string):
    return '\033[36m' + string + '\033[0m'

def white(string):
    return '\033[37m' + string + '\033[0m'

def bold(string):
    return '\033[1m' + string + '\033[0m'

def underline(string):
    return '\033[4m' + string + '\033[0m'

def reverse(string):
    return '\033[07m' + string + '\033[0m'

def bg_black(string):
    return '\033[40m' + string + '\033[0m'

def bg_red(string):
    return '\033[41m' + string + '\033[0m'

def bg_green(string):
    return '\033[42m' + string + '\033[0m'

def bg_yellow(string):
    return '\033[43m' + string + '\033[0m'

def bg_blue(string):
    return '\033[44m' + string + '\033[0m'

def bg_magenta(string):
    return '\033[45m' + string + '\033[0m'

def bg_cyan(string):
    return '\033[46m' + string + '\033[0m'

def bg_white(string):
    return '\033[47m' + string + '\033[0m'
