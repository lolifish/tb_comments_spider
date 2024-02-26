from DrissionPage import ChromiumPage
from time import sleep

page = ChromiumPage()
page.get("https://www.taobao.com/")
input("请登录...")

url = "https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&q=%E6%98%BE%E5%8D%A1&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ssid=s5-e"
page.get(url)

for i in range(1, 49):
    sleep(1)
    page.ele(f"xpath=//div[@class='Content--contentInner--QVTcU0M']/div[{i}]/a").click(by_js=True)
    sleep(0.5)

    page.wait.new_tab()
    new_tab = page.get_tab(0)
    new_tab.wait.load_start()
    print('\n', new_tab.title)
    new_tab.ele("xpath=//div/span[contains(text(),'宝贝评价')]").click(by_js=True)
    
    sleep(0.5)
    comments = new_tab.eles("xpath=//div[@class='Comments--comments--1662-Lt']/div/div/div[@class='Comment--content--15w7fKj']")
    for comment in comments:
        print(comment.text)
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(comment.text)
            f.write("\n")
    
    page.close_other_tabs()