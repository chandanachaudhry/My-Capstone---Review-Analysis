# My-Capstone - Review-Analysis

## Table of Contents

- [The Problem area](#background)
- [The Big Idea](#idea)
- [The Impact](#impact)
- [Potential Applications](#applications)
- [Roadmap for EDA](#eda)
- [Data Dictionary](#data-dictionary)
- [Modeling](#modeling)
   - [Logistic Regression](#modeling)
   - [Decision Trees](#modeling)
   - [LSTM neural networks](#modeling)
- [Model Evaluation](#evaluation)

## The Problem area
The particular area of interest is the Retail Industry. For any strategy building or forecasting, it is crucial to understand the consumer shopping behaviour. This helps us define patterns and nuances which helps the business to grow further. 

<img src="https://media.istockphoto.com/id/1206753760/vector/set-of-feedback-icons-customer-opinion-marketing-research-review-product.jpg?s=612x612&w=0&k=20&c=7E7y7cpNpqhZOZdAO5dH0HzWd7mwkWYnGTFzRRpF4ps=" alt="Why we need it" width="340" height="200" border="10" />

## The Big Idea
Studying the consumer behaviour or the end use shopping pattern helps the product owning team to come up with better iterations or enhanced shopping experience for the customer. Which eventually helps in increasing the revenue. The data set of interest consist of customer reviews which can be analyzed by using Sentiment Analysis : both RNNs and LSTMs can be used for sentiment analysis, which involves determining the sentiment or emotion expressed in a piece of text (e.g.,  positive, negative, neutral). We can also use aspect based sentiment analysis, which can help us in identifying particular aspects such as ‘quality’ , ‘price’ etc.

## The Impact
Sentiment analysis and aspect based sentiment analysis can really help the company by Product improvement, customer feedback analysis, marketing campaign planning and competitive analysis. Overall better delivery of product to the customer. 

<img src="https://media.sproutsocial.com/uploads/2023/06/Review-Analysis-Final.png" alt="Analysing Reviews" width="540" height="280" border="10" />
</a>

## Potential Applications
- Customer Feedback Analysis: Companies can use this analysis to understand customer satisfaction levels, identify areas for improvement, and make data-driven decisions. 
- Political Analysis: Can be used in political campaigns to gauge public opinion, monitor voter sentiment. 
- Customer Support: Can be integrated into customer support systems to automatically categorize and prioritize customer queries based on sentiment. It helps in providing faster responses and resolving customer issues more efficiently. 
- Brand Monitoring: By analyzing sentiment, they can track public perception, identify emerging trends, and manage their brand reputation effectively.

## Roadmap for EDA
- The Data set can be downloaded from the link : https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews/data
- Analysis of null values and figuring out suitable option to drop or fill na()
- Finding out dataset information and then converting 'Object' type data to necessary 'Int/Float' type or by adding dummy variables


**This is essentially a classification problem where we have to classify our review column(Target) into three main buckets such as 'Positive' , 'Negative' and 'Nuetral' using NLP**



## Data Dictionary
- `Clothing ID`: Integer Categorical variable that refers to the specific piece being reviewed.
- `Age`: Positive Integer variable of the reviewers age.
- `Title`: String variable for the title of the review.
- `Review Text`: String variable for the review body.
- `Rating`: Positive Ordinal Integer variable for the product score granted by the customer from 1 Worst, to 5 Best.
- `Recommended IND`: Binary variable stating where the customer recommends the product where 1 is recommended, 0 is not recommended.
- `Positive Feedback Count`: Positive Integer documenting the number of other customers who found this review positive.
- `Division Name`: Categorical name of the product high level division.
- `Department Name`: Categorical name of the product department name.
- `Class Name`: Categorical name of the product class name.

## Modeling
Build models with three different algorithms and compare their performance. Thus, we will determine the algorithm that makes the most accurate emotion estimation by using the information obtained from the Review Text variable.

  #### - Logistic Regression : Logistic regression is one of the most basic (yet effective) tools we have for classifying categorical data. Here using review_text as the target variable

  ####  - Decision Trees : Decision trees are useful for categorizing results where attributes can be sorted against known criteria to determine the final category. In this case, extremely useful as it requires less data cleaning than other data modeling techniques.

 #### - LSTM neural networks : recurrent neural network (RNN) architecture that is particularly well-suited for sequence prediction tasks, such as natural language processing (NLP), and speech recognition  


## Model Evaluation : based on hyperparameter optimization 

## Applications : Reccomender sytemems 
