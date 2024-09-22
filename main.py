import requests
from bs4 import BeautifulSoup
import pandas as pd


API_KEY = "2b07c06174caa2fa2d44549c69f85108"

def scrape_table(url):
  
    response = requests.get(url)

   
    soup = BeautifulSoup(response.content, 'html.parser')

    
    table_div = soup.find('div', id='table')

    if not table_div:
        return "Table not found"

   
    rows = table_div.find_all('tr')

   
    headers = [th.text.strip() for th in rows[0].find_all('th')]

    
    data = []
    for row in rows[1:]:
        cells = row.find_all('td')
        data.append([cell.text.strip() for cell in cells])

    
    df = pd.DataFrame(data, columns=headers)

    return df


def get_movie_info(movie_name):
    
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

    
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])

        if results:
            
            movie = results[0]
            movie_info = {
                'Title': movie['title'],
                'Overview': movie['overview'],
                'Release Date': movie['release_date'],
                'Rating': movie['vote_average'],
                'Popularity': movie['popularity'],
                'Poster URL': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else "N/A"
            }
            return movie_info
        else:
            return f"No movie found with the name: {movie_name}"
    else:
        return f"Error: Unable to fetch data from TMDb (Status Code: {response.status_code})"


url = "https://www.boxofficemojo.com/year/world/2024/?ref_=bo_hm_yrww"
df = scrape_table(url)
df = df.head(20)

names = df["Release Group"]
newdf = {
  'Release Group': [],
  'Overview': [],
  'Release Date': [],
  'Rating': [],
  'Popularity': [],
  'Poster URL': [],
}

for name in names:
  details = get_movie_info(name)
  newdf["Release Group"].append(details["Title"])
  newdf["Overview"].append(details["Overview"])
  newdf["Release Date"].append(details["Release Date"])
  newdf["Rating"].append(details["Rating"])
  newdf["Popularity"].append(details["Popularity"])
  newdf["Poster URL"].append(details["Poster URL"])

df2 = pd.DataFrame(newdf)
df3 = pd.merge(df,df2,on="Release Group")
print(df3)
df3.to_csv("output.csv")