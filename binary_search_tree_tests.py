import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_unbalanced_tree(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(1)
        bst.insert(10)
        bst.insert(0)
        bst.insert(2)
        bst.insert(4)
        bst.insert(7)
        bst.insert(3)
        bst.insert(15)
        bst.insert(12)
        bst.insert(16, 'yea')
        self.assertFalse(bst.search(11))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(12))
        self.assertEqual(bst.find_min(), (0, None))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (16, 'yea'))
        self.assertEqual(bst.tree_height(), 4)
        self.assertEqual(bst.inorder_list(), [0,1,2,3,4,5,7,10,12,15,16])
        self.assertEqual(bst.preorder_list(), [5,1,0,2,4,3,10,7,15,12,16])
        self.assertEqual(bst.level_order_list(), [5,1,10,0,2,7,15,4,12,16,3])



if __name__ == '__main__': 
    unittest.main()
