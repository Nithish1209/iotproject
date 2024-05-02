def word_c(i):
    w = i.split()
    return len(w)

n=1;
with open('nimmi.txt','r') as f:
    for i in f:
        wc=word_c(i)
        print(f'line no{ n} :  {i} The number of { wc}')
        n=n+1

