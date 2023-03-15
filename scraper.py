import time
import csv
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedrive_win32/chromedriver.exe")
browser.get(start_url)
time.sleep(10)

def scrape():
    header=["name", "distance", "mass", "radius"]
    planet_data = []
    for i in range(0, 97):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for th_tag in soup.find_all("th", attrs={"class", "headerSort"}):
            tr_tags = th_tag.find_all("tr")
            temp_list = []
            for index, tr_tag in enumerate(tr_tags):
                if index==0:
                    temp_list.append(tr_tag.find_all("a")[0].contents(0))
                else:
                    try:
                        temp_list.append(tr_tag.content[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        #browser.find_element_by_xpath('NOT APPLICABLE (There is no x-path.)').click()
    with open("scraper.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(planet_data)

scrape()