PREFIX = '\u001b['
ANSI_RESET = "\u001B[0m"

def colorizeString(s: str, textColorCode: str='', backColorCode: str=''):
    return f'{textColorCode}{backColorCode}{s}{ANSI_RESET}'

def genANSI_TextTrueColorCode(r, g, b):
    return f'{PREFIX}38;2;{r};{g};{b}m'

def genANSI_BackTrueColorCode(r, g, b):
    return f'{PREFIX}48;2;{r};{g};{b}m'