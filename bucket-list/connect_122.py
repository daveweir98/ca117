import sys

n = int(sys.argv[1])

def main():
    table = [i.strip() for i in sys.stdin]
    count = 0
    for i, line in enumerate(table):
        for j, char in enumerate(line):
            row = ""
            column = ""
            diag = ""
            rev_diag = ""
            if char == "x":
                for k in range(n+1):
                    try:
                        row += line[j+k]
                    except:
                        pass
                    try:
                        column += table[i + k][j]
                    except:
                        pass
                    try:
                        diag += table[i + k][j + k]
                    except:
                        pass
                    try:
                        if j - k >= 0:
                            rev_diag += table[i + k][j - k]
                    except:
                        pass
                if row == "x" * n + "." or row == "x" * n:
                    count += 1
                if column[:n] == "x" * n and column != "x" * (n + 1):
                    count += 1
                if diag[:n] == "x" * n and diag != "x" * (n + 1):
                    count += 1
                if rev_diag[:n] == "x" * n and rev_diag != "x" * (n + 1):
                    count += 1

    print(count)

if __name__ == "__main__":
    main()
