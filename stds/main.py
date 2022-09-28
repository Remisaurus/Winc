# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here

import sys


def main():
    linelist = []
    argin1 = []
    for line in sys.stdin:
        linelist.append(line) # linelist contains all lines of stdin
    for line in sys.argv:
        argin1.append(line[-1])
    print(argin1)
    if len(argin1) != 2:
        print('This program requires precisely one argument of which the last character will be used as definitive argument.')
        print('try again with that confinement.')
        sys.exit()
    argument = argin1[1]
    
    # TODO: Print the result to stdout

    # TODO: Print the total number of removed characters to stderr
    ...


if __name__ == "__main__":
    main()
