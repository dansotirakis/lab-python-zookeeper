n = int(input())
word = input()
words = []

while n > 0:
    words.append(word)
    n -= 1

print("".join(str(x) for x in words))
