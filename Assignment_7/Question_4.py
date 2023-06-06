def r_w(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

s=input()
print(r_w(s))
