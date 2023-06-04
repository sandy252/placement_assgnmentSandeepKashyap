import requests
import pandas as pd
import openpyxl

# API link
api_link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send GET request to the API
response = requests.get(api_link)
data = response.json()

# Extracting data attributes
episodes = data['_embedded']['episodes']

# Create a list to store the extracted data
formatted_data = []

for episode in episodes:
    episode_data = {
        'id': episode['id'],
        'url': episode['url'],
        'name': episode['name'],
        'season': episode['season'],
        'number': episode['number'],
        'type': episode['type'],
        'airdate': episode['airdate'],
        'airtime': episode['airtime'],
        'runtime': episode['runtime'],
        'average rating': episode['rating']['average'],
        'summary': episode['summary'],
        'medium image link': episode['image']['medium'],
        'original image link': episode['image']['original']
    }
    formatted_data.append(episode_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(formatted_data)

# Remove HTML tags from the 'summary' column
df['summary'] = df['summary'].str.replace('<[^<]+?>', '', regex=True)

# Save the DataFrame to Excel
output_file = 'episodes_data.xlsx'
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file} successfully.")
