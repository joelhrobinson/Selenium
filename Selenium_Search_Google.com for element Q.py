############################################
## JOEL: you need to set up the path variable first.  It cannot find the files 
# copy chromedriver.exe to d:\bin, then change system variable to include c:\bin
# the end
#############################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
element = 'SORRY!!!'
# open the the google web page
driver.get ('http://google.com')
element = driver.find_element_by_name('q'  )
element.send_keys('Python Selenium Commands')
print ('Found element "q"')
print (element    )

# simulate someone pressing the RETURN or enter key
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)
time.sleep (5)
print ('Searched Google for Python Selenium Commands')
print ('Note: page results will close unless you click on the window')

#for ii in ids:
    #print ii.tag_name
 #   print ids.get_attribute('id')    # id name as string

#find_elements_by_tag_name()
#find_elements_by_id()
#find_elements_by_css_selector()
#find_elements_by_xpath()