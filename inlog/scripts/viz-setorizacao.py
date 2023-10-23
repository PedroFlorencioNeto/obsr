import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# carregando o arquivo GeoJSON
gdf_setorizacao = gpd.read_file('ColetaDomiciliarSetorizacao.geojson')
gdf_bairros = gpd.read_file('data/shp_bairros/Fortaleza_Bairros.shp')

fig, ax = plt.subplots(figsize=(10,10))

# plotando os dados
gdf_bairros.boundary.plot(ax=ax, linewidth=0.3, color='black')
gdf_setorizacao.plot(ax=ax, column='FREQUENCIA', cmap='tab20b', legend=True)

# exibindo o gráfico
ax.set_title('Setores de Coleta Domiciliar em Fortaleza')

# adicione uma legenda manualmente abaixo do mapa

plt.axis('off')
plt.show()