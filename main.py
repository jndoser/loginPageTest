import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#Tạo class test, kế thừa class TestCase
#của thư viện unittest để tiến hành
#viết các testcase
class Test(unittest.TestCase):
    #phương thức setUp này sẽ được gọi đầu tiên
    #khi khởi chạy testcase, nên ta sẽ tạo driver
    #cho selenium để có thể mở trình duyệt của
    #chúng ta lên
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'E:/selenium/loginPageTest/geckodriver.exe')

    #testcase đầu tiên là xét trường hợp
    #cả 2 username và password đều đúng
    def test_login_1true_true(self):
        #tiến hành mở trang login đã tạo từ trc,
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        #lần lượt tìm 2 ô nhập username và password, sau đó
        #tiến hành nhập
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username01')
        #tạm dừng 2 giây để ta nhìn thấy kết quả của chương trình
        time.sleep(2)
        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password')
        time.sleep(2)
        #chụp lại màn hình của trang web để tiện kiểm tra sau này
        self.driver.save_screenshot("true_true.png")
        #tìm nút đăng nhập sau đó click vào
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        time.sleep(2)
        #sau khi click vào nút đăng nhập thì
        #trang web sẽ hiển thị lên tb alert
        #về kết quả đăng nhập là đúng hay sai,
        #nếu đúng thì sẽ hiển thị lên ok, ko thì là fail
        result = self.driver.switch_to.alert.text;
        #sử dụng phương thức assertEqual để so sánh
        #kết quả thu đc với kết quả ta mong đợi xem
        #có khớp ko, nếu có thì testcase pass
        #ko thì sẽ có tb là fail test
        self.assertEqual(result, 'ok', 'fail test')

    #testcase thứ 2 thử nghiệm nhập cả
    #username và password đều sai
    def test_login_2false_false(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username02')
        time.sleep(2)

        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password01')
        time.sleep(2)

        self.driver.save_screenshot("false_false.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        time.sleep(2)

        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    #testcase thứ 3 thử nghiệm nhập
    #username đúng và password sai
    def test_login_3true_false(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username01')
        time.sleep(2)

        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password01')
        time.sleep(2)

        self.driver.save_screenshot("true_false.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        time.sleep(2)

        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    #testcase cuối cùng thử nghiệm nhập
    #vào username sai và password đúng
    def test_login_4false_true(self):
        self.driver.get('file:///E:/selenium/loginPageTest/loginpage.html')
        username = self.driver.find_element_by_id('uname')
        username.send_keys('username02')
        time.sleep(2)

        psw = self.driver.find_element_by_id('psw')
        psw.send_keys('password')
        time.sleep(2)

        self.driver.save_screenshot("false_true.png")
        submit = self.driver.find_element_by_tag_name('button')
        submit.click()
        time.sleep(2)

        result = self.driver.switch_to.alert.text;
        self.assertEqual(result, 'ok', 'fail test')

    #phương thức tearDown sẽ được gọi sau mỗi testcase
    #nên ta gọi phương thức quit để thoát trình duyệt sau
    #mỗi test case
    def tearDown(self):
        self.driver.quit()

#tiến hành chạy testcase
if __name__ == "__main__":
    unittest.main()
