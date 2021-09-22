from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./Chrome/chromedriver.exe')
url = "https://www.google.com/"


driver.get(url)
search = driver.find_element_by_class_name('gb_f')
search.click()

# This does not change focus to the new window for the driver.
driver.execute_script("window.open('');")

# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")


#  https://www.youtube.com/watch?v=t_jkcK5-2jQ Observar Videoo
#  https://python-forum.io/thread-7530.html