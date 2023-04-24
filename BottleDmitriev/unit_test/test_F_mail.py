import unittest
import sys
sys.path.append("C:/Users/admin/source/repos/BottleDmitriev/BottleDmitriev")
from myform import *

class Test_F_mail(unittest.TestCase): #incorrect mails test module
    def test(self):
        maillist = ["", "1", "m1@", "@mail", ".com", "hellomymail.com", "testcase()@mail.ru", "mymail @ mail.ru", "mail@mail,ru"] #correct mails list
        for i in maillist: #test every mail in list
            self.assertFalse(bool(regular_expr(i)))
            