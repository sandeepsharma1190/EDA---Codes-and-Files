import pandas as pd

dataset = pd.read_csv('Adult Salary.csv', names = ['age',
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

dataset = dataset.dropna()

data = dataset.groupby('workclass')['hours-per-week'].sum()

data = {'Gender':['m', 'f', 'm', 'f', 'm', 'f', 'm'], 'Height': [10, 11, 9, 15, 7, 9, 11]}
df = pd.DataFrame(data)

m_filter = df['Gender'] == 'm'
mean_m_h = df[m_filter].mean()

f_filter = df['Gender'] == 'f'
mean_f_h = df[f_filter].mean()

df_com = pd.DataFrame({'Gender': ['m', 'f'], 'M_Height': [mean_m_h, mean_f_h]})
print(df_com)


df.groupby('Gender').mean()


ob_w = dataset.groupby('workclass')
ob_w
ob_w.groups


for name, group in ob_w:
    print(name, 'containes', group.shape[0], 'group')


ob_w.get_group(' Private')












