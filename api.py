from __future__ import print_function
import selenium
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = './keys.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
books = []

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
# I have not added the spreadsheet id of my spreadsheet because anyone can access it, but if you want to see if the code works, you can contact me.
SAMPLE_SPREADSHEET_ID = ''

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A2:D22").execute()
#values = result.get('values', [])

print(result)
#print((result['values']))
for a in range(0,len((result['values']))):
    books.append((result['values'][a][2]))
chrome_options = Options()
#books = (input("Enter books names seperated by ',' : ").split(','))
mainlist = []
chrome_options.add_argument("--headless")
wd = webdriver.Chrome(options=chrome_options)
print(books)
def link():
    for a in (books):
        print(a)
        def fetch_image_urls(query: str, max_links_to_fetch: int, wd: wd, sleep_between_interactions: int = 1):
            def scroll_to_end(wd):
                wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # build the google query

            search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

            # load the page
            wd.get(search_url.format(q=query))

            image_urls = []
            image_count = 0
            results_start = 0
            scroll_to_end(wd)

            thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
            try:
                thumbnail_results[0].click()

                time.sleep(sleep_between_interactions)

                actual_images = wd.find_elements_by_css_selector('img.n3VNCb')[0]
                if actual_images.get_attribute('src') and 'http' in actual_images.get_attribute('src'):
                    image_urls.append(actual_images.get_attribute('src'))
                try:
                    mainlist.append(image_urls)
                except:
                    mainlist.append(["No image found"])
            except:

                mainlist.append(["No image found"])
                print("hello")

            return 0
        fetch_image_urls(a, 1, wd)
    wd.quit()
link()

print(mainlist)

request = sheet.values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID,
    range="Sheet1!G2",
    valueInputOption="USER_ENTERED",
    body={"values":mainlist}).execute()
