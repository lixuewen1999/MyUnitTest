'''
@author: lixuewen
@file: test.py
@time: 2020/9/20 22:00
@desc:
'''
from day33.unittest.myunittest import MyUnitTest
from day33.unittest.ddt import data
list = [['1+1是否等于2',1,1,2],['2+1是否等于3',2,1,3],['3+1是否等于4',3,1,4]]

class Test(MyUnitTest):

    @data(list)
    def test_1(self,name,x,y,expect):
        actual = x+y
        self.assertEqual(name,actual,expect)

if __name__ == '__main__':
    T = Test()
    T.main()
    T.report()
    T.testsuite('test','day33.unittest','Test')