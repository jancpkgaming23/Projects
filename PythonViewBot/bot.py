import time;
from selenium import webdriver;

#time to refresh page (minute)
Timer = 5

#youtube link
link = 'https://youtu.be/yiIsp1Yt8rY'

#number of views
views = 250.000

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
