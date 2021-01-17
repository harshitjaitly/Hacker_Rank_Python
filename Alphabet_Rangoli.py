def print_rangoli(size):
    # your code goes here
    alp_bets = [chr(x) for x in range(97,97+size)]
    rev_alp_bets =alp_bets[::-1]
    width = (size*4)-3

    in_use = []
    for i in range(size) :
        if(i==0) :
            in_use = in_use+[rev_alp_bets[:i+1]]
        else :
            in_use = in_use+[rev_alp_bets[:i+1] + alp_bets[-i:]]

    final = ["-".join(i).center(width,'-') for i in in_use]
    final = final+final[::-1][1:]
    print(*final, sep = '\n')

    # import string
    #
    # alpha = string.ascii_lowercase
    # n = size
    # L = []
    #
    # for i in range(n):
    #
    #     s = "-".join(alpha[i:n])
    #     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    #
    # print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    int(input())
    print_rangoli(n)
