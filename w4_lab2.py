s = input().strip()
s = s.lower()
words_list = s.split()
count = dict()

for word in words_list:
    if word in count:
        continue
    count[word] = s.count(word)

for word, count in count.items():
    print(word, count)