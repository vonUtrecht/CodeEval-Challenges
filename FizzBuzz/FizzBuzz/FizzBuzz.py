import sys

def fizzBuzz(div1, div2, maxCount):
    for n in range(1, maxCount + 1):
        replaced = False
        if (n % div1 == 0):
            print('F', end='')
            replaced = True
        if (n % div2 == 0):
            print('B', end='')
            replaced = True
        if not replaced:
            print(n, end='')
        print(' ', end='')
    print()

def main(argv):
    fileName = argv[0] # ignore any other arguments
    with open(fileName) as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            print(line)
            values = [int(v) for v in line.split()]
            # Assume the numbers are valid positive (>0) integers but constrain them
            # x in range (1,20), y in range (1,20), n in range (21,100)
            x = values[0]
            y = values[1]
            n = values[2]
            if (x > 20):
                x = 20
            if (y > 20):
                y = 20
            if ((n < 21) or (n > 100)):
                n = 50
            fizzBuzz(x, y, n)
            print()

if __name__ == "__main__":
    main(sys.argv[1:])