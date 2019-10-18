# Sentiment Analysis

This project was part of the course in Big Data in the Fall of 2014, during my masters.

## Description
According to Moat et al: “…data on changes in how often financially related Wikipedia pages were viewed may have
contained early signs of stock market moves.(1)” and “By analyzing changes in Google query volumes for search terms
related to finance, we find patterns that may be interpreted as “early warning signs” of stock market moves. (2)”
Primary motivation for this project was to simply verify above claims using Hadoop as a tool. Apple inc’s stock
performance was measured against sentiment analysis data from internet archives, and Wikipedia page counts related
to apple products.

### Data used
1. Web-archive files which are archived web-content, publicly available, and stored in Amazon’s S3 buckets.
2. Wikipedia page counts of Apple’s products

### Map reduce jobs written in Python(using Hadoop streaming) to do the following main tasks:
1. Web archive files were accessible in Amazon’s S3 storage
2. Data extraction stage involved reading data from S3 buckets, filtering content related to Apple’s products, and
storing extracted data in text files. The setup involved 10 worker nodes, and 1 master node
3. Sentiment Analysis stage involved reading data from the extracted text files and performing sentiment analysis,
and storing results in a text file with dates
4. Wikipedia page counts related to Apple’s products by date was scraped using a Python script
5. Data was analyzed using Google Fusion tables.

## Description of folders

Folder | Description
-------|-------------
[ExtractionMRCode/](https://github.com/codebleeder/Sentiment-analysis/tree/master/ExtractionMRCode)|Map-reduce code to extract data relevant to Apple products using Textblob library
[cleanWithoutTextblob/](https://github.com/codebleeder/Sentiment-analysis/tree/master/cleanWithoutTextblob)|Map-reduce code to extract data relevant to Apple products without Textblob library. This code was used on AWS EMR cluster as Textblob is not needed, and is simpler.
[collectWikipediaPageCounts/](https://github.com/codebleeder/Sentiment-analysis/tree/master/collectWikipediaPageCounts)|Code to extract page views on Apple products on Wikipedia
[sentiment/](https://github.com/codebleeder/Sentiment-analysis/tree/master/sentiment)|Map-reduce code to calculate sentiment of extracted data
[stats/](https://github.com/codebleeder/Sentiment-analysis/tree/master/stats)|Extracted sentiment data, and stock values
[utilityCode/](https://github.com/codebleeder/Sentiment-analysis/tree/master/utilityCode)|Python scripts for extracting, cleaning, and filtering data


## Presentation:

The [Presentation](https://github.com/codebleeder/Sentiment-analysis/blob/master/analysis%20of%20stock%20performance%20based%20on%20sentiment%20analysis.pdf) contains further details on data source (WARC), and overall data-flow.

## Data visualization

Here is the data visualization from final data: [data visualization](https://fusiontables.google.com/DataSource?docid=13KKVu3TX0F9R2hQOG6FbElf-KrPoFgSmOuxa1mPU#chartnew:id=3)

## Improvements

This course focused on the data engineering part. i.e., running Hadoop Map-reduce code using a cluster, which was successfully achieved. 

However, at the end of the project I felt there is a lot more to this. There is a need to learn more and build upon this:
1. Learn statistical methods, and machine learning to gain further insights, and possibly create predictive models.
1. Use a custom visualization library like D3.js
1. Use consistent data. The web-archive files were recorded at certain intervals. The data collected wasn't inline with the dates on which the actual posts were made. 

## References
1. Quantifying Wikipedia Usage Patterns Before Stock Market Moves (Helen Susannah Moat, Chester Curme, Adam
Avakian, Dror Y. Kenett, H. Eugene Stanley & Tobias Preis - http://rdcu.be/x9Eo)
2. Quantifying Trading Behavior in Financial Markets Using Google Trends (Tobias Preis, Helen Susannah Moat & H.
Eugene Stanley - http://rdcu.be/x9EN)
