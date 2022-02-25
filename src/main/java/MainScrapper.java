import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class MainScrapper {
    public static void main(String[] args) {
        final String url = "https://scrolller.com/r/cats?sort=top&filter=pictures";

        try {
            WebClient webClient = new WebClient();
            HtmlPage myPage = webClient.getPage(new File("page.html").toURI().toURL());

            Connection con = Jsoup.connect(url);
            TimeUnit.SECONDS.sleep(5);
            Document doc = con.timeout(5000).get();

            System.out.println(doc.outerHtml());
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
