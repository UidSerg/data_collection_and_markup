import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn
from sklearn.preprocessing import LabelEncoder #pip install scikit-learn - инструмент для кодирования категориальных переменных
from sklearn.preprocessing import StandardScaler
from scipy import stats # pip install scipy - библиотека для научных и математических вычислений




# установка стиля и цветовой палитры для графиков
sns.set(style='whitegrid')
# загрузка данных
file_path = "./seminar_8/googleplaystore.csv"
df = pd.read_csv(file_path)
print('первые строки датасета')
print(df.head())
print(df.describe())
# print(df.stats())

numeric_cols = df.select_dtypes(include=[np.number]) # выбор числовых колонок
df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean) # замена пропущенных значений на среднее
print(df[numeric_cols.columns])

categoria_cols = df.select_dtypes(include=['object']) # выбор категориальных колонок
df[categoria_cols.columns] = categoria_cols.fillna(categoria_cols.mode().iloc[0]) 
print(df[categoria_cols.columns])
df.drop_duplicates(inplace=True)

"""
# графическая обработка
plt.figure(figsize=(10,6))
sns.histplot(df['Rating'], kde=True, color='skyblue')
plt.title("Distr of App rating")
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(y='Category', data=df, order=df['Category'].value_counts().index, palette='viridis', legend=False)  ## vs ругается что устарело
plt.title("App Distr across Categories")
plt.show()

plt.figure(figsize=(7,5))
sns.countplot(x="Type", data=df)
plt.title("Free vs Paid")
plt.show()
"""

# обнаружение и обработка выбросов
z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number))) # z оценки для числовых переменных
df = df[(z_scores<3).all(axis=1)] # удаление строк с выбросами
# Эта строка выполняет фильтрацию строк в DataFrame df  на основе условия, связанного с Z оценками (z-scores) 

# стандартизация данных (числовых переменных)
df_standardized = df.copy() # копия датафрейма
#df_standardized[numeric_cols.columns] = (df_standardized[numeric_cols.columns] - df_standardized[numeric_cols.columns].mean()) / df_standardized[numeric_cols.columns].std() 

# создание доп столбца
label_encoder = LabelEncoder()
df['Type_Encoded'] = label_encoder.fit_transform(df['Type']) # преобразование категорийной переменной в числовую

df = pd.get_dummies(df, columns=["Content Rating"], prefix='ContentRating', drop_first=True)
#df = pd.get_dummies(df, columns=["Category"], prefix='Category', drop_first=True)
# создание сводной таблицы
pivot_table = df.pivot_table(index='Category', columns='ContentRating_Teen', values="Rating", aggfunc='mean') # создание сводной таблицы средних
print('\n сводная таблица')
print(pivot_table)

# сохранение
output_file_path = 'clear_gapps.csv'
df.to_csv(output_file_path, index=False)
