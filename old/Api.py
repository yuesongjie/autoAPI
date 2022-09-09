from Base.BaseElementEnmu import Element
from Base.BaseGetExcel import read_excel
from Base.BaseIni import BaseIni
from Base.BaseReq import Config
from Base.BaseRunner import ParametrizedTestCase


class ApiTest(ParametrizedTestCase):
    @staticmethod
    def test_api():
        ls = read_excel(Element.API_FILE)
        if BaseIni(Element.OPEN_PICT).read_ini():
            Config().config_req_pict(ls)
        else:
            Config().config_req(ls)

    @classmethod
    def setUpClass(cls):
        super(ApiTest, cls).setUpClass()
        # cls.req
