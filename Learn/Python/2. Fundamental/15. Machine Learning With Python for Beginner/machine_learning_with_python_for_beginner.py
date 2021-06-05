# -*- coding: utf-8 -*-
"""Machine Learning With Python for Beginner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HsnllJ9g454t3HVigRCjix_lc45L1DER

# Eksplorasi Data: Memahami Data dengan Statistik - Part 1
"""

import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
print('Shape dataset:', dataset.shape)

print('Lima data teratas:\n', dataset.head())

print('Informasi dataset:\n', dataset.info())

print('Statistika Deskriptif:\n', dataset.describe())

"""# Eksplorasi Data: Memahami Data dengan Statistik - Part 2"""

dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset_corr)
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())

print('\nKorelasi BounceRates-ExitRates:', dataset_corr.loc['BounceRates', 'ExitRates'])

print('\nKorelasi Revenue-PageValues:', dataset_corr.loc['Revenue', 'PageValues'])

print('\nKorelasi TrafficType-Weekend:', dataset_corr.loc['TrafficType', 'Weekend'])

"""# Eksplorasi Data: Memahami Data dengan Visual"""

import matplotlib.pyplot as plt
import seaborn as sns

# Checking the distribution of customers on Revenue
plt.rcParams['figure.figsize'] = (12, 5)
plt.subplot(1, 2, 1)
sns.countplot(dataset['Revenue'], palette = 'pastel')
plt.title('Buy or Not', fontsize = 20)
plt.xlabel('Revenue or Not', fontsize = 14)
plt.ylabel('count', fontsize = 14)

# Checking the distribution of customers on Weekend
plt.subplot(1, 2, 2)
sns.countplot(dataset['Revenue'], palette = 'inferno')
plt.title('Purchase on Weekend', fontsize = 20)
plt.xlabel('Weekend or Not', fontsize = 14)
plt.ylabel('count', fontsize = 14)
plt.show()

"""# Tugas Praktek"""

import matplotlib.pyplot as plt

# Visualizing the distribution of customers around the Region
plt.hist(dataset['Region'], color = 'lightblue')
plt.title('Distribution of Customers', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()

"""# Data Pre-processing: Handling Missing Value - Part 1"""

# Checking missing value for each feature
print('Checking missing balue for each feature:')
print(dataset.isnull().sum())

# Checking total missing value
print('Counting total missing value:')
print(dataset.isnull().sum().sum())

"""# Data Pre-processing: Handling Missing Value - Part 2"""

# Drop rows with missing value
dataset_clean = dataset.dropna()
print('Ukuran dataset_clean:', dataset_clean.shape)

"""# Data Pre-processing: Handling Missing Value - Part 3"""

print("Before imputation:")
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

print("\nAfter imputation:")
# Fill missing value with mean of feature value
dataset.fillna(dataset.mean(), inplace=True)
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

"""# Tugas Praktek"""

import pandas as pd
dataset1 = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')

print('Before imputation:')
# Checking missing value for each feature
print(dataset1.isnull().sum())
# Checking total missing value
print(dataset1.isnull().sum().sum())

print('After imputation:')
# Fill missing value with median of feature value
dataset1.fillna(dataset1.median(), inplace=True)
# Checking missing value for each feature
print(dataset1.isnull().sum())
# Checking total missing value
print(dataset1.isnull().sum().sum())

"""# Data Preprocessing: Scaling

# Tugas Praktek
"""

from sklearn.preprocessing import MinMaxScaler

# Define MinMaxScaler to scaler
scaler = MinMaxScaler()

# List all the feature that need to be scaled  
scaling_column = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']

# Apply fit_transform to scale selected feature
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])

# Checking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min', 'max']])

"""# Data Pre-processing: Konversi string ke numerik"""

import numpy as np
from sklearn.preprocessing import LabelEncoder
# Convert feature/column 'Month'
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')

# Convert feature/column 'VisitorType'
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))

"""# Features & Label"""

# Removing the target column Revenue from dataset and assigning to X
x = dataset.drop(['Revenue'], axis = 1)

# Assigning the target column Revenue to y
y = dataset['Revenue']

# Checking the shapes
print('Shape of x:', x.shape)
print('Shape of y:', y.shape)

"""# Training dan Test Dataset"""

from sklearn.model_selection import train_test_split

# Splitting the x and y
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Checking the shapes
print('Shape of x_train:', x_train.shape)
print('Shape of y_train:', y_train.shape)
print('Shape of x_test:', x_test.shape)
print('Shape of y_test:', y_test.shape)

