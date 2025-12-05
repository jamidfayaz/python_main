import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load MovieLens 100K dataset files (u.data and u.item) from local directory
ratings_cols = ['userId', 'movieId', 'rating', 'timestamp']
movies_cols = ['movieId', 'title', 'release_date', 'video_release_date', 'IMDb_url', 
               'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy',
               'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
               'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

ratings = pd.read_csv('u.data', sep='\t', names=ratings_cols, encoding='latin-1')
movies = pd.read_csv('u.item', sep='|', names=movies_cols, encoding='latin-1', usecols=range(24))

# Ratings distribution
plt.figure(figsize=(8,6))
sns.countplot(x='rating', data=ratings, palette='viridis')
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Number of ratings per movie (top 20)
movie_rating_counts = ratings['movieId'].value_counts().sort_values(ascending=False).head(20)
plt.figure(figsize=(12,6))
sns.barplot(x=movie_rating_counts.index.astype(str), y=movie_rating_counts.values, palette='magma')
plt.title('Top 20 Movies by Number of Ratings')
plt.xlabel('Movie ID')
plt.ylabel('Number of Ratings')
plt.xticks(rotation=45)
plt.show()

# Number of ratings per user (top 20)
user_rating_counts = ratings['userId'].value_counts().sort_values(ascending=False).head(20)
plt.figure(figsize=(12,6))
sns.barplot(x=user_rating_counts.index.astype(str), y=user_rating_counts.values, palette='cool')
plt.title('Top 20 Users by Number of Ratings')
plt.xlabel('User ID')
plt.ylabel('Number of Ratings')
plt.xticks(rotation=45)
plt.show()

# Average rating by genre
movies_long = movies.melt(id_vars=['movieId', 'title'], value_vars=movies_cols[5:], var_name='genre', value_name='is_genre')
movies_genres = movies_long[movies_long['is_genre'] == 1]

ratings_with_genres = pd.merge(ratings, movies_genres[['movieId', 'genre']], on='movieId')

avg_rating_by_genre = ratings_with_genres.groupby('genre')['rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(14,7))
sns.barplot(x=avg_rating_by_genre.index, y=avg_rating_by_genre.values, palette='plasma')
plt.title('Average Movie Rating by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()

# Genre popularity (number of movies per genre)
genre_popularity = movies_long[movies_long['is_genre'] == 1]['genre'].value_counts()
plt.figure(figsize=(14,7))
sns.barplot(x=genre_popularity.index, y=genre_popularity.values, palette='inferno')
plt.title('Genre Popularity (Number of Movies)')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()
