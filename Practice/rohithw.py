import string
def repeat_words():
    content = ['too wet to go out and too cold to play ball.', 'so we sat in the house.', 'we did nothing at all.', 'so all we could do was to sit! sit! sit! sit']
    sentences=[]
    for sentence in content:
        sentences.append(sentence.split(' '))

    results =[]
    for sentence in sentences:
        rep_words=[]
        result =[]
        for word in sentence:
            if word.endswith("!"):
                word = word.strip(string.punctuation)
            if word not in rep_words:
                rep_words.append(word)
            else:
                result.append(word)
        results.append(result)
    print(results)












repeat_words()