"""# Training Model: Fit"""

from sklearn.tree import DecisionTreeClassifier

# Call the classifier
model = DecisionTreeClassifier()

# Fit the classifier to the training data
model = model.fit(x_train, y_train)

"""# Training Model: Predict"""

# Apply the classifier/model to the test data
y_pred = model.predict(x_test)
print(y_pred.shape)

"""# Evaluasi Model Performance"""

from sklearn.metrics import confusion_matrix, classification_report

# Evaluating the model
print('Training Accuracy:', model.score(x_train, y_train))
print('Testing Accuracy:', model.score(x_test, y_test))

# Confusion Matrix
print('\nConfusion matrix:')
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Classification_report
print('Classification report:')
cr = classification_report(y_test, y_pred)
print(cr)

"""# Pemodelan Permasalahan Klasifikasi dengan Logistic Regression"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Call the classifier
logreg = LogisticRegression()

# Fit the classfier to the training data
logreg = logreg.fit(x_train, y_train)

# Training Model: Predict
y_pred = logreg.predict(x_test)

# Evaluate Model Performance
print('Training Accuracy:', model.score(x_train, y_train))
print('Testing Accuracy:', model.score(x_test, y_test))

# Confusion Matrix
print('\nConfusion Matrix')
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Classification Report
print('\nClassification Report')
cr = classification_report(y_test, y_pred)
print(cr)

"""# Classification - Decision Tree

# Tugas Praktek
"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Splitting the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

# Call the classifier
decision_tree = DecisionTreeClassifier()

# Fit the classifier to the training data
decision_tree = decision_tree.fit(x_train, y_train)

# Evaluating the decision_tree performance
print('Training Accuracy:', decision_tree.score(x_train, y_train))
print('Testing Accuracy:', decision_tree.score(x_test, y_test))

"""# Regression: Linear Regression

# Tugas Praktek
"""

# Load dataset
import pandas as pd
housing = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/housing_boston.csv')

# Data rescaling
from sklearn import preprocessing
data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
housing[['RM','LSTAT','PTRATIO','MEDV']] = data_scaler.fit_transform(housing[['RM','LSTAT','PTRATIO','MEDV']])

# Getting Dependent and Independent Variables
X = housing.drop(['MEDV'], axis = 1)
y = housing['MEDV']

# checking the shapes
print('Shape of X:', X.shape)
print('Shape of y:', y.shape)

# Splitting the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Checking the shapes  
print('Shape of X_train :', X_train.shape)
print('Shape of y_train :', y_train.shape)
print('Shape of X_test :', X_test.shape)
print('Shape of y_test :', y_test.shape)

# Import regressor from Scikit-Learn
from sklearn.linear_model import LinearRegression

# Call the regressor
reg = LinearRegression()

# Fit the regressor to the training data  
reg = reg.fit(X_train, y_train)

# Apply the regressor/model to the test data  
y_pred = reg.predict(X_test)

"""# Regression Performance Evaluation"""

from sklearn.metrics import mean_squared_error, mean_absolute_error  
import numpy as np
import matplotlib.pyplot as plt 

# Calculating MSE, lower the value better it is. 0 means perfect prediction
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error of testing set:', mse)

# Calculating MAE
mae = mean_absolute_error(y_test, y_pred)
print('Mean absolute error of testing set:', mae)

# Calculating RMSE
rmse = np.sqrt(mse)
print('Root Mean Squared Error of testing set:', rmse)

"""# K-Means Clustering

# Tugas Praktek
"""

# Import Library
import pandas as pd
from sklearn.cluster import KMeans

# Load Dataset
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/mall_customers.csv')

# Selecting Features (default)
X = dataset[['annual_income', 'spending_score']]

# Define K-Means as cluster_model
cluster_model = KMeans(n_clusters = 5, random_state = 24)
labels = cluster_model.fit_predict(X)

"""# Tugas Praktek: Inspect & Visualizing the Cluster"""

# Import Library
import matplotlib.pyplot as plt

# Convert dataframe to array
X = X.values

# Separate X to xs and ys --> use for chart axis
xs = X[:,0]
ys = X[:,1]

# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(xs, ys, c=labels, alpha=0.5)

# Assign the cluster centers: centroids
centroids = cluster_model.cluster_centers_

# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]

# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x, centroids_y, marker='D', s=50)
plt.title('K Means Clustering', fontsize = 20)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

"""# Measuring cluster criteria
# Tugas Praktek
"""

