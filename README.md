# Sentiment Analysis

I had done this project for my course in Big Data in the Fall of 2014, during my masters. I wanted to save this project before I lost the code from my computer. 

## Description of folders

Folder | Description
-------|-------------
ExtractionMRCode/|Map-reduce code to extract data relevant to Apple products using Textblob library
cleanWithoutTextblob/|Map-reduce code to extract data relevant to Apple products without Textblob library
collectWikipediaPageCounts/|Code to extract page views on Apple products on Wikipedia
sentiment/|Map-reduce code to calculate sentiment of extracted data
stats/finalData/|Final extracted sentiment data
utilityCode/|Python scripts for extracting, cleaning, and filtering data


## Presentation:

The [Presentation](https://github.com/codebleeder/Sentiment-analysis/blob/master/analysis%20of%20stock%20performance%20based%20on%20sentiment%20analysis.pdf) contains further details on data source (WARC), and overall data-flow.

## Data visualization

Here is the data visualization from final data: [data visualization](https://fusiontables.google.com/DataSource?docid=13KKVu3TX0F9R2hQOG6FbElf-KrPoFgSmOuxa1mPU#chartnew:id=3)

## Improvements

This course focused on the data engineering part. i.e., running Hadoop Map-reduce code using a cluster, which was successfully achieved. 

However, at the end of the project I felt there is a lot more to this. There is a need to learn more and build upon this:
1. Learn statistical methods, and machine learning
1. Use a custom visualization library like D3.js
1. Use consistent data. The web-archive files were recorded at certain intervals. The data collected wasn't inline with the dates on which the actual posts were made. 
