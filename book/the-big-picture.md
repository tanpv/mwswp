---
layout: default
---

### The Big Picture : Scrape any Website in 4 Steps

![](images/big_picture.png)

What are common steps which you need to do for all web scraping tasks ?

**Inspecting** : Mean understand where your data located inside html page ? We use `chrome developer tool` to inspect what `tag` contain our wanted data.



**Download html** : We use `selenium` to download html.



**Search for Tag** : After have html content, we use `Beautiful Soup` to parse html. Then we search for `tag` which contain our data.



**Scrape data** : Final step is scraping data from `tag` and store it to file  or database.



### Selenium

We use <a href="https://www.seleniumhq.org/" target="_blank">Selenium</a> to control browser and download HTML content. 

Why not just use simple library like requests to download HTML content ?. 

Have 2 reasons:

* Many modern web page use a lot of JavaScript for dynamic HTML render, requests package could not render HTML from JavaScript.
* In some web pages, in order access wanted data, we need to do actions like : login, click link to navigate. Selenium can do that perfectly.



### Beautiful Soup

We need [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse HTML in to object. Beautiful Soup provide functions help us to search HTML tags inside HTML object. After have HTML tags, final step just about access wanted data and save.