# Import library
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Elbow Method - Inertia plot
inertia = []

# Looping the inertia calculation for each k
for k in range(1, 10):
    # Assign KMeans as cluster_model
    cluster_model = KMeans(n_clusters = k, random_state = 24)
    # Fit cluster_model to X
    cluster_model.fit(X)
    # Get the inertia value
    inertia_value = cluster_model.inertia_
    # Append the inertia_value to inertia list
    inertia.append(inertia_value)

# Inertia plot
plt.plot(range(1, 10), inertia)
plt.title('The Elbow Method - Inertia plot', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('Inertia')
plt.show()

"""# Mini Project

# Case Study: Promos for our e-commerce - Part 1
"""

# Import library 
import pandas as pd

# Baca data 'ecommerce_banner_promo.csv'
data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/ecommerce_banner_promo.csv')

#1. Data eksplorasi dengan head(), info(), describe(), shape
print("\n[1] Data eksplorasi dengan head(), info(), describe(), shape")
print("Lima data teratas:")
print(data.head())
print("Informasi dataset:")
print(data.info())
print("Statistik deskriptif dataset:")
print(data.describe())
print("Ukuran dataset:")
print(data.shape)

"""# Case Study: Promos for our e-commerce - Part 2"""

#2. Data eksplorasi dengan dengan mengecek korelasi dari setiap feature menggunakan fungsi corr()
print("\n[2] Data eksplorasi dengan dengan mengecek korelasi dari setiap feature menggunakan fungsi corr()")
print(data.corr())

#3. Data eksplorasi dengan mengecek distribusi label menggunakan fungsi groupby() dan size()
print("\n[3] Data eksplorasi dengan mengecek distribusi label menggunakan fungsi groupby() dan size()")
print(data.groupby('Clicked on Ad').size())

"""# Case Study: Promos for our e-commerce - Part 3"""

# Import library
import matplotlib.pyplot as plt
import seaborn as sns

# Seting: matplotlib and seaborn
sns.set_style('whitegrid')  
plt.style.use('fivethirtyeight')

# 4. Data eksplorasi dengan visualisasi
# 4a. Visualisasi Jumlah user dibagi ke dalam rentang usia (Age) menggunakan histogram (hist()) plot
plt.figure(figsize=(10, 5))
plt.hist(data['Age'], bins = data.Age.nunique())
plt.xlabel('Age')
plt.tight_layout()
plt.show()

# 4b. Gunakan pairplot() dari seaborn (sns) modul untuk menggambarkan hubungan setiap feature.
plt.figure()
sns.pairplot(data)
plt.show()

"""# Case Study: Promos for our e-commerce - Part 4"""

# 5. Cek missing value
print("\n[5] Cek missing value")
print(data.isnull().sum().sum())

"""# Case Study: Promos for our e-commerce - Part 5"""

# Import library
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 6.Lakukan pemodelan dengan Logistic Regression, gunakan perbandingan 80:20 untuk training vs testing
print("\n[6] Lakukan pemodelan dengan Logistic Regression, gunakan perbandingan 80:20 untuk training vs testing")

# 6a. Drop Non-Numerical (object type) feature from X, as Logistic Regression can only take numbers, and also drop Target/label, assign Target Variable to y.   
X = data.drop(['Ad Topic Line', 'City', 'Country', 'Timestamp', 'Clicked on Ad'], axis = 1)
y = data['Clicked on Ad']

# 6b. splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

# 6c. Modelling
# Call the classifier
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg = logreg.fit(X_train,y_train)

# Prediksi model
y_pred = logreg.predict(X_test)

# 6d. Evaluasi Model Performance
print("Evaluasi Model Performance:")
print("Training Accuracy :", logreg.score(X_train, y_train))
print("Testing Accuracy :", logreg.score(X_test, y_test))

"""# Case Study: Promos for our e-commerce - Part 6"""

# Import library
from sklearn.metrics import confusion_matrix, classification_report

# 7. Print Confusion matrix dan classification report
print("\n[7] Print Confusion matrix dan classification report")

# Apply confusion_matrix function to y_test and y_pred
print("Confusion matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Apply classification_report function to y_test and y_pred
print("Classification report:")
cr = classification_report(y_test, y_pred)
print(cr)

"""Model sudah sangat baik dalam memprediksi user yang akan mengklik website atau tidak, dapat dilihat dari nilai accuracy = 0.90; Dataset memiliki jumlah label yang seimbang (balance class), sehingga evaluasi performansi dapat menggunakan metrik Accuracy."""