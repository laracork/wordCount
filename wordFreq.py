import re, string

def word_freq(str):
    str = re.sub(r'[^\w\s]', '', str).lower()
    freq = dict()
    words = str.split()

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

def sort_dict_by_value(dict):
    return sorted(dict.items(), key = lambda(k,v): v, reverse=True)

freq = word_freq('From the moment the first immigrants arrived on these shores, generations of parents have worked hard and sacrificed whatever is necessary so that their children could have the same chances they had; or the chances they never had. Because while we could never ensure that our children would be rich or successful; while we could never be positive that they would do better than their parents, America is about making it possible to give them the chance. To give every child the opportunity to try. Education is still the foundation of this opportunity. And the most basic building block that holds that foundation together is still reading. At the dawn of the 21st century, in a world where knowledge truly is power and literacy is the skill that unlocks the gates of opportunity and success, we all have a responsibility as parents and librarians, educators and citizens, to instill in our children a love of reading so that we can give them the chance to fulfill their dreams.')
sorted = sort_dict_by_value(freq)

for k,v in sorted:
    print(k, v)
