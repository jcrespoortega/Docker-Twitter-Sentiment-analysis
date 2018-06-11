# Docker Twitter Sentiment analysis

Docker's Cointaners are useful tools because its have some advantages over virtual machines as time and  memory resources optimization.

In this app I develop a Sentiment Analysis in the platform of Twitter, with their Streaming API in order to feed with data the system. The proyect is developed with Docker Compose, creating an image which is bases on Clodera and MongoDB images.  

Sentiment Analysis is based in these case in dictionaries, in order to make it works in Cloudera image  an old Map Reduce is used with mrjob library in python. When the procces is finished the result are stored in MongoDB. 

The image build is also available in Docker Hub with the name of jcrespo2017/fin_jc.

The information to build and run container is in docker run.txt and app directory have all the files and scripts to build it.
