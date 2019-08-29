
# coding: utf-8

# # Applying Machine Learning to Sentiment Analysis

# In[70]:


# import libs
import pandas as pd
import numpy as np
import pyprind
import os


# In[71]:


# Obtaining the IMDb movie review dataset

def create_sa_df():
    '''obtaining movie data'''
    pbar = pyprind.ProgBar(50000)
    labels = {'pos':1, 'neg':0}
    df = pd.DataFrame()
    for s in ('train', 'test'):
        for i in ('pos','neg'):
            path = 'C://Users//omar.hazim//movie_review//movie_dataset//aclImdb//%s//%s' %(s,i)
            for file in os.listdir(path):
                with open(os.path.join(path, file), encoding="utf8") as infile:
                    txt = infile.read()
                    df = df.append([[txt, labels[i]]], ignore_index=True)
                    pbar.update()
    df.columns = ['review', 'sentiment']
    return df

def shuffle_dataset(df):
    '''shuffle the stored data to prepare for splitting training and testing datasets'''
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    return df.to_csv('C://Users//omar.hazim//movie_review//movies_data//raw_data//mv_data.csv', index=False)

# In[ ]:


# Creat main file 

def main():
    # Reading training/testing 
    df = create_sa_df()
    print(df.head())
    
     #Shuffle dataset and create .csv file
    shuffle_dataset(df)
    df_shuffled = pd.read_csv('C://Users//omar.hazim//movie_review//movies_data//raw_data//mv_data.csv')
    print('Shuffled dataset:',df_shuffled.head())
    
    
# run main file 
if __name__ == '__main__':
    main()

