
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

# URL
Youtube = 'https://www.youtube.com/'
WebWhatsapp = 'https://web.whatsapp.com/'
Twitter = 'https://twitter.com/?lang=es'
Platzi = 'https://platzi.com/'
Gmail = 'https://gmail.com'
Instagram = 'https://www.instagram.com/'
GitHub = 'https://github.com/'
Linkedin = 'https://www.linkedin.com/'
Google = 'https://www.google.com/'

# Youtube
driver.get(Youtube)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

# WebWhatsapp
driver.get(WebWhatsapp)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])

# Twitter
driver.get(Twitter)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])

# Platzi
driver.get(Platzi)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])

# Gmail
driver.get(Gmail)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[5])

# Instagram
driver.get(Instagram)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[6])

# GitHub
driver.get(GitHub)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[7])

# Linkedin
driver.get(Linkedin)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[8])

# Google
driver.get(Google)

