

'''

By:SKP

'''


from splinter.browser import Browser
from time import sleep
import traceback
import time,sys
import os
class HuoChe(object):
    """docstring for Train"""

    driver_name = 'chrome'
    executable_path = 'C:\Program Files (x86)\Google\Chrome\Application'      #server


    # 用户名 密码
    username = u"****@qq.com"   #写上你的用户名邮箱什么的
    passwd = u"**********"      #写上你的密码

    # cookies值自己找
    # 天津%u5929%u6D25%2CTJP 南昌%u5357%u660C%2CNCG 桂林%u6842%u6797%2CGLZ
    starts = u"%u5357%u5B81%u4E1C%2CNFZ	"       #从哪里来
    ends = u"%u957F%u6C99%u5357%2CCWQ"          #到哪里去


    # 时间格式2018-02-05
    dtime = "2018-04-18"

    # 车次,选择第几趟,0则从上之下依次点击
    order = 3

    ###乘客姓名
    users =[u'***']   #谁要坐火车


    ##席位
    xb = u"二等座"
    pz = u"成人票"



    """网址"""
    # 12306查询URL
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"


    # 12306登录URL
    login_url = "https://kyfw.12306.cn/otn/login/init"


    # 我的12306URL
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

    # 购票URL
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    login_url = 'https://kyfw.12306.cn/otn/login/init'

    def __init__(self):
        self.driver_name = 'chrome'
        self.executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        print("Welcome To Use The Tool")

    def login(self):
        self.driver.visit(self.login_url)
        # 填充密码
        self.driver.fill("loginUserDTO.user_name" ,self.username)
        # sleep(1)
        self.driver.fill("userDTO.password" ,self.passwd)
        print("等待验证码，自行输入....")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else :
                break
    def start(self):
        self.driver = Browser(driver_name=self.driver_name ,executable_path = self.executable_path)
        self.driver.driver.set_window_size(1400 ,1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print("购票页面开始....")
            # sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation" :self.starts})
            self.driver.cookies.add({"_jc_save_toStation" :self.ends})
            self.driver.cookies.add({"_jc_save_fromDate" :self.dtime})

            self.driver.reload()

            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print("循环点击查询.... 第 %s 次 " %count)
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u'预定')[self.order - 1].click()
                    except Exception as e:
                        print(e)
                        print("还没开始预订")
                        continue
            else :
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print("循环点击查询.... 第 %s 次 " %count)
                    # sleep(0.8)
                    try:
                        for i in self.driver.find_by_text(u"预定"):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print("还没开始预订 %s  " %count)
                        continue
            print("开始预订....")
            # sleep(1)
            # self.driver.reload()
            sleep(1)
            print("开始选择用户....")
            for user in self.users:
                self.driver.find_by_text(user).last.click()
            print("提交订单....")
            sleep(1)
            # self.driver.find_by_text(self.pz).click()
            # self.driver.find_by_id('').select(self.pz)
            # sleep(1)
            # self.driver.find_by_text(self.xb).click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            print("开始选座...")
            # self.driver.find_by_id('1D').last.click()
            # self.driver.find_by_id('1F').last.click()
            sleep(1.5)
            print("确认选座....")
            self.driver.find_by_text('qr_submit_id').click()

        except Exception as e:
            print(e)

#一个小例子
cities = {
    '南宁东':'%u5357%u5B81%u4E1C%2CNFZ',
    '长沙南':'%u957F%u6C99%u5357%2CCWQ'
}
if __name__ == "__main__":
    train = HuoChe()
    train.starts = cities['南宁东']
    train.ends = cities['长沙南']
    train.dtime = '2018-04-18'
    train.start()
