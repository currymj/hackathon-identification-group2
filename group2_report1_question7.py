from pprint import pprint                                                                                                                                                 

'''
Note - we managed to extract the deletions out of the MD tag,
but attempting to line up our MD and CIGAR fields with the actual
read resulted in a misalignment - one field will say a match,
and another will say mismatch, and the read could say '=' or anything
else. We thus couldn't reconstruct the full reference and figure
out our insertion distribution.
'''


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
