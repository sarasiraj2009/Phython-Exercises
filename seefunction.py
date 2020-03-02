def see1(word, pharse):
    count = 0
    word = word.strip()
    list = pharse.split(" ")
    for i in range(len(list)):
        if word == list[i]:
            count+=1
        else:
            continue
    return count

word = input("Please input word: ")
pharse = input("Please input pharse: ")

print(see1(word, pharse))