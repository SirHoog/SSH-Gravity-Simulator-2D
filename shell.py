from cmd import Cmd

class Shell(Cmd):
    intro="Thanks for trying `SSH Gravity Simulator 2D` by Sir Hoog! Have fun!\n\n"
    use_rawinput=False
    prompt=" > "

    def __init__(self, stdin=None, stdout=None):
        super(Shell, self).__init__(completekey='tab', stdin=stdin, stdout=stdout)

    def print(self, txt):
        if self.stdout and not self.stdout.closed:
            self.stdout.write(txt)
            self.stdout.flush()
    def println(self, txt):
        self.print(txt + '\r\n')
    def newline(self):
        self.print('\r\n')