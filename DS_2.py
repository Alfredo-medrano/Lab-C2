import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
balon_oro = pd.read_csv('DataSet_2.csv')

# Ordenar los datos orden descendente y seleccionar los 10 mejores jugadores
seleccion_balon_oro = balon_oro[['player', 'team', 'Performance_misc-Recov']].sort_values('Performance_misc-Recov', ascending=False).head(10)

# Concatenar el nombre del jugador con su equipo para las etiquetas
seleccion_balon_oro['label'] = seleccion_balon_oro['player'] + ' (' + seleccion_balon_oro['team'] + ')'


# Agregar etiquetas de datos
for i, value in enumerate(seleccion_balon_oro['Performance_misc-Recov']):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=9, color='black')
plt.figure(figsize=(12, 8))
plt.plot(seleccion_balon_oro['label'], seleccion_balon_oro['Performance_misc-Recov'], marker='s', linestyle='-', color='black')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Jugador (Equipo)')
plt.ylabel('Recuperaciones')
plt.title("Top 10 Jugadores Nominados al Balón de Oro 2024")
plt.tight_layout()
plt.show()