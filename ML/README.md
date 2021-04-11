# ML-anomaly_detection-demo

This Repo is to accompany the Cisco Live HOLSPG-2400 lab sessions.

First clone the repo with 

$ git clone https://github.com/mikemikhail/HOLSPG-2400/

Install the requirements:

$ cd ~/ML 
$ pip install -r requirements.txt

Start Machine Learning prediction & Anomaly Detection:

$ python moniotr.py

In a few seconds you'll see descriptions of large dataframes of numbers. After the first large training cycle, you'll see plots. Initially, there's 3 lage learning activities, 5 minutes apart, with plots updated after each. Then smaller data learn/predict/compare every 10 minutes. The new model will improve with experience!

![3 plots](https://github.com/mikemikhail/ML-anomaly_detection-demo/blob/master/demo.png)

A model is born!

The program takes you to a start on same time of day on January 9th, 2020. From there can run until data is exhausted, about a week to last data of January 16th, 2020. Previous period data is used for training and prediction.
