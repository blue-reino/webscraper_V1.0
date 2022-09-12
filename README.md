# webscraper_V1.0 by: Devin Reino
Shitty ass web scraper that took way too long to make. Only capable of scraping limited data off imdb's top 250 movies. 

# how to work
All you got to do is install all the required libraries if you haven't already
Run the program in your compiler
A CSV file will be saved with the data collected
It will give you an output message that it has been completed

# how it works (shitty explanation)
Access the URL
Parses the information to lxml
Gets the table where the information we want to scrape is stored
Then a new data frame is created with the layout we will be storing our information
A for loop loops over the table and looks for all rows
In the loop we get all our columns and hyper link
We use an if statement to collect our required information, then assign them to the dataframe
Lasty I save that dataframe to a CSV file


