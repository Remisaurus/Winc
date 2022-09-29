# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"
# Your code here

import sys

def main():
    linelist = []
    linelistold = []
    argin1 = []
    for line in sys.argv:
        argin1.append(line[-1])
    if len(argin1) != 2:
        print('This program requires precisely one argument of which the last character will be used as the definitive argument.')
        print('try again with that confinement.')
        sys.exit()
    argument = argin1[1]
    removed_count = 0
    for line in sys.stdin:
        temp = []
        for character in line:
            if character != argument:
                temp.append(character)
            else:
                removed_count += 1
        linelist.append(''.join(temp))       
        linelistold.append(line) # linelist contains all lines of stdin
    sys.stderr.write(str(removed_count))
    sys.stdout.write(''.join(linelist))

if __name__ == "__main__":
    main()