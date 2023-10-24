import pandas as pd
import geopandas as gpd
from shapely.wkt import loads
from shapely.geometry import MultiPolygon

# lendo e adequando os dados
df = pd.read_excel('data/2023_DiasColetasParcial.xls')

# resolvendo problema dos acentos
#df['coluna_com_problema'] = df['coluna_com_problema'].str.encode('latin-1').str.decode('utf-8')

# renomeando a label das colunas
df.rename(columns={'Circuito':'CO_CIRCUITO',
                   'Frequência':'FREQUENCIA',
                   'Observação':'NOME',
                   'PolygonZ':'GEOMETRY'}, inplace=True)

# removendo a setorizacao com geometria dos poligonos ausentes
df.dropna(subset=['GEOMETRY'], inplace=True)

# ajustando a coluna GEOMETRY para o formato correto
df['GEOMETRY'] = df['GEOMETRY'].apply(lambda x: x.replace(' 0',''))
df['GEOMETRY'] = 'POLYGON(('+df.GEOMETRY+'))'

# removendo colunas desnecessarias
df.drop(columns=['CO_CIRCUITO'], inplace=True)

# convertendo a coluna de texto WKT em geometrias
df['GEOMETRY'] = df['GEOMETRY'].apply(loads)

# criando um GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='GEOMETRY')

# convertendo em MultiPolygon
gdf['GEOMETRY'] = gdf['GEOMETRY'].apply(lambda geom: MultiPolygon([geom]))

# exportando para GeoJSON
gdf.to_file('ColetaDomiciliarSetorizacao.geojson', driver='GeoJSON', crs='EPSG:4326', encoding='utf-8')

#debug
gdf.to_csv('DEBUG_ColetaDomiciliarSetorizacao.csv', index=False, encoding='utf-8')