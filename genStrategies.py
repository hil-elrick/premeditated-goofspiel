toMake = 20
def main():
    import random
    base = list(range(1,14))
    outString = ""
    for i in range(toMake):
        random.shuffle(base)
        tempString = ' '.join(str(e) for e in base)
        outString += '['
        outString += tempString.replace(',', ' ')
        outString += ']\n'
    with open("in.txt", 'w') as f:
        f.write(outString)

if __name__ == "__main__":
    main()
