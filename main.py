# coding = utf-8
from selenium import webdriver
from time import sleep
import random
import json

from selenium.webdriver import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SyntheticWatermelon(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", {'deviceName': 'iPhone 6'})
        options.add_argument("Access-Control-Allow-Origin:*")

        capabilities = DesiredCapabilities.CHROME
        capabilities['loggingPrefs'] = {'browser': 'ALL'}

        self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
        self.driver.get("http://localhost:5000")
        self.driver.implicitly_wait(3)


    def run(self):
        prevGameScore = int(0)
        gameScore = int(0)
        fruitType = int(0)
        while gameScore < 1000:
            if gameScore > prevGameScore:
                prevGameScore = gameScore
                print("final gameScore:" + str(gameScore))
            x_pos = 360
            y_pos = 200
            ActionChains(self.driver).move_by_offset(x_pos, y_pos).click().perform()
            ActionChains(self.driver).move_by_offset(-x_pos, -y_pos).perform()

            result = [-1, 0, 0] # fruitType、currentScore、gameScore
            self.parseLog(result)
            sleep(.001)
            # if result[0] != -1:
            print(result)

    # 解析一场游戏的各种指标
    def parseLog(self, result=[]):
        for entry in self.driver.get_log('browser'):
            if (entry.__contains__("message")):
                message = entry.get("message")
                if any([message.__contains__("gameScore"),
                        message.__contains__("fruitType"),
                        message.__contains__("currentScore")]):
                    return self._parseLog(message, result)

    def _parseLog(self, consoleMessage, result=[]):
        split = consoleMessage.split()
        if split.__len__() == 3:
            if split[2].__contains__("fruitType"):
                strip = split[2].strip("\"")
                strip_split = strip.split(":")
                if strip_split.__len__() == 2:
                    result[0] = int(strip_split[1])
            elif split[2].__contains__("currentScore"):
                strip = split[2].strip("\"")
                strip_split = strip.split(":")
                if strip_split.__len__() == 2:
                    result[1] = int(strip_split[1])
            elif split[2].__contains__("gameScore"):
                strip = split[2].strip("\"")
                strip_split = strip.split(":")
                if strip_split.__len__() == 2:
                    result[2] = int(strip_split[1])



syntheticWatermelon = SyntheticWatermelon()
syntheticWatermelon.run()
