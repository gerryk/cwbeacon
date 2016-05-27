import time
import RPi.GPIO as GPIO

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
    timer = None

    def __init__(self, cps):
        self.cps = cps
        self.dit_length = 1.0/cps
        self.dah_length = self.dit_length*3

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
        GPIO.output(11,True)
        time.sleep(self.dit_length)
        GPIO.output(11,False)

    def dah(self):
        GPIO.output(11,True)
        time.sleep(self.dah_length)
        GPIO.output(11,False)


    def wspace(self):
        time.sleep(self.dah_length * 3)

    def cspace(self):
        time.sleep(self.dah_length)

    def pause(self):
        time.sleep(self.dit_length)


def main():
    import argparse
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11,False)
    parser = argparse.ArgumentParser('CW Beacon Sender - uses GPIO pin')
    parser.add_argument('-c', '--cps', type=int, default='15', help='Characters per second to send')
    parser.add_argument('message', nargs='+', help='Text string to send as CW')
    args = parser.parse_args()
    cw = CWString()
    message = ' '.join(args.message)
    encoded = cw.encode(message)
    sender = CWSender(args.cps)
    sender.send(encoded)

if __name__ == "__main__":
    main()
