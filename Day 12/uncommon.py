#find uncommon words from two sentences

def uncommon(sentence1,sentence2):
    L1 = sentence1.split()
    L2 = sentence2.split()

    uncommon = [i for i in L1+L2 if i not in L1 or i not in L2]
    return uncommon

def main():

    s1 = "Hello World , I live in Mumbai"
    s2 = "Hello India , I live in Goa"

    result = uncommon(s1,s2)
    print(result)

if __name__=="__main__":
    main()