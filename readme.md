# Anime Recommendation System

![Project Preview](https://media.tenor.com/QcvGepJbzYIAAAAC/anime-tumblr.gif)

## About the Project

Welcome to the "Anime Recommendation System" project! This project aims to provide personalized anime recommendations based on users' preferences. The recommendation system uses CountVectorizer to analyze anime summaries after applying pre-processing techniques such as text normalization (lowercasing) and removing punctuation marks.

## Dataset

For this project, I used a publicly available anime dataset containing information about various anime shows, including their summaries, genres, and ratings. This dataset serves as the foundation for building the recommendation system.

link : https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020

## Pre-processing

To prepare the anime summaries for analysis, I applied the following pre-processing steps:

- Lowercasing: Convert all text to lowercase to ensure consistency.
- Removing Punctuation: Eliminate punctuation marks from the text to focus on content words.
- Tokenization: Split the text into individual words (tokens) to create a bag-of-words representation.
- Stop Words Removal: Remove common stop words like "the", "and", "is", etc., to reduce noise in the data.

## Feature Extraction

After pre-processing, I used the CountVectorizer technique to convert the pre-processed text into numerical features. CountVectorizer creates a document-term matrix, representing each anime summary as a vector of word frequencies.

## Recommendation Model

The recommendation model is developed using collaborative filtering, a popular technique for recommending items based on user behavior and preferences. The model analyzes the preferences of other users with similar tastes and suggests anime shows that align with the user's interests.

## Contribution

I am continuously working on refining this recommendation system to enhance its accuracy and effectiveness. If you have any ideas for improvements, new features, or encounter any issues, please feel free to open an issue or submit a pull request. Your contributions and feedback are invaluable!

## License

This project is open-source and licensed under the MIT License. For more details, please see the "LICENSE" file.
