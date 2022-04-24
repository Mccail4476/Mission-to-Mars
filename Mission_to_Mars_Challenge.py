#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from splinter import Browser


# In[ ]:


from bs4 import BeautifulSoup as soup


# In[ ]:


from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[ ]:


# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[ ]:


# Scrape the Title
title = html_soup.find('h2').text
title


# In[ ]:


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)


# In[ ]:


url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[ ]:


for x in range(1, 6):
   html = browser.html
   quote_soup = soup(html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.links.find_by_partial_text('Next').click()


# In[ ]:





# In[ ]:





# In[ ]:


#MISSION_TO_MARS_ipynb


# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:


browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:


#Challenge code


# In[ ]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[ ]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[ ]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[ ]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 

# ### Hemispheres

# In[7]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[8]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[10]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Parse the HTML
#html = browser.html
#html_soup = soup(html, 'html.parser')
#slide_elem = html_soup.select_one('div', class_='item')

# Find and click the full image button
#full_image_elem = browser.find_by_tag('img')[1]
#full_image_elem.click()
for page in range(4):
    #creating a list to store title and urls
    hemisphere = {}
    #selecting each hemisphere from main page
    browser.find_by_css('a.product-item h3')[page].click()
    #grabbing url of full-resolution image
    element = browser.find_link_by_text('Sample')
    img_url = element["href"]
    #grabbing title for each image
    title = browser.find_by_css("h2.title").text
    hemisphere["img_url"] = img_url
    hemisphere["title"] = title
    #adding it to the list
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[11]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[12]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




