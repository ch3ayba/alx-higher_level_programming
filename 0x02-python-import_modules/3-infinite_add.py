#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    somme = 0
    for num in range(len(sys.argv) - 1):
        somme += int(sys.argv[num + 1])
    print("{}".format(somme))
