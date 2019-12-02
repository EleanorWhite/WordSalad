
def processOuters(s):
    outers = []
    for c in s:
        if c.isalpha():
            outers.append(c)
    return outers

def goodWord(line, center, outers):
    hasCenter = False
    for c in line.strip():
        if not ((c in outers) or (c == center)):
            return False
        if (c == center):
            hasCenter = True
    return hasCenter





def main() :
    center = ""
    while not (center.strip().isalpha and len(center.strip()) == 1):
        print("Enter Center letter")
        center = input()
    
    outers = []
    while not (outers != []):
        print("Enter Outer letters")
        outers = processOuters(input())

    f = open("./words.txt", 'r')
    for line in f:
        if (goodWord(line, center, outers)):
            print(line.strip())


if __name__ == "__main__":
    main()
