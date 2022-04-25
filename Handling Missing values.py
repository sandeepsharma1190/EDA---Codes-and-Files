import pandas as pd
import numpy as np


dataset = pd.read_csv('adult.csv', names = ['age',
                                          'workclass',
                                          'fnlwgt',
                                          'education',
                                          'education-num',
                                          'marital-status',
                                          'occupation',
                                          'relationship',
                                          'race',
                                          'gender',
                                          'capital-gain',
                                          'capital-loss',
                                          'hours-per-week',
                                          'native-country',
                                          'salary'],
                        na_values = ' ?')


dataset.isnull().sum()


# 1 way
test_dataset = dataset.iloc[:, [1, 6, 13]]
test_dataset.isnull().sum()

from sklearn.impute import SimpleImputer
si = SimpleImputer(missing_values=np.nan, strategy='mean')

test_dataset = si.fit_transform(test_dataset)
test_dataset = pd.DataFrame(test_dataset)

test_dataset.isnull().sum()


# 2 way
test_dataset = dataset.iloc[:, [1, 6, 13]]
test_dataset.isnull().sum()

test_dataset.iloc[:, 0].value_counts()
test_dataset.iloc[:, 1].value_counts()
test_dataset.iloc[:, 2].value_counts()

test_dataset.iloc[:, 0] = test_dataset.iloc[:, 0].fillna(' Private')
test_dataset.iloc[:, 1] = test_dataset.iloc[:, 1].fillna(' Prof-specialty')
test_dataset.iloc[:, 2] = test_dataset.iloc[:, 2].fillna(' United-States')

test_dataset.isnull().sum()



dataset.iloc[:, [1, 6, 13]] = test_dataset


