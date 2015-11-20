from pprint import pprint                                                                                                                                                 

CIGAR = 5
SEQ = 9
MD = 12

def main():
    bu = []
    with open("alignment.txt") as f:
        b = f.readline()

        # Skip the headers
        while(len(b.split('\t')) < 10):
            b = f.readline()

        for elem in f:
            tmp = elem.split('\t')
            a,b,c = None, None, None
            try:
                a = tmp[CIGAR]
                b = tmp[SEQ]
                c = tmp[MD]
            except:
                continue

            bu.append((a,b,c if c else ''))

        # Deletions
        de = {'A': 0, 'C':0, 'T':0, 'G':0}
        ins = {'A': 0, 'C':0, 'T':0, 'G':0}

        for elem in bu:
            md = elem[2]
            for i in range(len(md)):
                if(md[i] == '^'):
                    de[md[i+1]] += 1

        for elem in bu:
            cigar = zip(elem[0][::2], elem[1][1::2])
            read = elem[1]
            print(cigar,read)

if __name__ == "__main__":
    main()
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                                                                                                                                                                         
~                      
