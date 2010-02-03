# vim:fileencoding=utf-8
from unittest import TestCase

from bputils.javascript import * 

class JavascriptUtilsTestCase(TestCase):

    def test_escapejs_json(self):
        self.assertEqual(escapejs_json(u"<テスト>"), u'\\u003cテスト\\u003e')
        self.assertEqual(escapejs_json(u"Q&A"), u"Q\\u0026A")
        self.assertEqual(escapejs_json(u"データ"), u"データ")

    def test_force_js(self):
        from datetime import datetime,date,time
        self.assertEqual(force_js({"msg": u"メッセージ"}), '{"msg": "\\u30e1\\u30c3\\u30bb\\u30fc\\u30b8"}')
        self.assertEqual(force_js(datetime(2009, 12, 22, 16, 35, 02)), '"2009-12-22 16:35:02"') 
        self.assertEqual(force_js(date(2009, 12, 22)), '"2009-12-22"') 
        self.assertEqual(force_js(time(16, 35, 02)), '"16:35:02"')

    def test_force_js_type(self):
        self.assertEqual(force_js("", "bool"), "false")
        self.assertEqual(force_js("5", "int"), '5')
        self.assertEqual(force_js("test", "array"), '["t", "e", "s", "t"]')
        self.assertEqual(force_js(5, "string"), '"5"')
