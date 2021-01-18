# link - https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    from collections import OrderedDict
    sub_seq = []
    i = 0
    while (i<len(string)) :

        sub_str = string[i:i+k]
        sub_seq.append( ''.join(OrderedDict.fromkeys(sub_str).keys()) )
        i+=k

    print(*sub_seq, sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
