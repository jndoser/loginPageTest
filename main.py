import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'E:/selenium/geckodriver.exe')

    def test_login_true_true(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username01')
        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password')
        self.driver.save_screenshot("true_true.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    def test_login_false_false(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username02')
        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password01')
        self.driver.save_screenshot("false_false.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    def test_login_true_false(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username01')
        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password01')
        self.driver.save_screenshot("true_false.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    def test_login_false_true(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username02')
        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password')
        self.driver.save_screenshot("false_true.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    def test_fb_login(self):
        self.driver.set_window_size(700, 700)

        self.driver.get('https://www.facebook.com/login')
        time.sleep(3)
        self.driver.find_element_by_id('email').send_keys('')
        self.time.sleep(2)
        self.driver.find_element_by_id('pass').send_keys('')
        time.sleep(2)
        self.driver.find_element_by_name('login').click()
        time.sleep(4)
        self.driver.get('https://www.facebook.com/Utc2Confessions')
        time.sleep(3)
        self.driver.execute_script('document.querySelector(".j83agx80.taijpn5t.c4xchbtz.by2jbhx6.a0jftqn4").click()')
        time.sleep(4)
        self.driver.execute_script('window.scroll(0,3300)')
        time.sleep(3)

        input()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
