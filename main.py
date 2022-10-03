# Import requests and soup to scrape the internet
import requests
import bs4


def get_keyword():
    # Get keyword function
    keyword = str(input("What crypto are we looking for: "))
    return keyword


def url_request(keyword):
    # Requesting our url and souping it :)
    url = 'https://news.search.yahoo.com/search?q={}&b=1'.format(keyword)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup


def print_articles():
    # Prints our articles
    print('\n')
    print('Title: ' + news_title)
    print('Source: ' + news_source)
    print(news_desc)
    print(news_link)
    print(news_time)


while True:

    keyword = get_keyword()
    soup = url_request(keyword)

# Define the parts we want from the news article and iterate over the page with a for loop
    for news_article in soup.find_all('div', class_='NewsArticle'):
        news_title = news_article.find('h4').text
        news_desc = news_article.find('p', class_='s-desc').text
        news_source = news_article.find('span', class_='s-source').text
        news_time = news_article.find('span', class_='fc-2nd').text
        news_link = news_article.find('a').get('href')
        # Let's clean up the text a bit
        news_time = news_time.replace('·', '').strip()
        # Then display the articles
        print_articles()
    # Offer the chance to search again
    search = input('\nWould you like to search again? \ny or n: ')

    if search == 'y':
        # I print 80 new line to clear the old code from the screen
        print('\n' * 80)
        continue
    else:
        break


