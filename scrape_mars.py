# Jupyter Notebook Conversion to Python Script

from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

#Nasa News


def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    title = soup.find('div', class_="content_title").get_text()

    paragraph = soup.find('div', class_="article_teaser_body").get_text()

    image_url = "https://spaceimages-mars.com/"  
    browser.visit(image_url)


    button = browser.find_by_tag("button")[1]
    button.click()

    html = browser.html
    image_soup = bs(html, "html.parser")


    image = image_soup.find("img", class_="fancybox-image").get("src")
 
    # facts = pd.read_html("https://galaxyfacts-mars.com/")[0]
    # facts.reset_index(inplace=True)
    # facts.columns=["ID", "Properties", "Mars", "Earth"]


    facts = "abc"
    image = f"https://spaceimages-mars.com/{image}"
    mars_scraper_data = {
        "title": title,
        "paragraph": paragraph,
        "image": image,
        "facts": facts
    }

    browser.quit()

    # Return results
    return mars_scraper_data