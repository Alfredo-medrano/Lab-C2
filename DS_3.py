import pandas as pd
import matplotlib.pyplot as plt

# lee eñ csv
movies = pd.read_csv('DataSet_3.csv')

# Agrupar por título y obtener el promedio de los votos
movies_selection = movies.groupby('title')['vote_average'].mean().sort_values(ascending=False).head(5)

# grafico circular 
plt.figure(figsize=(8, 8))
plt.pie(movies_selection, labels=movies_selection.index, autopct='%1.1f%%', startangle=140,
        colors=['Violet', 'Purple', 'Green', 'gold', 'pink'], explode=[0.1, 0, 0, 0, 0])#separacion para que resalte la seccion que tenga mayor porcentaje
plt.title('Distribución de los promedios de votos de las películas')
plt.tight_layout()
plt.show()
