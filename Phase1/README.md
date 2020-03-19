# cs105-prj-phase1-mvb

In this phase, our team crawled basketball-reference.com in order to retrieve data that we will use to analyze and find trends in multiple aspects of the NBA. This includes finding trends in teams that won championships, finding how the game changed overall, and comparing stats amongst individuals to see how players generally change as they continue to develop. Our analysis will include current and past players. Other analysis from other team members also include looking at specific head coaches and their influence on teams over the years.

We used beautiful soup to gather information about successful teams, stats of everyplayer in the NBA from 1950-2018 season, 1950-2018 season coaching stats, and other useful information around the NBA.

Our team did use Jupyter's Notebook to run our code, as our process was to gather the data, turn the text into a dataframe, and then retreive a csv file from that dataframe. Thus to running our code can be done through Jupyter's Notebook.

Our group used beautifulsoup's functions to scrap and crawl data from multiple webpages, around 69 web pages scraped per person. To first access the html code from the website, we import urlopen from the urllib.request library. This is used to access the raw html code and store it in a python variable. Using the raw code, we pass it into BeautifulSoup in order to parse through the raw html code. We utilize the function findAll(), which we can pass in a specific html element, and it will store all the elements of that type. We then use .getText() in order to pull out the actual text on the webpage that is a part of the html element we parsed for. The website we used uses html tables to store the data, so we can easily parse for html table elements in order to parse the data. After parsing and storing specific data from the tables columns, as well as the headers for the columns, we create a data frame using pandas, and use the .to_csv() function in order to create a csv from the data frame we just built.