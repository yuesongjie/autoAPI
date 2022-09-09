import sys
import unittest

from Base.BaseGetExcel import write_excel
from Base.BaseInit import BaseInit
from Base.BaseRunner1 import ParametrizedTestCase
from Runner.Api import ApiTest

sys.path.append("..")


def runner_case():
    BaseInit().mk_file()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(ApiTest))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runner_case()
    write_excel()
