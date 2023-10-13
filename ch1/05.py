def get_ngram(text, n):
    ngram = []
    for i in range(len(text) - n + 1):
        ngram.append(text[i:i+n])
    return ngram

text = "I am an NLPer"

print(get_ngram(text, 2))
print(get_ngram(text.split(), 2))
