"""
Serialize and Deserialize Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        q = queue.Queue()
        q.put(root)
        res = ''
        
        while not q.empty():
            node = q.get()
            if not node:
                res += 'null,'
                continue
            res += str(node.val) + ','
            q.put(node.left)
            q.put(node.right)
            
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        ls = data.split(',')
        q = queue.Queue()
        root = TreeNode(int(ls[0]))
        q.put(root)
        i = 1
        
        while not q.empty() and i < len(ls):
            node = q.get()
            if ls[i] != 'null':
                left = TreeNode(int(ls[i]))
                node.left = left
                q.put(left)
            i += 1
            if ls[i] != 'null':
                right = TreeNode(int(ls[i]))
                node.right = right
                q.put(right)
            i += 1
              
        return root
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
