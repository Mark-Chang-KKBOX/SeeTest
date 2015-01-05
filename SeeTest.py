import unittest, sys
sys.path.insert(0, "/Applications/SeeTest/clients/Python/")
from ExperitestClient import Client
from ExperitestClient import Configuration

class SeeTest(unittest.TestCase):
    def setUp(self):
        self.host = "localhost"
        self.port = 8889
        self.client = Client()
        self.client.init(self.host, self.port, True)
        self.client.setProjectBaseDirectory("/Users/mac/workspace/project2")
        self.client.setReporter2("xml", "reports", "SeeTest")

    def testSeeTest(self):
        self.client.setDevice("adb:SM-N900")
        self.client.elementSendText("NATIVE", "xpath=//*[@text and @class='android.widget.EditText']", 0, "company")
        if(self.client.waitForElement("NATIVE", "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@class='android.widget.ScrollView']]/*/*[@class='android.widget.EditText'])[2]", 0, 10000)):
                # If statement
                pass
        self.client.elementSendText("NATIVE", "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@class='android.widget.ScrollView']]/*/*[@class='android.widget.EditText'])[2]", 0, "company")
        self.client.click("NATIVE", "xpath=//*[@text='Login']", 0, 1)
        self.client.click("NATIVE", "xpath=//*[@text='Logout']", 0, 1)

    def tearDown(self):
        self.client.generateReport2(True)

if __name__ == '__main__':
    unittest.main()


