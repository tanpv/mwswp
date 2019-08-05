---
layout: default
---

### Scrape Data from Tag

Congratulations, so you come to the final step. And at this step we will harvest out result.

For easy of demo, let continue using the following soup.

```python
# import beautifulsoup object
from bs4 import BeautifulSoup

# predefine a html content
html = """
<html>
<head>
	<title>The Dormouse's story</title>
</head>
<body>
	<p class="title">
		<b>The Dormouse's story</b>
	</p>
	<p class="story">
		Once upon a time there were three little sisters. And their names were
		<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom of a well.
	</p>
	<p class="story">...</p>
/</body>
</html>
"""
# create soup object by HTML content
soup = BeautifulSoup(html, 'lxml')
```

#### Scrape for text

To scrape the text inside a tag we just need to use grammar `tagname.text`

As following code example

```python
p = soup.find('p')
print(p.text)
```

will return result

```python
"""
The Dormouse's story
"""
```



#### Scrape for link

To scrape the link inside `a` tag, we just need to access attribute `href` 

Following code will print out all link inside a tags.

```python
a_tags = soup.find_all('a')
for a in a_tags:
	print(a['href'])
```

And we have result

```python
"""
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
"""
```



