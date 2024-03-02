## Movie-Recommendation-System

In this machine learning project, I utilized a movie dataset from Kaggle to develop a movie recommendation system. The project is divided into three main parts: 
1. __Content-Based Recommendation__,
2. __Popularity-Based Recommendation__,
3. __Genres-Based Recommendation__.

For the Content-Based Recommendation, I used Natural Language Processing (NLP) techniques to analyze movie descriptions and recommend similar movies based on their content. This approach helps users discover movies with similar themes or genres.

The Popularity-Based Recommendation system recommends movies based on their overall popularity among users based on ratings and total likes. This method is useful for suggesting popular and widely liked movies to a broad audience.

In the Genres-Based Recommendation, I focused on recommending movies based on specific genres selected by the user. This approach allows users to explore movies within their preferred genres and discover new films of interest.

To implement the recommendation system, I created pickle files to store trained models and data (see *JupyterNotebookFiles*). Additionally, I developed a Flask application (app.py) to convert the model into a website (see *FlaskApplicationFiles*). The website utilizes __HTML__, __CSS__, and the __Flask framework__ to provide users with an interactive interface to explore movie recommendations.
