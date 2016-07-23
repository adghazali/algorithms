

#words = [w.rstrip() for w in open('WORD.LST')]
words = ['train', 'python','irant']
mast_set = []


    

for word in words:
    ord_set = [len(word)]

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = 0 
        for each_letter in word:
            if each_letter == letter:
                count += 1 
        ord_set.append(count)
    mast_set.append((ord_set, word))

mast_set.sort()
print mast_set

def annograms(w):
    ord_set = [len(w)]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = 0
        for each_letter in w:
            if each_letter == letter:
                count += 1
        ord_set.append(count)

    y = (ord_set, w)
    anagrams = []

    for x in mast_set:
        if x[0] == y[0]:
            if x[1] != y[1]:
                anagrams.append(x[1])
    return anagrams
        

if __name__ == "__main__":
    print annograms("train")



