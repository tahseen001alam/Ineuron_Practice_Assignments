def iss(s, t):
    if len(s) != len(t):
        return False

    st = {}
    ts = {}

    for i in range(len(s)):
        if s[i] not in st:
            st[s[i]] = t[i]
        elif st[s[i]] != t[i]:
            return False

        if t[i] not in ts:
            ts[t[i]] = s[i]
        elif ts[t[i]] != s[i]:
            return False

    return True
s=input()
t=input()
print(iss(s,t))
