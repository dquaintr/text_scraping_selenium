from selenium import webdriver
from selenium.webdriver.common.by import By



#set options to make browsing easier

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")


  driver = webdriver.Chrome(options=options)
  driver.get("https://linguistics.illinois.edu/hindi/about-hindi")
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(by=By.XPATH, value="//*[@id='block-framework-las-unit-theme-content']/article/div/div/div/div/div/div/div/div/div/div/div/div/div/p[12]")   #("/html/body/div[1]/div/h1[1]")
  return element.text


print(main())
