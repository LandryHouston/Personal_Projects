def main():
    te = input()
    result = convert(te)
    print(result)

def convert(te):
    text = te.replace(":)", "🙂")
    tex1 = text.replace(":(", "🙁")
    return tex1


main()