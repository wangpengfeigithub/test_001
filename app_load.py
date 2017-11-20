#coding=utf-8
from appium import webdriver

desired_caps={
	'platformName':'Android',
	'deviceName':'Appium',
	'platformVersion':'4.2.2',
	'appPackage':'com.haokukeji.coolfood.debug',
	'appActivity':'com.haokukeji.coolfood.activities.LaunchActivity'
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)