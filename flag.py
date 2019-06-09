import argparse

def flag(n):
    arr = [['#' for i in range(n*3+2)] for i in range(n*2+2)]
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr)+n-1):
            arr[i][j] = ' '
    for i in range(int(n/2)+1,int(n/2)+n+1):
        for j in range(n+1,n*2+1):
            if i==j or j== i+n:
                arr[i][j] = '*'
            elif i > j or i+n<j:
                arr[i][j] = ' '
            elif n/2+n>i>n/2+1 and 2*n>j>n+1:
                arr[i][j] = 'o'
    for i in range(-int(n/2)-2,-len(arr)+int(n/2),-1):
        for j in range(n+1,n*2+1):
            if i+1 == -j or i-n+1 == -j:
                arr[i][j] = '*'
            elif i+1 < -j or i-n+1 > -j:
                arr[i][j] = ' '
    for i in range(len(arr)):
        arr[i].extend(['\n'])

    st = ''.join(str(i) for j in arr for i in j)
    print(st)
    return st

def main():
    parser = argparse.ArgumentParser()
    n = parser.add_argument('n',help="The even number you want to draw flag",type=int)
    args = parser.parse_args()
    if args.n%2==1:
        raise argparse.ArgumentError(n, "The parameter must be even integer number'")
    result = flag(args.n)

if __name__ == '__main__':
    main()
