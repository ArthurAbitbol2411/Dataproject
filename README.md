The goal of my project is to create a dataset that examines the relationship between movie features and box office performance. 
Combining data from The Movie Database (TMDb) API with box office revenue data scraped from Mojo Box office allows to identify the relation between a movie's particularities and the box office revenue
The TMDb API was used to gather some informations on the movie, such as the popularity, reviews and movie overview.
The Mojo Box office website was scraped to find the movies with the top 20 box office revenue. (It can also be used to extract the box office revenue from different categories of movie, not just only the 2024 top 20, to drive deeper research and gain more insights)
I then combined both dataframes to create a new, unique dataset with both data. 
The next step for me would be to plot graphs to identify easily some correlations, for which I will need to clean the Mojo Box Office data for revenue as it is currently strings and not integers. I would also be interested in creating this dataset for other categories of movies to see if some relations are observable everywhere.
