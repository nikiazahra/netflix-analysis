import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('netflix_titles.csv', encoding='latin1')

# Basic info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())

# Clean data
df.dropna(subset=['type', 'country', 'rating', 'listed_in'], inplace=True)

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Chart 1: Movies vs TV Shows
plt.figure()
df['type'].value_counts().plot(kind='bar', color=['#E50914', '#221F1F'])
plt.title('Movies vs TV Shows on Netflix', fontsize=16)
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart1_type.png')
plt.close()
print("Chart 1 saved")

# Chart 2: Top 10 Countries
plt.figure()
top_countries = df['country'].str.split(',').explode().str.strip()
top_countries.value_counts().head(10).plot(kind='barh', color='#E50914')
plt.title('Top 10 Countries Producing Netflix Content', fontsize=16)
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig('chart2_countries.png')
plt.close()
print("Chart 2 saved")

# Chart 3: Content Added Over Years
plt.figure()
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['year_added'].value_counts().sort_index().plot(kind='line',
    color='#E50914', marker='o')
plt.title('Netflix Content Added Over the Years', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Number of Titles Added')
plt.tight_layout()
plt.savefig('chart3_trend.png')
plt.close()
print("Chart 3 saved")

# Chart 4: Top 10 Genres
plt.figure()
genres = df['listed_in'].str.split(',').explode().str.strip()
genres.value_counts().head(10).plot(kind='barh', color='#E50914')
plt.title('Top 10 Genres on Netflix', fontsize=16)
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig('chart4_genres.png')
plt.close()
print("Chart 4 saved")

# Chart 5: Content Ratings Distribution
plt.figure()
df['rating'].value_counts().plot(kind='bar', color='#E50914')
plt.title('Netflix Content Rating Distribution', fontsize=16)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart5_ratings.png')
plt.close()
print("Chart 5 saved")

print("\nAll charts saved successfully!")
