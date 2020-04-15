"""
Given two string A and B. Check if A is a rotated version of B
For example, "winterbreak" is a cyclic rotation of "breakwinter" (and vice versa). 
"""

def rotate_string(self, A: str, B: str) -> bool:
    return len(A) == len (B) and A in 2*B
