from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

#Scraping article titles, descriptions, and links
#returns object carrying title, description and link
def scrape_article():
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless = True)
    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    news_array = []

    div_content = soup.find_all('div', class_='list_text')
    for item in div_content:
        news_article = {
            "title": item.find('a').text,
            "description": item.find('div', class_='article_teaser_body').text,
            "link": "https://mars.nasa.gov" + item.find('a').get('href')
        }

        news_array.append(news_article)

    return news_array

# using splinter to scrape images
# returns link to the featured object
def splinter_scrape_img():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless = True)
    target_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=mars"

    browser.visit(target_url)
    button = browser.find_by_id('full_image')
    button.click()

    soup1 = bs(browser.html, "html.parser")
    soup1.prettify()

    featured_img_link = 'https://www.jpl.nasa.gov' + soup1.find('a', class_='button').get('data-fancybox-href')

    return featured_img_link

# scraping twitter for weather reports
# returns list of the lastest weather tweets
def weather_scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless = True)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    soup = bs(browser.html, "html.parser")
    soup.prettify()

    weather_tweets = soup.find_all("p", class_="TweetTextSize")
    weather_tweets

    current_weather = []
    for tweet in weather_tweets:
        if (tweet.text[0:3] == "Sol"):
            current_weather.append(tweet.text)


    return current_weather


# End of function definitions
