# ADA Project - team LEGO

# How emotions make the money? Movies sentiment analysis in time.

## Abstract
### 0. Old data - why it is not satisfying?
### 1. How we got the new data?
### 2. New data descriptive statistics + assumptions on the data for further analysis
#### Assumptions
- popular movies means the one which got the highest box revenues. If the film has no box revenue, then we consider it not influential enough.
- when considering sentiment indicators influence on the revenue and reviews, we ommit the aspect of technical realisation of the movie.

## Research question
1. How prevalent in popular movies are emotions (anger, disgust, fear, joy, sadness, surprise love, neutral), general sentiment (positivity, negativity), violence dose (custom measurement), violence manifestation (most frequent word)?
2. How sentiment indicators (enumerated in 1. subpoint) change over the years?
3. What are sentiment indicators values for different generes of movies over the years?
4. How sentiment indicators composition relates to the revenues and reviews?
5. What is the ultimate cookbook for making successful movie?

## Additional data resources
- IMDB and TMDB
- Inflation over the years data
- Grievance dictionary

## Methods
### Data acquiring
- [IMDB](https://www.imdb.com/) - python [cinemagoer](https://imdbpy.readthedocs.io/en/latest/) library
- [TMDB](https://www.themoviedb.org/) - python [request](https://requests.readthedocs.io/en/latest/) library
### Sentiment analysis
- emotions - pretrained transformer - [distiled RoBERT trained on 6 different datasets](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base?text=This+movie+always+makes+me+cry..) - [|collab working example|](https://colab.research.google.com/drive/1XGtSiTwpB2o8EImQ2PeRzpHL_kSxBTOV?usp=sharing)
- general sentiment - method based on [predefined dictionary](https://github.com/sloria/TextBlob/blob/6396e24e85af7462cbed648fee21db5082a1f3fb/textblob/en/en-sentiment.xml) - python [TextBlob](https://textblob.readthedocs.io/en/dev/index.html) library - [|collab working example|]()
- violence - [grievance dictionary](https://github.com/Isabellevdv/grievancedictionary)
    - measurement - term frequency and weighting - [|collab working example|]()
    - manifestation - tf and wordnet synset - [|collab working example|]()

## Proposed timeline and organization within the team
### Workload split
 - Emna
    - Implementing and testing SA methods
        - distiled RoBERT utilities
 - Ondrej
    - Scraping movie data
    - Data descriptive stats
 - Lauri
    - Finding America inflation data (movies revenue in USD)
 - Wojtek
    - Finding, implementing and testing SA methods
        - grievance dictionary utilities
            - tf and weighting for violence measurement
            - tf and wordnet synsets for violence manifestation
    - Readme outline
### Schedule
 - (30.11.22r.) Answering based on code the 1-st question
 - (16.12.22r.) Finishing the project
 - (23.12.22r.) Project deadline

## Questions for TAs