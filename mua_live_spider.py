from appium import webdriver
from time import sleep
from utils import tools
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Action():
    def __init__(self):
        # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "TRT_AL00A",
            "appPackage": "cn.dps05.live",
            "appActivity": "com.fan.fan.activity.InitActivity",
            "noReset": "true",
            "autoAcceptAlerts": "true"

        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个Session
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        #打印出页面源码
        # print(self.driver.page_source)
        # print(self.driver.context)
        try:
            sleep(6)
            #模拟点击跳出广告
            self.driver.find_element_by_xpath("//*[@resource-id='cn.dps05.live:id/tv_count_down']").click()
        except Exception as err:
            sleep(6)
            self.driver.find_element_by_xpath("//*[@resource-id='cn.dps05.live:id/tv_count_down']").click()
        try:
            sleep(2)
            #模拟点击知道了页面
            self.driver.find_element_by_xpath('//*[@text="知道了"]').click()
        except Exception as err:
            sleep(2)
            self.driver.find_element_by_xpath('//*[@text="知道了"]').click()
        try:
            #点击主播页面
            self.driver.tap([(2, 775),(358, 1098)], 500)
            sleep(10)
        except Exception as err:
            # 点击主播页面
            self.driver.tap([(2, 775), (358, 1098)], 5000)

        self.driver.swipe(355, 1176, 100,1176-1000)

        # 点击一次屏幕，确保页面的展示

        self.driver.tap([(0, 48),(720, 1208)], 5000)

        self.start_x = 355
        self.start_y = 1176
        self.distance = 1000

    def scroll(self):
        # 无限滑动
        while True:

            # try:
            #     online_number=self.driver.find_element_by_xpath("//*[@resource-id='cn.dps05.live:id/tv_viewer_number']").get_attribute('text')
            # except Exception as err:
            #     online_number = self.driver.find_element_by_xpath(
            #         "//*[@resource-id='cn.dps05.live:id/tv_viewer_number']").get_attribute('text')
            # # 点击主播信息
            try:
                self.driver.find_element_by_xpath("//*[@resource-id='cn.dps05.live:id/ll_click_creater']").click()
                # self.driver.find_element_by_xpath("//*[@resource-id='cn.dps05.live:id/iv_head_image']").click()
                sleep(4)
            except Exception as err:
                continue

            try:
                nick_name = self.driver.find_element_by_xpath(
                    "//*[@resource-id='cn.dps05.live:id/tv_nick_name']").get_attribute('text')
            except Exception as err:
                sleep(2)
                nick_name = self.driver.find_element_by_xpath(
                    "//*[@resource-id='cn.dps05.live:id/tv_nick_name']").get_attribute('text')
            try:
                tv_number = self.driver.find_element_by_xpath(
                    "//*[@resource-id='cn.dps05.live:id/tv_number']").get_attribute('text')
            except Exception as err:
                sleep(2)
                tv_number = self.driver.find_element_by_xpath(
                    "//*[@resource-id='cn.dps05.live:id/tv_number']").get_attribute('text')
            try:
                tv_fans= self.driver.find_element_by_xpath(
                    "//*[@resource-id='cn.dps05.live:id/tv_fans']").get_attribute('text')
            except Exception as err:
                sleep(2)
                tv_fans = self.driver.find_element_by_xpath(
                    "//*[@resource-id='cn.dps05.live:id/tv_fans']").get_attribute('text')

            data=str(nick_name)+","+str(tv_number)+','+str(tv_fans)
            f = open('room.txt', 'a', encoding="utf-8")
            f.write(data + "\n")
            f.close()
            print(nick_name)
            print(tv_number)
            print(tv_fans)
            try:
                #点击叉号，关闭主播信息
                self.driver.tap([(560, 270), (600, 310)], 500)
            except Exception as err:
                sleep(1)
                self.driver.tap([(560, 270), (600, 310)], 500)

            try:
                sleep(4)
                # 模拟滑动
                self.driver.swipe(self.start_x, self.start_y, self.start_x,
                                  self.start_y - self.distance)
                self.driver.tap([(0, 48), (720, 1208)], 5000)
                # 设置延时等待
                sleep(4)
                try:
                    if '直播Live' not in str(self.driver.page_source):
                        continue
                except Exception as err:
                    print(err)


            except Exception as err:
                sleep(4)
                self.driver.swipe(self.start_x, self.start_y, self.start_x,
                                  self.start_y - self.distance)
                self.driver.tap([(0, 48), (720, 1208)], 5000)

    def main(self):
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()
