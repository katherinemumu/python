

def crypo(s):
    ss = ''
    for i in range(1,len(s),2):
        ss = ss + s[i] + s[i-1]
    if (len(s) % 2 == 0):
        return ss
    else:
        return ss+s[-1]
