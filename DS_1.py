import pandas as pd
import matplotlib.pyplot as plt

# lee el csv
marvel_DC = pd.read_csv('DataSet_1.csv')

# foltra las peliculas 
filtered_marvel_dc = marvel_DC[marvel_DC['IMDB_Score'] > 0]

# selecciona las primeras 10 peliculas en orden 
marvel_dc_selection = filtered_marvel_dc[['Movie', 'IMDB_Score']].head(10).sort_values('IMDB_Score', ascending=False)
#colores para las barras
colores = ["Red", "Blue", "Pink", "Black", "Green", "Orange", "Purple", "Brown", "Cyan", "Magenta"]

#el apartado grafico 
plt.figure(figsize=(10, 6))
plt.bar(marvel_dc_selection['Movie'], marvel_dc_selection['IMDB_Score'], color=colores[:len(marvel_dc_selection)])
plt.xticks(range(len(marvel_dc_selection)), marvel_dc_selection['Movie'], rotation=45, ha='right')
plt.xlabel('Movie')
plt.ylabel('IMDB Score')
plt.title('IMDB Puntuaciones de películas de Marvel vs DC')
plt.tight_layout()
plt.show()