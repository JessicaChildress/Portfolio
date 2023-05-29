# In this file I perform some basic data cleaning on the .csv files that are storing all of our data

import pandas as pd


'''
* Function: dropDuplicateRows()
* This function uses pandas to drop duplicate rows from all of the files storing data that will
* be used to train our neural network. 
* Parameters: NA
* Returns: NA 
'''
def dropDuplicateRows():
    df_trefoils = pd.read_csv("trefoils.csv")
    df_trefoils.drop_duplicates(inplace=True)
    print("new trefoils size: ", len(df_trefoils.index))
    # print(df_trefoils.iloc[-1])

    df_hopff_links = pd.read_csv("hopff_links.csv")
    df_hopff_links.drop_duplicates(inplace=True)
    print("new links size: ", len(df_hopff_links.index))
    # print(df_hopff_links.iloc[-1])

    df_unknots = pd.read_csv("unknots.csv")
    df_unknots.drop_duplicates(inplace=True)
    print("new unknots size: ", len(df_unknots.index))
    # print(df_unknots.iloc[-1])