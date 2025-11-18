#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cem = 0
    for i in range(1, len(sys.argv)):
        cem += int(sys.argv[i])
    print(cem)
