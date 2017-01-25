
In this assignment, you will build a prototype system to analyze a dataset of Twitter
tweets collected beforehand using Twitter’s datastream API. The tweets are available in
the public container ‘tweets’ in the SSC cloud, and the dataset consists of a number of
files containing lineseparated
tweet entries. Every second line is a blank line.
Each tweet is a JSON document http://en.wikipedia.org/wiki/JSON . JSON is one of the
standard Markup formats used on the Web. While it would not be considered your
typical “scientific data”, familiarity with JSON quickly becomes essential in applied cloud
computing and data analytics. For the specific case of Twitter tweets, you can read
about the possible fields in the JSON documents here:
https://dev.twitter.com/overview/api/tweets
This particular Twitter dataset was collected by filtering the stream of tweets to store
those containing the Swedish pronouns “han”, “hon”, “den”, “det”, “denna”, “denne” and
the gender neutral, new pronoun “hen”. Your task is now to construct a computeservice
based on the distributed task queue ‘Celery’, using ‘RabbitMQ’ as the broker. The
service should be capable of analyzing the dataset on demand. In particular, as an
example of an analysis, your solution should count the total number of mentions of the
above mentioned pronouns in the dataset.
