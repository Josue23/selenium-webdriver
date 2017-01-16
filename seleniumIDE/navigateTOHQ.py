# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NavigateTOHQ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.udemy.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_navigate_t_o_h_q(self):
        driver = self.driver
        driver.get(self.base_url + "/selenium-webdriver-with-python/learn/v4/t/lecture/1279182")
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_link_text("Download").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        self.assertEqual("Downloads", driver.title)
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_link_text("Documentation").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("webdriver")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        driver.find_element_by_id("js-video-player_1550282_86867974_html5_api").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*$")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
