def getcloseparan(s, openindex):

    openbrackets = 0
    s = list(s)

    for i,j in enumerate(s):
        if i > openindex:
            if j == "(":
                openbrackets += 1
            elif j == ")":
                if openbrackets == 0:
                    return i
                else:
                    openbrackets -= 1

    return None


if __name__ == "__main__":

    print(getcloseparan("(hello(morning)world)he he", 1))
