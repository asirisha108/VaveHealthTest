import os
import unittest
from appium import webdriver
import time


class IonicAndroidTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps['platformName'] = 'android'
        caps['app'] = os.path.abspath('platforms/android/build/outputs/apk/android-debug.apk')
        caps['deviceName'] = 'emulator-5554'
        caps['platformVersion'] = '7.1.1'
        caps['automationname'] = 'uiautomator2'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_tab_navigation(self):
        time.sleep(2)

        ctxts = self.driver.contexts
        for c in ctxts:
            if 'WEBVIEW' in c:
                self.driver.switch_to.context(c)
        # Goto About page at tab 1
        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-0"]')
        el.click()

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-0"]')
        self.assertTrue(el.is_displayed())

        time.sleep(1)

        # Goto About page at tab 2
        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-1"]')
        el.click()

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]')
        self.assertTrue(el.is_displayed())

        time.sleep(1)

        # Goto About page at tab 3
        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-2"]')
        el.click()

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-2"]')
        self.assertTrue(el.is_displayed())

        time.sleep(1)

    def test_button_press(self):
        time.sleep(2)

        ctxts = self.driver.contexts
        for c in ctxts:
            if 'WEBVIEW' in c:
                self.driver.switch_to.context(c)
        # Goto About page at tab 1
        el = self.driver.find_element_by_xpath('//*[@id="tab-t0-1"]')
        el.click()

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]')
        self.assertTrue(el.is_displayed())

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]/page-about/ion-content/div[2]/p')
        self.assertEqual(el.text, 'This is a sample text area to demonstrate ability to add test area.')

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]/page-about/ion-content/div[2]/ion-list/ion-item[1]/div[1]/div/ion-input/input')
        el.send_keys('Test First')
        time.sleep(2)
        
        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]/page-about/ion-content/div[2]/ion-list/ion-item[2]/div[1]/div/ion-input/input')
        el.send_keys('Test Last')
        time.sleep(2)

        el = self.driver.find_element_by_xpath('//*[@id="tabpanel-t0-1"]/page-about/ion-content/div[2]/ion-list/ion-item[3]/div[1]/div/ion-label/button')
        self.assertEqual('SUBMIT',el.text)
        el.click()

        time.sleep(1)

        # Alert 
        el = self.driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[1]')
        self.assertEqual('Custom Alert',el.text)

        # Alert OK button
        el = self.driver.find_element_by_xpath('/html/body/ion-app/ion-alert/div/div[3]/button')
        el.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IonicAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
