'''Consider the following:

A string, S, of length n where S=C0C1.....Cn-1.
An integer, K, where K is a factor of n.
We can split S into n/k substrings where each subtring, t1, consists of a contiguous block of K characters in S. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.
Given s and k, print n/k lines where each line i denotes string ui.

Example
s='AAABCADDE' 
k=3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1='A'. The second substring has all distinct characters, so u2='BCA'. The third substring has 2 different characters, so u3='DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format

The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

Constraints

1<=n<=10^4 , where n is the length of s
1<=k<=n
It is guaranteed that n is a multiple of k.
'''
def merge_the_tools(string, k):
    
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)