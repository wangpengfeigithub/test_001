#coding=utf8
from appium import webdriver
import time
import unittest
import HTMLTestRunner

class testlogin(unittest.TestCase):
	u'创建登录app的测试用例'
	def setUp(self):
		u'创建APP登录的函数'
		desired_caps={
		'platformName':'android',
		'deviceName':'KR99LF9SO7HUZP4L',
		'platformVersion':'4.2.2',
		#apk package name
		'appPackage':'com.haokukeji.coolfood.debug',
		'appActivity':'com.haokukeji.coolfood.activities.LaunchActivity',
		#输入中文
		# 'unicodeKeyboard':True,
		# 'resetKeyboard':True
		}
		driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
	def  testlogin(self):
		
		#休眠3秒等待页面加载完成
		time.sleep(3)
		driver.find_element_by_name(u'幸福早餐').click()
		driver.find_element_by_name(u'我的').click()
		driver.find_element_by_name(u'请点击登录').click()
		driver.find_element_by_xpath('''//android.widget.EditText[@text=\"请输入您的手机号\"]''').clear()
		driver.find_element_by_xpath('''//android.widget.EditText[@text=\"请输入您的手机号\"]''').send_keys(u'13138153397')
		driver.find_element_by_xpath('''//android.widget.EditText[@text=\"获取验证码\"]''').click()
		driver.find_element_by_xpath('''//android.widget.EditText[@text=\"请输入短信验证码\"]''').clear()
		driver.find_element_by_xpath('''//android.widget.EditText[@text=\"请输入短信验证码\"]''').send_keys(u'123456')
		driver.find_element_by_xpath('''//android.widget.Button[@text=\"登录\"]''').click()
		 
		try:
			text=driver.find_element_name(u'幸福早餐，幸福从早餐开始！').text
			time.sleep(2)
			print text
			print u'登录成功！！！'
			
		except Exception as e:
			print e
			print u'登录失败！！！'

	def tearDown(self):
		
		# driver.close()
		# driver.quit()
		pass


if __name__=='__main__':
	testsuite=unittest.TestSuite()
	testsuite.addTest(testlogin('testlogin'))

	now=time.strftime('%Y-%m-%d %H_%M_%S')
	filename=r'D:\\appReport\\testscript'+now+'result.html'
	fp=open(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
	runner.run(testsuite)
	fp.close()
