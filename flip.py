def check_regex(reg, exp):
    if reg[0] == '^':
        reg = reg[1:]
    elif reg[-1] == '$':
        reg = reg[:-1]
    i = 0
    j = 0
    while i<len(exp):
        if reg[j] == '.':
            i += 1
        elif reg[j] == '*':
            while(exp[i-1] == exp[i]):
                i += 1
        elif exp[i] == reg[j]:
                i += 1
        else:
            return False
        j += 1
    return True

string , pattern = raw_input("ENTER STRING AND pattern \n").strip().split(" ")
check_regex(string, pattern)