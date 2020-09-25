'''
@author: lixuewen
@file: myunittest.py
@time: 2020/9/20 18:30
@desc:
'''
import unittest
import importlib
class MyUnitTest():

    def __init__(self):
        self.report_template = '<html><body><meta http-equiv="Content-Type" content="text/html"; charset="gbk" /><table border="1" width="800" align="center"><tr><th>用例名</th><th>预期结果</th><th>实际结果</th><th>是否通过</th></tr>$data</table></body></html>'
        self.report_str = ''

    def assertEqual(self,name,actual,expect):
        if actual == expect:
            self.report_str += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(name,actual,expect,'通过')
            return True
        else:
            self.report_str += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(name,actual,expect,'不通过')
            return False

    def report(self,path='./report.html'):
        content = self.report_template.replace('$data',self.report_str)
        with open(path,'w') as file:
            file.write(content)



    def main(self):
        for i in dir(self):
            if i.startswith('test_'):
                getattr(self,i)()

    def testsuite(self,module, package, classname):
        mymodule = importlib.import_module(name=module, package=package)
        myclass = getattr(mymodule,classname)()
        list = dir(myclass)
        for method in list:
            if method. startswith('test_'):
                getattr(myclass, method)()

if __name__ == '__main__':

    my = MyUnitTest(path='./report.html').main()


