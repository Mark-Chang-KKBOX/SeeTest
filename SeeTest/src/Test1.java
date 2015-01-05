//package <set your test package>;
import com.experitest.client.*;
import org.junit.*;
/**
 *
 *
*/
public class Test1 {
    private String host = "localhost";
    private int port = 8889;
    private String projectBaseDirectory = "/Users/mac/workspace/project2";
    protected Client client = null;

    @Before
    public void setUp(){
        client = new Client(host, port, true);
        client.setProjectBaseDirectory(projectBaseDirectory);
        client.setReporter("xml", "reports", "Untitled");
    }

    @Test
    public void testUntitled(){
        client.setDevice("adb:SM-N900");
        client.elementSendText("NATIVE", "xpath=//*[@text and @class='android.widget.EditText']", 0, "company");
        if(client.waitForElement("NATIVE", "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@class='android.widget.ScrollView']]/*/*[@class='android.widget.EditText'])[2]", 0, 10000)){
            // If statement
        }
        client.elementSendText("NATIVE", "xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@class='android.widget.ScrollView']]/*/*[@class='android.widget.EditText'])[2]", 0, "company");
        client.click("NATIVE", "xpath=//*[@text='Login']", 0, 1);
        client.click("NATIVE", "xpath=//*[@text='Logout']", 0, 1);
    }

    @After
    public void tearDown(){
        client.generateReport(true);
    }
}
