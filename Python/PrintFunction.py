'''The included code stub will read an integer,n, from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example
n=5

Print the string 12345.

Input Format

The first line contains an integer n.

Constraints
1<=n<=150'''
if __name__ == '__main__':
    n = int(input())
    for k in range(n):
        print(k+1, end="")
        