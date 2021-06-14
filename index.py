import subprocess
import contextlib


#Replace "Intercept.json" with the story you want to play
command = ["node", "parser.js", "Intercept.json"]


def process(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
    universal_newlines=True, encoding = 'utf-8', bufsize=0, stdin=subprocess.PIPE)
    for line in unbuffered(p):
        if "qnext" not in line:
            #Your output method
            print (line)
            try:
                past = int(line[0])
            except:
                v = True
        elif "qnext" in line:
            abc = True
            #Runs until a valid number is entered, then enters that number as a choice
            while abc == True:
                #Your input method
                inp = (input('Input: ')).strip()
                if inp.isnumeric() and int(inp) <= past and int(inp) > 0:
                    p.stdin.write(inp+"\n")
                    abc = False
                else:
                    print ("Invalid input. Please try again.")


#Output antibuffer code. Credit to https://gist.github.com/thelinuxkid/5114777
newlines = ['\n', '\r\n', '\r']
def unbuffered(proc, stream='stdout'):
    stream = getattr(proc, stream)
    with contextlib.closing(stream):
        while True:
            out = []
            last = stream.read(1)
            if last == '' and proc.poll() is not None:
                break
            while last not in newlines:
                if last == '' and proc.poll() is not None:
                    break
                out.append(last)
                last = stream.read(1)
            out = ''.join(out)
            yield out
process(command)
