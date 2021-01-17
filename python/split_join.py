if __name__ == "__main__":
    string = "Hi, man!\nHow\tare you      doing?"
    print(string)

    # Split without separator will split by space, line break, tab etc.
    print(" ".join(string.split()))

    print("a,b,c,d,e,,,,f".split(","))

    print("a,b,c,d,e,f".split(",", maxsplit=1))

    print("a,b,c,d,e,f".split(",", maxsplit=-1))
