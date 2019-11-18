from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 平台
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取
DEVICE_NAME = 'TRT_AL00A'

# APP包名
APP_PACKAGE = 'cn.dps03.live'

# 入口类名
APP_ACTIVITY = 'com.fan.fan.activity.InitActivity'

# Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
# 等待元素加载时间
TIMEOUT = 300

# 滑动点
FLICK_START_X = 355
FLICK_START_Y = 1176
FLICK_DISTANCE = 1000

# 滑动间隔
SCROLL_SLEEP_TIME = 1


class MuaLive():
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            "noReset": "true",
            "autoAcceptAlerts": "true"
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def crawl(self):
        """
        爬取
        :return:
        """
        # 点击跳过广告
        a = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, 'cn.dps03.live:id/tv_count_down')))
        a.click()
        # 点击关闭广告
        b = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, 'cn.dps03.live:id/btn_know')))
        b.click()
        # 点击主播页面
        try:
           #cn.dps03.live:id/iv_room_image
            self.driver.tap([(362,777),(718,1098)], 500)
            sleep(10)
        except Exception as err:
            self.driver.tap([(362, 777), (718, 1098)], 500)
        # 点击一次屏幕，确保页面的展示
        self.driver.tap([(0,209), (720,1098)], 5000)

        while True:
            '''
            #等待页面加载，判断页面加载是否完成，设置等待时间16秒，每隔0.5秒查询一次，抛出异常
            WebDriverWait(self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, 'cn.dps05.live:id/iv_creater'))), timeout=20, poll_frequency=0.5, ignored_exceptions=None)
            '''
            #获取页面信息
            source = self.driver.page_source
            if '主播累了，休息好了再来直播' in source:
                print('主播下播，稍后片刻，切换到其他主播频道')
                c = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/iv_creater')))
                c.click()
            elif 'cn.dps03.live:id/ll_click_creater' in source:
                # 获取当前在线人数
                tv_viewer_number = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/tv_viewer_number')))
                tv_viewer_number = tv_viewer_number.get_attribute('text')
                # print(tv_viewer_number)
                #d点击直播信息
                c = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/ll_click_creater')))
                c.click()
                sleep(3)
                #获取主播名
                nick_name = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/tv_nick_name')))
                nick_name=nick_name.get_attribute('text')
                #print(nick_name)
                #获取房间ID
                tv_number = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/tv_number')))
                tv_number=tv_number.get_attribute('text')
                # print(tv_number)
                #获取粉丝数量
                tv_fans = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/tv_fans')))
                tv_fans=tv_fans.get_attribute('text')
                #print(tv_fans)
               # 获取地点
                tv_city = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, 'cn.dps03.live:id/tv_city')))
                tv_city = tv_city.get_attribute('text')
                # print(tv_city)
                # # 获取榜单
                # tv_ticket = self.wait.until(
                #     EC.element_to_be_clickable(
                #         (By.ID, 'cn.dps03.live:id/tv_ticket')))
                # tv_ticket = tv_ticket.get_attribute('text')

                data = str(nick_name) + "," + str(tv_number) + ',' + str(tv_fans)+','+str(tv_viewer_number)+','+str(tv_city)
                f = open('room.txt', 'a', encoding="utf-8")
                f.write(data + "\n")
                f.close()
                print(data)
               # print(tv_ticket)

                # #截屏操作
                # self.driver.get_screenshot_as_file('E:\\www\\mua_live_spider\\img\\{}.png'.format(str(tv_number)))
                # sleep(1)
                # 点击叉号，关闭主播信息
                try:
                    self.driver.tap([(560, 270), (600, 310)], 500)
                except Exception as err:
                    sleep(1)
                    self.driver.tap([(560, 270), (600, 310)], 500)

                # 上滑
                try:
                    self.driver.swipe(FLICK_START_X, FLICK_START_Y , FLICK_START_X, FLICK_START_Y-FLICK_DISTANCE)
                except Exception as err:
                    sleep(1)
                    self.driver.swipe(FLICK_START_X, FLICK_START_Y, FLICK_START_X, FLICK_START_Y - FLICK_DISTANCE)
            # else:
            #     # 上滑
            #     print('出现主播无直播状态，无法获取元素，执行滑屏操作，进入下一个直播间')
            #     try:
            #         self.driver.swipe(FLICK_START_X, FLICK_START_Y, FLICK_START_X, FLICK_START_Y - FLICK_DISTANCE)
            #     except Exception as err:
            #         sleep(1)
            #         self.driver.swipe(FLICK_START_X, FLICK_START_Y, FLICK_START_X, FLICK_START_Y - FLICK_DISTANCE)

    def start(self):
        """
        入口
        """
        self.crawl()


if __name__ == '__main__':
    mua_live = MuaLive()
    mua_live.start()
