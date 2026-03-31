import csv
import os


def loadMovieData(data_path, item_path):
    """
    Loads movie ratings and titles from MovieLens data files.

    Expects tab-separated ratings in data_path and pipe-separated titles in item_path.

    Args:
        data_path (str): File path to 'u.data'.
        item_path (str): File path to 'u.item'.

    Returns:
        tuple (dict, dict): A mapping of movie_id to ratings list, and movie_id to title.
    """
    movie_id_to_ratings = {}
    movie_id_to_title = {}

    # Loads titles from u.item using Pipe delimiter.
    if os.path.exists(item_path):
        with open(item_path, "r", encoding="ISO-8859-1") as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                if row:
                    movie_id_to_title[row[0]] = row[1]

    # Loads ratings from u.data using Tab delimiter.
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="ISO-8859-1") as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                if row:
                    m_id = row[1]
                    rating = float(row[2])
                    if m_id not in movie_id_to_ratings:
                        movie_id_to_ratings[m_id] = []
                    movie_id_to_ratings[m_id].append(rating)

    return movie_id_to_ratings, movie_id_to_title


def calculateTopMovies(data_path, item_path, min_reviews=50):
    """
    Identifies the top 10 movies by average rating with sufficient reviews.

    Args:
        data_path (str): Path to ratings file.
        item_path (str): Path to items file.
        min_reviews (int): Minimum number of ratings required to be considered.

    Returns:
        list (tuple): A list of top 10 (title, average_rating) sorted by rating.
    """
    movie_id_to_ratings, movie_id_to_title = loadMovieData(data_path, item_path)
    rankings = []

    for m_id, ratings in movie_id_to_ratings.items():
        if len(ratings) >= min_reviews: # Only considers movies with a credible review count.
            avg_rating = sum(ratings) / len(ratings)
            title = movie_id_to_title.get(m_id, f"Unknown (ID: {m_id})")
            rankings.append((title, avg_rating))

    # Sorts the movies primarily by average rating in descending order.
    rankings.sort(key=lambda x: x[1], reverse=True)
    return rankings[:10]


def main():
    """
    Entry point to display the top 10 movie titles and their average ratings.
    """
    # Directs to the ml-100k directory relative to the script location.
    data_dir = "ml-100k/"
    data_path = f"{data_dir}u.data"
    item_path = f"{data_dir}u.item"

    if os.path.exists(data_path) and os.path.exists(item_path):
        top_movies = calculateTopMovies(data_path, item_path)
        print("Top 10 Movie Ratings (Traditional Method):")
        for i, (title, avg) in enumerate(top_movies, 1):
            print(f"{i}. {title} - {avg:.2f}")
    else:
        print(f"Error: Required files not found in {data_dir}")
        print("Please ensure 'u.data' and 'u.item' are extracted correctly.")


if __name__ == "__main__":
    main()
