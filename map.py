a = 'Hello Hello are you there man bear pig who eats pig'

words = [i for i in a.split()]
counter = [1 for i in range(len(words))]

words_zip = list(zip(words,counter))
#print(words_zip)

words_dict = {}

for i in range(len(words)):
    if words_dict.get(words[i])==None:
        words_dict[words[i]] = [1]
    else:
        words_dict[words[i]].append(1)

print(words_dict)

