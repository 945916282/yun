from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class Auto(unittest.TestCase):
    #登录
    def setUp(self):
        self.we=webdriver.Firefox()
        self.we.get("http://192.168.0.126:801/Login.aspx")
        time.sleep(3)
        self.we.find_element_by_id("tbx_UserName").send_keys("adm")
        time.sleep(3)
        self.we.find_element_by_id("tbx_Password").send_keys("adm")
        self.we.find_element_by_css_selector("#ibtLogin").click()
        time.sleep(3)
    # 1.新建事务保存成功
    def test_case1(self):
        self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(1)").click()
        self.we.implicitly_wait(10)
        self.we.switch_to.frame(2)
        a=self.we.find_element_by_id("kind")
        a.click()
        time.sleep(3)
        Select(a).select_by_index(1) #下拉框
        time.sleep(3)
        self.we.find_element_by_css_selector("#subject").click()
        self.we.find_element_by_css_selector("#subject").send_keys("出差")
        self.we.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-03")
        time.sleep(5)
        self.we.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys("1")
        self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys("1000")
        self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").click()
        self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys("灰机票")
        self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys("2000")
        self.we.find_element_by_id("save").click()
        b=self.we.switch_to.alert
        print(b.text)
        c=b.text
        self.assertEqual(c,"成功：当前事务创建成功！",msg="创建失败")
        b.accept()
        time.sleep(10)
    #新建事务主题为空
    # def test_case2(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(1)").click()
    #     self.we.implicitly_wait(10)
    #     self.we.switch_to.frame(2)
    #     a = self.we.find_element_by_id("kind")
    #     a.click()
    #     time.sleep(3)
    #     Select(a).select_by_index(1)  # 下拉框
    #     time.sleep(3)
    #     self.we.find_element_by_css_selector(
    #         "#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys(
    #         "2020-06-03")
    #     time.sleep(5)
    #     self.we.find_element_by_css_selector(
    #         "#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys(
    #         "1")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys("1000")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").click()
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys("灰机票")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys("2000")
    #     self.we.find_element_by_id("save").click()
    #     d = self.we.find_element_by_css_selector("body > div:nth-child(3)").text
    #     print(d)
    #     self.assertEqual(d,"◆\n◆\n!请填写此字段。", msg="创建失败")
    #     time.sleep(5)
    # # 日期为空
    # def test_case03(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(1)").click()
    #     self.we.implicitly_wait(10)
    #     self.we.switch_to.frame(2)
    #     a = self.we.find_element_by_id("kind")
    #     a.click()
    #     time.sleep(3)
    #     Select(a).select_by_index(1)  # 下拉框
    #     time.sleep(3)
    #     self.we.find_element_by_css_selector("#subject").click()
    #     self.we.find_element_by_css_selector("#subject").send_keys("出差")
    #     self.we.find_element_by_css_selector(
    #         "#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys(
    #         "1")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys("1000")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").click()
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys("灰机票")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys("2000")
    #     self.we.find_element_by_id("save").click()
    #     e=self.we.find_element_by_css_selector("body > div:nth-child(3)").text
    #     print(e)
    #     self.assertEqual(e, "◆\n◆\n!请填写此字段。", msg="创建失败")
    # #票据为空
    # def test_case04(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(1)").click()
    #     self.we.implicitly_wait(10)
    #     self.we.switch_to.frame(2)
    #     a = self.we.find_element_by_id("kind")
    #     a.click()
    #     time.sleep(3)
    #     Select(a).select_by_index(1)  # 下拉框
    #     time.sleep(3)
    #     self.we.find_element_by_css_selector("#subject").click()
    #     self.we.find_element_by_css_selector("#subject").send_keys("出差")
    #     self.we.find_element_by_css_selector(
    #         "#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys(
    #         "2020-06-03")
    #     time.sleep(5)
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys("1000")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").click()
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys("灰机票")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys("2000")
    #     self.we.find_element_by_id("save").click()
    #     f=self.we.find_element_by_css_selector("body > div:nth-child(3)")
    #     print(f.text)
    #     g= f.text
    #     self.assertEqual(g, "◆\n◆\n!请填写此字段。", msg="创建失败")
    # #项目为空
    # def test_case05(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(1)").click()
    #     self.we.implicitly_wait(10)
    #     self.we.switch_to.frame(2)
    #     a = self.we.find_element_by_id("kind")
    #     a.click()
    #     time.sleep(3)
    #     Select(a).select_by_index(1)  # 下拉框
    #     time.sleep(3)
    #     self.we.find_element_by_css_selector("#subject").click()
    #     self.we.find_element_by_css_selector("#subject").send_keys("出差")
    #     self.we.find_element_by_css_selector(
    #         "#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys(
    #         "2020-06-03")
    #     time.sleep(5)
    #     self.we.find_element_by_css_selector(
    #         "#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys(
    #         "1")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input").send_keys("1000")
    #     self.we.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input").send_keys("2000")
    #     self.we.find_element_by_id("save").click()
    #     h=self.we.find_element_by_css_selector("body > div:nth-child(3)")
    #     print(h.text)
    #     j=h.text
    #     self.assertEqual(j, "◆\n◆\n!请填写此字段。", msg="创建失败")
    # #2.已建事务(日期输入、搜索关键字、下拉框）
    # def test_case06(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(2)").click()
    #     self.we.switch_to.frame("tab_OaAffairList_ifm")
    #     self.we.find_element_by_css_selector("#Date1").send_keys("2020-05-31")
    #     self.we.find_element_by_css_selector("#Date2").send_keys("2020-06-06")
    #     a=self.we.find_element_by_css_selector("html body form#form1 dl.dl.form_bar dd select#ddl_Kind.border")
    #     Select(a).select_by_index(1)
    #     self.we.find_element_by_css_selector("#tbx_Keyword").send_keys("ADM")
    #     self.we.find_element_by_css_selector("#btnSearch").click()
    #     self.we.switch_to.default_content()
    #     time.sleep(3)
    # # 3.代办事务
    # def test_case07(self):
    #     self.we.find_element_by_css_selector(" ul:nth-child(6) > li:nth-child(3)").click()
    #     self.we.switch_to.frame(2)
    #     self.we.find_element_by_xpath("//*[@id='GridView1_ctl13_lbt_Operation']").click()
    #     time.sleep(5)
    #     self.we.switch_to.default_content()
    #     self.we.switch_to.frame(3)
    #     self.we.find_element_by_xpath("//*[@id='opinion']").send_keys("同意")
    #     time.sleep(3)
    #     self.we.find_element_by_xpath("//*[@id='selectClerk']").click()
    #     self.we.switch_to.frame(1)
    #     self.we.find_element_by_xpath("//*[@id='TreeView1n2CheckBox']").click()
    #     self.we.find_element_by_xpath("//*[@id='btn_Ok']").click()
    #     self.we.switch_to.parent_frame()
    #     time.sleep(3)
    #     self.we.find_element_by_xpath("//*[@id='save']").click() ###
    #     self.we.switch_to.default_content()
    #     time.sleep(3)
    # #已办事务(么有)
    # def test_case08(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(4)").click()
    #     self.we.switch_to.frame(2)
    #     self.we.find_element_by_css_selector("#Date1").send_keys("2020-05-31")
    #     self.we.find_element_by_css_selector("#Date2").send_keys("2020-06-06")
    #     self.we.find_element_by_css_selector("#ddl_Kind").click()
    #     k=self.we.find_element_by_css_selector("#ddl_Kind")
    #     Select(k).select_by_index(2)
    #     time.sleep(3)
    #     self.we.find_element_by_css_selector("#tbx_Keyword").send_keys("ADM")
    #     self.we.find_element_by_css_selector("#btnSearch").click()
    #     self.we.switch_to.default_content()
    #     time.sleep(5)
    # #查阅事务
    # def test_case09(self):
    #     self.we.find_element_by_css_selector("ul:nth-child(6) > li:nth-child(5)").click()
    #     self.we.switch_to.frame(2)
    #     self.we.find_element_by_css_selector("#Date1").clear()
    #     self.we.find_element_by_css_selector("#Date1").send_keys("2020-05-31")
    #     self.we.find_element_by_css_selector("#Date2").send_keys("2020-06-06")
    #     self.we.find_element_by_css_selector("#ddl_Kind").click()
    #     k = self.we.find_element_by_css_selector("#ddl_Kind")
    #     Select(k).select_by_index(2)
    #     time.sleep(3)
    #     self.we.find_element_by_css_selector("#tbx_Keyword").send_keys("ADM")
    #     self.we.find_element_by_css_selector("#btnSearch").click()
    #     l=self.we.find_element_by_xpath("//*[@id='GridView1_ctl04_ddlPageSize']") #每页显示
    #     Select(l).select_by_value('10')
    #     time.sleep(3)
    #     above=self.we.find_element_by_xpath("//*[@id='GridView1_ctl02_lblViewAmount']")
    #     ActionChains(self.we).move_to_element(above).perform()
    #     self.we.find_element_by_xpath("//*[@id='GridView1_ctl02_lbtSubject']").click()
    #     time.sleep(5)
    #     self.we.switch_to.default_content()
    #     time.sleep(5)

    def tearDown(self):
        self.we.quit()

if __name__=="__main__":
    unittest.main()


