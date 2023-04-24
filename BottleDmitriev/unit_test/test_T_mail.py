import unittest
import sys
sys.path.append("C:/Users/admin/source/repos/BottleDmitriev/BottleDmitriev")
from myform import *

class Test_T_mail(unittest.TestCase): 
    def test(self):
        maillist = ["mymail@mail.ru", "validmail@mail.edu.ru", "valid_mail@mail.check", "123mail@no.hey"]
        for i in maillist:
            self.assertTrue(bool(regular_expr(i)))
