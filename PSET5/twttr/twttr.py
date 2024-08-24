def shorten(sentence):
    res = ""
    for word in sentence:
        if word.lower() in ("a", "e", "i", "o", "u"):
            continue
        else:
            res += word
    return f"{res}"
def main():
    sentence=input("Word: ")
    print(shorten(sentence))

if __name__ == "__main__":
    main()
