from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located, visibility_of_element_located
from selenium.webdriver.chrome.options import Options

# LOG INTO THE TEAMS FROM CHROME WITH YOUR ID BEFORE TESTING.

opt = webdriver.ChromeOptions()
opt.add_argument("user-data-dir=C:/Users/ASUS/AppData/Local/Google/Chrome/User Data/")
driver = webdriver.Chrome(options=opt)

driver.get("http://teams.microsoft.com")
driver.implicitly_wait(10)
li = driver.find_elements_by_class_name("match-parent")
print(len(li))
for i in li:
    i.click()
    i.find_element_by_class_name("channels")
    print("found")

assert "No results found." not in driver.page_source
# driver.close()

# ele.


# The class 'active-calls-counter' gets added under the respective team which is having a meeting rn. Teams are sorted in lists.
# To check for the 'active-calls-counter' class under any team, the team needs to be triggered first so that it adds the div block containing the req. class.
