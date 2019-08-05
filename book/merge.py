filenames = ['the-big-picture.md',
'inspecting.md',
'download-html.md',
'create-soup-and-search.md',
'scrape-data-from-tag.md',
'project1-basketball-data-from-nba.md',
'project2-game-data-from-steam.md',
'project3-movie-data-from-imdb.md',
'project4-product-data-from-amazon.md'
 ]
with open('book.md', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
            	if ('---' not in line) and ('layout: default' not in line):
                	outfile.write(line)
