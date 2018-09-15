# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(20)
# 鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
driver.find_element_by_link_text("搜索设置").click()
# 通过text:select_by_visible_text()
s = driver.find_element_by_id("nr")
# Select(s).select_by_visible_text("每页显示50条")
# driver.execute_script("$('#tag_receivingId_flexselect').blur();$('#tag_receivingId option:eq(2)').attr('selected',true).change();ecui.form.flexSelect('#tag_receivingId');")#运用js来下拉选择数据（隐藏属性）
# ls=driver.execute_script('return $("#hid_new_tagno").text();')#使用return返回值，运用JS来获取内容值
# print(ls)

options_list = s.find_elements_by_tag_name("option")

for option in options_list:

    print ("Value is: " + option.get_attribute("value"))
    print ("Text is:" + option.text)
    print (option.value_of_css_property)
# options1=Select(s).options
# text=[i.text for i in options1]
# for i in options1:
#     print(i)
# # 分两步：先定位下拉框，再点击选项
# s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()

# # 另外一种写法
# driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()

# # 直接通过xpath定位
# driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()

# # 通过索引：select_by_index()
# s = driver.find_element_by_id("nr")
# Select(s).select_by_index(2)

# # 通过value：select_by_value()
# s = driver.find_element_by_id("nr")
# Select(s).select_by_value("20")
