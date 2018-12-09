import sys
import re


def arduino_style(match):
    pin = match.group(1)
    value = match.group(2)
    if value == '1':
        value = 'PIN_HIGH'
    elif value == '0':
        value = 'PIN_LOW'
    return 'rt_pin_write(COM' + pin + ', ' + value + ');'


# Define a main() function that prints a little greeting.
def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: filename'
        sys.exit(1)
    filename = args[0]
    f = open(filename, 'rU')
    text = f.read()
    new_text = re.sub(r'COM(\d+)\s*=\s*(\d);', arduino_style, text)
    f.close()
    outf = open(filename + '.arduion_style', 'w')
    outf.write(new_text)
    outf.close()
    sys.exit(0)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
