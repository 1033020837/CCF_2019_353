import pandas as pd
import os
import jieba
import re

from util import * 

class Solution(object):

    def __init__(self):
        self.train_path = os.path.join("data","Train_Data.csv")
        self.test_path = os.path.join("data","Test_Data.csv")
        
    def read_data(self):
        """
            读取数据
        """
        self.train_data = pd.read_csv(self.train_path)
        self.test_data = pd.read_csv(self.test_path)

    def process_data(self):
        """
            处理数据
        """
        
        self.train_data['title'] =  self.train_data['title'].fillna('')
        self.train_data['text'] =  self.train_data['text'].fillna('')
        self.test_data['title'] =  self.test_data['title'].fillna('')
        self.test_data['text'] =  self.test_data['text'].fillna('')

        self.train_data['title'] = self.train_data['title'].apply(stop_words)
        self.test_data['title'] = self.test_data['title'].apply(stop_words)
        self.train_data['text'] = self.train_data['text'].apply(stop_words)
        self.test_data['text'] = self.test_data['text'].apply(stop_words)

        self.train_data['title'] = self.train_data.apply(seg_depart,axis = 1, args = ("title",))
        self.train_data['text'] = self.train_data.apply(seg_depart,axis = 1, args = ("text",))

if __name__ == "__main__":
    solution = Solution()
    solution.read_data()

    solution.process_data()
    print(solution.train_data.head(15)['text'])