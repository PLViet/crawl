import asyncio
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


async def create_driver():
    firefox_options = Options()
    firefox_options.headless = False
    return webdriver.Firefox(options=firefox_options) 

async def start():
    driver = await create_driver()

    driver.get("https://www.facebook.com/hunggcom003/posts/pfbid02k8L3HbD9z3KrYWFhHd9DZU7WWM8e8UpF3k9g7UsuDuStj9Djq2koCXnvTRC4dRskl")
    await asyncio.sleep(4)
    name_page = driver.find_element(By.XPATH, '//*[@data-ad-rendering-role="profile_name"]/h3/span/span/a/strong/span').text
    title = driver.find_element(By.XPATH, '//*[@data-ad-comet-preview="message"]').text
    image = driver.find_element(By.XPATH, '//*[@id="«r5»"]/div[1]/a/div[1]/div/div/div/img').get_attribute('src')
    print("""
    name_page: {}
    title: {}
    image: {}
    """.format(name_page, title, image))

if __name__ == '__main__':
    asyncio.run(start())
