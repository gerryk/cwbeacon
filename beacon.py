import time
# import RPi.GPIO as GPIO

class CWString(object):
    letters = { 'a' : '.-',
           'b' : '-...',
           'c' : '-.-.',
           'd' : '-..',
           'e' : '.',
           'f' : '..-.',
           'g' : '--.',
           'h' : '....',
           'i' : '..',
           'j' : '.---',
           'k' : '-.-',
           'l' : '.-..',
           'm' : '--',
           'n' : '-.',
           'o' : '---',
           'p' : '.--.',
           'q' : '--.-',
           'r' : '.-.',
           's' : '...',
           't' : '-',
           'u' : '..-',
           'v' : '...-',
           'w' : '.--',
           'x' : '-..-',
           'y' : '-.--',
           'z' : '--..',
           '1' : '.----',
           '2' : '..---',
           '3' : '...--',
           '4' : '....-',
           '5' : '.....',
           '6' : '-....',
           '7' : '--...',
           '8' : '---..',
           '9' : '----.',
           '0' : '-----',
           '.' : '.-.-.-',
           '/' : '-..-.',
           ',' : '--..--',
           '?' : '..--..'
          }

    cw = ""

    def encode(self, m):
        self.cw = ""
        new_word = True
        for i in m:
            if i in self.letters:
                if not new_word:
                    self.cw = self.cw + " "
                self.cw = self.cw + self.letters[i]
                new_word = False
            elif i is " ":
                self.cw = self.cw + "/"
                new_word = True
            else: # Unrecognised character... what now?
                pass
        return self.cw

class CWSender(object):
    cps = None
    csp = None
    wsp = None
    timer = None

    def __init__(self, cps, cspace, wspace):
        self.cps = cps
        self.csp = cspace
        self.wsp = wspace

    def send(self, m):
        for i in m:
            if i == '.':
                self.dit()
                self.pause()
            if i == '-':
                self.dah()
                self.pause()
            if i == ' ':
                self.cspace()
            if i == '/':
                self.wspace()


    def dit(self):
        print 'dit '

    def dah(self):
        print 'dah '

    def wspace(self):
        print '--- '

    def cspace(self):
        print '- '

    def pause(self):
        print ' '


def main():
    import argparse
    parser = argparse.ArgumentParser('CW Beacon Sender - uses GPIO pin')
    parser.add_argument('-c', '--cps', type=int, default='15', help='Characters per second to send')
    parser.add_argument('-s', '--space', type=int, default=3, help='Farnsworth spacing... space value in \'dits\'')
    parser.add_argument('-w', '--wspace', type=int, default=9, help=
        "Word spacing... value in 'dits'")
    parser.add_argument('message', nargs='+', help='Text string to send as CW')
    args = parser.parse_args()
    cw = CWString()
    message = ' '.join(args.message)
    encoded = cw.encode(message)
    sender = CWSender(args.cps, args.space, args.wspace)
    sender.send(encoded)

if __name__ == "__main__":
    main()
