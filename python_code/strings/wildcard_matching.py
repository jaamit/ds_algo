"""
Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

ref:- https://leetcode.com/problems/wildcard-matching/discuss/370736/Detailed-Intuition-From-Brute-force-to-Bottom-up-DP
I really like this approach
"""

def is_match(s, p):
    return check(s, p, 0, 0)


def check(s, p, start_s, start_p):
    # print('start_s :', start_s, 'start_p :', start_p)
    if start_s == len(s) and start_p == len(p): # reached end of both s and p
        return True
    if start_p == len(p):  # there are still characters in S => there is no match
        return False
    if start_s == len(s):
        return p[start_p] == '*' and check(s, p, start_s, start_p+1)
    if p[start_p] == '*':
        # star either matches 0 or >=1 character
        return check(s, p, start_s+1, start_p) or check(s, p, start_s, start_p+1)
    elif p[start_p] == '?' or s[start_s] == p[start_p]:
        # move both pointers
        return check(s, p, start_s+1, start_p+1)
    else: # the current char from P is a lowercase char different from s[start_s]
        return False
