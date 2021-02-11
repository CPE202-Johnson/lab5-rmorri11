
import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())                     #test is_empty works
        self.assertFalse(q.is_full())                     #test is_full works
        q.enqueue('thing')
        self.assertEqual(q.dequeue(), 'thing')            #test dequeue works
        self.assertEqual(q.size(), 0)                     #test size works
        with self.assertRaises(IndexError): q.dequeue()   #test dequeue indexError
        q.enqueue(0)                                      #test enqueing random datatypes
        q.enqueue(-124.9876)
        q.enqueue(None)
        q.enqueue(-13)
        q.enqueue('')
        with self.assertRaises(IndexError): q.enqueue(67)  #test enqueue indexError
        self.assertTrue(q.is_full())                       #test is_empty works
        self.assertFalse(q.is_empty())                     #test is_full works

    # for the array, make sure the read and write pointers 
     # are wrapping around the circular array correctly
    def test_write_wraparound(self):
        q = Queue(4)
        q.enqueue(0)
        q.enqueue(-124.9876)
        q.enqueue(None)
        q.enqueue(-13)
        a = q.dequeue()
        a = q.dequeue()
        a = q.dequeue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(4)
        a = q.dequeue()
        a = q.dequeue()
        self.assertEqual(q.dequeue(), 2)
    
    def test_fully_dequeue(self):
        q = Queue(4)
        q.enqueue(0)
        q.enqueue(-124.9876)
        q.enqueue(None)
        q.enqueue(-13)
        with self.assertRaises(IndexError): q.enqueue(67)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), -124.9876)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.dequeue(), -13)
        with self.assertRaises(IndexError): q.dequeue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
    
    def test_queue_fill_to_capacity_and_dequeue_all(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertRaises(IndexError, q.dequeue)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertRaises(IndexError,q.enqueue,6)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.size(), 0)



if __name__ == '__main__': 
    unittest.main()
