import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
SVC_Gaussian = SVC(kernel="rbf")
from sklearn.kernel_approximation import Nystroem
import sklearn.metrics
import matplotlib.pyplot as plt
import seaborn as sns

def histogram_chart_example(values, filename):
    plt.figure() # creates a new *current figure*
    # default number of bins is 10
    plt.hist(values, bins=20, edgecolor="black")
    plt.savefig(filename)

# LOAD THE DATA
stroke_df = pd.read_csv("healthcare-dataset-stroke-data.csv")

# EXPLORE THE DATA
print(stroke_df.head(5))
print(stroke_df.tail(5))
print(stroke_df.columns)
print(stroke_df.iloc[660:670, :])
print(stroke_df["gender"].unique())


# CLEAN THE DATA &
# HANDLE MISSING VALUES 
print(stroke_df.isnull().sum()) # there are 201 null values in the bmi column of the dataset (less than 4% of the data)
print("mean: ", stroke_df["bmi"].mean())
print("median: ", stroke_df["bmi"].median())
print("mode: ", stroke_df["bmi"].mode())
# the mean, median, and mode are all ~28
# create a bmi histogram to determine which fillna technique to use
histogram_chart_example(stroke_df["bmi"], "histogram_bmi_before.png")

# replace null values with median:
stroke_df["bmi"].fillna(28.1, inplace=True)

# shows the new distribution of data after null values were filled
histogram_chart_example(stroke_df["bmi"], "histogram_bmi_after.png")

# VISUALIZE THE DATA
# Look for relationships between features and the target variable
# Create cat plots, heatmaps, pairplots and boxplots
''' these are all the different features:
'id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
'work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status', 'stroke'
'''
# create a dataframe containing numerical columns
stroke_df_quantitative = stroke_df.copy(deep=True)
stroke_df_quantitative.drop(labels=["id", "gender", "ever_married", "work_type", "Residence_type", "smoking_status"], axis='columns', inplace=True)
# generate a heat map:
fig, ax = plt.subplots()
sns.heatmap(stroke_df_quantitative.iloc[660:670, :], cmap ='RdYlGn')
plt.savefig("heatmap.png")
# there are not strong relationships that are easily identifiable by the heat map for this slice of the dataframe

# generate a pairplot:
sns.pairplot(stroke_df)
plt.savefig("pairplot.png")
# age appears to be a factor in the presence of hypertension 
# a bmi greater than 60 does not correlate to a higher incidence of stroke

# generate some catplots and box plots
sns.catplot(stroke_df, x="avg_glucose_level", y="gender", hue="stroke", kind="violin", bw=.25, cut=0, split=True)
plt.savefig("catplot_glucose_gender.png")
# regardless of gender, higher glucose levels are associated with a higher incidence of stroke

sns.catplot(data=stroke_df, x="Residence_type", y="hypertension", hue="stroke", kind="violin", bw=.25, cut=0, split=True)
plt.savefig("catplot_Residence_hypertension.png")
# does not appear to be a strong relationship between hypertension in urban vs rural areas on stroke

sns.catplot(stroke_df, x="heart_disease", y="avg_glucose_level", kind="box")
plt.savefig("catplot_heartDisease_glucose.png")
# there is a pretty strong correlation between the presence of heart disease and higher avg glucose levels

sns.catplot(stroke_df, x="ever_married", y="age", hue="heart_disease",  kind="violin", bw=.25, cut=0, split=True)
plt.savefig("catplot_marriage_heartDisease.png")
# age appears to be a greater contributor to stroke than does being married

# SPLIT INTO TRAIN/TEST SETS
X = stroke_df.iloc [:, : -1]    # ” : ” means it will select all rows,    “: -1 ” means that it will ignore last column
Y = stroke_df.iloc [:, -1 :]    # ” : ” means it will select all rows,    “-1 : ” means that it will ignore all columns except the last one

# PREDICT AND TRAIN THE RANDOM FOREST MODEL

# create regressor object:
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
 
# fit the regressor with x and y data
regressor.fit(X, Y)

# predict a new result
Y_pred = regressor.predict(np.array([6.5]).reshape(1, 1))  # test the output by changing values

# GET PRECISION, RECALL, ACCURRACY SCORES
