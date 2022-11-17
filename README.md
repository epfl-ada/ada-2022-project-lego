# ADA Project - team LEGO

# How on-screen emotions make the money? Movies sentiment analysis in time.

## Abstract

Flourishing film industry in 2019 achived the [global box office](https://www.statista.com/statistics/260198/filmed-entertainment-revenue-worldwide-by-region/) worth of around $42.2 billions. One year earlier, in 2018, when [including home entartainment](https://en.wikipedia.org/wiki/Film_industry), this market segment was priced at $136 billions. For comparison in 2018 [Switzerland GDP](https://www.google.com/search?q=swiss+gdp&oq=swiss+gdp&aqs=chrome..69i57.3721j0j4&sourceid=chrome&ie=UTF-8) was $735.5 billions. The most [popular titles](https://www.boxofficemojo.com/year/world/?ref_=bo_nb_yl_tab) (such us Top Gun: Maveric) can bring box office revenue of $1.486 billions worldwide. This shows how big of a deal it is to draw up a good recipe for entertaining and gripping movie. With the use of [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), additional datasets ([IMDB](https://www.imdb.com/), [TMDB](https://www.themoviedb.org/)) we will analyze the most popular movies' plots and extract their sentiment ingredients. Beside assessing general sentiment we will dive deeper and focus on, closest to the human soul, emotions. Moreover we will try to answer how and which manifestations of the violence influence movie popularity.

## Research question
1. How prevalent in popular movies are emotions (anger, disgust, fear, joy, sadness, surprise love, neutral), general sentiment (positivity, negativity), violence dose (custom measurement), violence manifestation (most frequent word)?
2. How sentiment indicators (enumerated in 1. subpoint) change over the years?
3. What are sentiment indicators values for different generes of movies over the years?
4. How sentiment indicators composition relates to the revenues and reviews?
5. What is the ultimate cookbook for making successful movie?

## Additional data resources
\<Why we have deciced that the old data is not sufficient?>

\<For each of the dataset: 
	- Where it comes from?
	- What is it's initial application?
	- What part of it we will use it and for what purpose?
Describe the choosen data (features, size).>
- IMDB
- TMDB
- Inflation over the years data (derived from Customer Price Index)
- Grievance dictionary

## Methods
### Data acquiring
- [IMDB](https://www.imdb.com/) - python [cinemagoer](https://imdbpy.readthedocs.io/en/latest/) library
- [TMDB](https://www.themoviedb.org/) - python [request](https://requests.readthedocs.io/en/latest/) library
- [CPI](https://www.bls.gov/cpi/data.htm) - downloading the data from the website
### Data preprocessing 
\<What our initial dataset should look like? (Cleaning, combining for further processing)>
Assumptions:
- popular movies means the one which got the highest box revenues. If the film has no box revenue, then we consider it not influential enough.
- when considering sentiment indicators influence on the revenue and reviews, we ommit the aspect of technical realisation of the movie.
### Sentiment analysis
- emotions - pretrained transformer - [distiled RoBERT trained on 6 different datasets](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base?text=This+movie+always+makes+me+cry..) - [|collab working example|](https://colab.research.google.com/drive/1XGtSiTwpB2o8EImQ2PeRzpHL_kSxBTOV?usp=sharing)
- general sentiment - method based on [predefined dictionary](https://github.com/sloria/TextBlob/blob/6396e24e85af7462cbed648fee21db5082a1f3fb/textblob/en/en-sentiment.xml) - python [TextBlob](https://textblob.readthedocs.io/en/dev/index.html) library - [|collab working example|]()
- violence - [grievance dictionary](https://github.com/Isabellevdv/grievancedictionary)
    - measurement - term frequency and weighting - [|collab working example|]()
    - manifestation - tf and wordnet synset - [|collab working example|]()

### Answering the questions
\<Infering from the data processing>

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