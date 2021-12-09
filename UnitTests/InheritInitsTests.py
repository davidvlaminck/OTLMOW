import ast
import tarfile
import unittest


class A:
    def __init__(self, param1, param2, param3, param4, param5):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5


class B(A):
    def __init__(self, param1, param2, aInstance: A):
        super().__init__(param1, param2, aInstance.param1, aInstance.param2, aInstance.param3)


class ContainerBuisTests(unittest.TestCase):
    def test_run(self):
        a = A(1,2,3,4,5)
        b = B(1,2,a)
        self.assertTrue(a.param1 == 1)
        self.assertTrue(b.param3 == 1)
