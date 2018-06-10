# Docker Twitter Sentiment analysis

Docker's Cointaners are very useful tool because its have some advantages over virtual machines as time and ran memory resources optimization.

In this app I develop a Sentiment Analysis in the platform of Twitter, with their Streaming API in order to feed with data the system. The proyect is developed with Docker Compose developing an image which is bases on Clodera and Mongo DB images.  

Sentiment Analysis is based in these case in dictionaries, in order to make it works in Cloudera image I develop an old Map Reduce with mrjob library in python and when the procces is finished the result are stored in MongoDB.

The image build is also available in Docker Hub with the name of jcrespo2017/fin_jc.
