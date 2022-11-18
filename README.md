## ADA Project - team LEGO

# How on-screen emotions make the money?

## _Analysis of movie sentiment correlation to ratings and revenue in years_.

## Abstract

The flourishing film industry in 2019 achieved the [global box office](https://www.statista.com/statistics/260198/filmed-entertainment-revenue-worldwide-by-region/) worth of around $42.2 billion. One year earlier, in 2018, when [including home entartainment](https://en.wikipedia.org/wiki/Film_industry), this market segment was priced at $136 billion. For comparison, in 2018 [Switzerland GDP](https://www.google.com/search?q=swiss+gdp&oq=swiss+gdp&aqs=chrome..69i57.3721j0j4&sourceid=chrome&ie=UTF-8) was $735.5 billion. The most [popular titles](https://www.boxofficemojo.com/year/world/?ref_=bo_nb_yl_tab) (such as Top Gun: Maveric) can bring box office revenue of $1.486 billion worldwide. This shows how big of a deal it is to draw up a good recipe for an entertaining and gripping movie. With the use of [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), additional datasets ([IMDB](https://www.imdb.com/), [TMDB](https://www.themoviedb.org/)) we will analyze the most popular movies' plots and extract their sentiment ingredients. Besides assessing general sentiment, we will dive deeper and focus on, closest to the human soul, emotions. Moreover, we will try to answer how and which manifestations of violence influence movie popularity.

## Research question

1. How prevalent in popular movies are emotions (anger, disgust, fear, joy, sadness, surprise, love, neutral), general sentiment (positivity, negativity), violence dose (custom measurement), violence manifestation (most frequent words)?
2. How have sentiment indicators (enumerated in 1. subpoint) changed over the years?
3. What are sentiment indicators values for different genres of movies over the years?
4. How does sentiment indicator composition relate to the revenues and reviews?
5. What is the ultimate cookbook for the director to make a successful movie? Which plot features and emotions should he include?

## Additional data resources

As can be seen in the attached notebook, the provided CMU Movie Summary Corpus contains movie data ranging from 1917 to 2011. As we consider the years from 2005 - 2022 a period of the film industry's exponential growth with vast amounts of data, we also want to include these years in the research. We used TMDB to query data from 1915-2021 and obtained 400k movies in total. Also, out of all 42k CMU movies, we have only 10% of revenues, with poor distribution over the years, so we tried to get more revenue data from the internet movie database TMDB. Moreover, we consider ratings a significant preference and popularity indicator besides revenue, for which we are getting rating value and count data from IMDb, the most popular movie-rating platform. Additionally, CMU Movie Summary Corpus data contains summaries that are sometimes very short, making it hard to perform sentiment analysis on such brief texts. We augment the data using TMdB and IMDb plot overviews, synopsis, and alternative plot summaries.
Eventually, we requested movie certificate data from both databases, which can be a potentially helpful indicator of movie violence/romance severity.

- TMDB - Main source for dataset augmentation. We obtained revenues, plot summaries and certificates using TMDB API.
- IMDB - Further extension of movies from TMDB by ratings and additional plot summaries.
- Inflation over the years data (derived from Customer Price Index)
- [Grievance dictionary](https://github.com/Isabellevdv/grievancedictionary) - it will help us to assess the plot violence score and infere what kind of violence manifestation were the most common. We will use especially the dictionary with words for which the threat category fit rating is at least 7 to have the most violence correlated words (scale explained below).
  - Contains 3633 entries, each has 4 features (id, category, word, mean rating)
  - [Threat assessment experts](https://link.springer.com/article/10.3758/s13428-021-01536-2) divided the dictionary into 22 categories (e.g. threat, murder, violence, paranoia etc.)
  - There are 2479 unique words overall
  - The mean rating - how well does the word fits it's category (0 = does not fit at all, 10 = fits perfectly)

## Methods

### 0. Data acquiring

- [IMDB](https://www.imdb.com/) - python [cinemagoer](https://imdbpy.readthedocs.io/en/latest/) library
- [TMDB](https://www.themoviedb.org/) - python [request](https://requests.readthedocs.io/en/latest/) library
- [CPI](https://www.bls.gov/cpi/data.htm) - downloading the data from the website

### 1. Data preprocessing

We need to keep only the frames with either revenues or user ratings, to be able to perform the final popularity correlation. What is also important is expressivity of the plot summaries. If we have in total less then 100 words, we drop these movies as well.

Assumptions:

- popular movies means the one which got the highest box revenues or are highest rated in user rankings.
- when considering sentiment indicators influence on the revenue and reviews, we ommit the aspect of technical realisation of the movie.

### 2. Sentiment analysis

1. general sentiment - we will use python [TextBlob](https://textblob.readthedocs.io/en/dev/index.html) library, which sentimet analyzer is based on [predefined dictionary](https://github.com/sloria/TextBlob/blob/6396e24e85af7462cbed648fee21db5082a1f3fb/textblob/en/en-sentiment.xml). This utility gives us informations such as: polarity (ranging from -1.0 to 1.0, where 1 indicates highest positivity), subjectivity (ranging from 0.0 to 1.0, where 0 means maximal objectivity)
2. emotions - pretrained transformer - [distiled RoBERT trained on 6 different datasets](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base?text=This+movie+always+makes+me+cry..)
3. violence - [grievance dictionary](https://github.com/Isabellevdv/grievancedictionary)
   - measurement - in order to measure general violence amount in movies we will use [min-max normalization](<https://en.wikipedia.org/wiki/Normalization_(statistics)>) to mean category fit score and increase it by one to have indication that the violence occured. Then for each plot we will add the normalized scores to obtain overall violence
   - manifestation - for assessing the most popular manifestation of the violence we will use top-k method combined with max mean fit score value, which will tell us what were the most violence correlated words

### Answering the questions

\<Infering from the data processing>

## Proposed timeline and organization within the team

### Workload split

#### For the milestone 2

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

#### For the upcoming work

- Emna
  - Analysis related to the questions 4, 5
- Ondrej
  - Analysis related to the question 5
  - Website
- Lauri
  - Analysis related to the question 3
- Wojtek
  -Analysis related to the questions 1, 2

### Schedule

- (30.11.22r.) Finishing the analysis related to the first and second question
- (4.12.22r.) Finishing the analysis related to the third question
- (8.12.22r.) Finishing the analysis related to the fourth question
- (16.12.22r.) Finishing the project - ultimate cookbook is ready
- (23.12.22r.) Project deadline

## Questions for TAs
