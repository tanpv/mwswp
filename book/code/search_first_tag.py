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

		<p class="story">Once upon a time there were three little sisters. And their names were
			<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
			<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
			<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
			and they lived at the bottom of a well.
		</p>

		<p class="story">...</p>

	</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

first_p_tag = soup.find('p')
print(first_p_tag)
