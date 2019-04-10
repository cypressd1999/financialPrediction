import xmlrpc.client
import numpy as np

def run():
    print("start prediciting: ")

    stock_name = "AAPL"
    print("stock name: " + stock_name)

    # stock price retriever
    container1 = xmlrpc.client.ServerProxy('http://localhost:8000')
    stock_data = container1.Predict(stock_name)
    print(stock_data)
    print("\nStock price data Retrieval FINISHED")

    # twitter collector
    container2 = xmlrpc.client.ServerProxy('http://localhost:9000')
    twitter_data = container2.Predict(stock_name)
    print(twitter_data)
    print("\nTwitter data Retrieval FINISHED")

    # tockenizer
    container3 = xmlrpc.client.ServerProxy('http://localhost:11000')
    tockenized_twitter_data = container3.Predict(twitter_data)
    print(tockenized_twitter_data)
    print("\nTwitter data Tockenization FINISHED")

    # sentiment analysis
    container4 = xmlrpc.client.ServerProxy('http://localhost:12000')
    prediction_1 = container4.Predict(tockenized_twitter_data)
    print(prediction_1)
    print("\nTwitter data Sentiment Analysis FINISHED")

    # LSTM
    container5 = xmlrpc.client.ServerProxy('http://localhost:12000')
    prediction_2 = container5.Predict(stock_data)

    # # Bagging Regression
    # container6 = xmlrpc.client.ServerProxy('http://localhost:13000')
    # prediction_3 = container6.Predict(stock_data)

    # # Random Forest
    # container7 = xmlrpc.client.ServerProxy('http://localhost:14000')
    # prediction_4 = container7.Predict(stock_data)

    # # K-Nearest
    # container8 = xmlrpc.client.ServerProxy('http://localhost:14000')
    # final_prediction = container8.Predict(stock_data)

    # # Mem cacher
    # container9 = xmlrpc.client.ServerProxy('http://localhost:15000')
    # stock_data = container9.Predict();

    # # Weighting Algorithm
    # container9 = xmlrpc.client.ServerProxy('http://localhost:14000')
    # final_prediction = container9.Predict(prediction_1, prediction_2, prediction_3, prediction_4)

    # print(final_prediction)

if __name__ == "__main__":
    run()