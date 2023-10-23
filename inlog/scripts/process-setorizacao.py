import pandas as pd
import geopandas as gpd
from shapely.wkt import loads

# lendo e adequando os dados
df = pd.read_csv('data/2023_DiasColetasParcial.csv', 
                 sep=';', 
                 dtype={'Circuito':'category',
                        'Frequencia': str,
                         'Nome':str,
                         'PolygonZ':str})

# renomeando a label das colunas
df.rename(columns={'Circuito':'CO_CIRCUITO',
                   'Frequencia':'FREQUENCIA',
                   'Nome':'NOME',
                   'PolygonZ':'GEOMETRY'}, inplace=True)

# removendo a setorizacao com geometria dos poligonos ausentes
df.dropna(subset=['GEOMETRY'], inplace=True)

# ajustando a coluna GEOMETRY para o formato correto
df['GEOMETRY'] = df['GEOMETRY'].apply(lambda x: x.replace(' 0',''))
df['GEOMETRY'] = 'POLYGON (('+df.GEOMETRY+'))'

# removendo colunas descenessarias
df.drop(columns=['CO_CIRCUITO'], inplace=True)

# convertendo a coluna de texto WKT em geometrias
df['GEOMETRY'] = df['GEOMETRY'].apply(loads)

# criando um GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='GEOMETRY')

# exportando para GeoJSON
gdf.to_file('ColetaDomiciliarSetorizacao.geojson', driver='GeoJSON', crs='EPSG:4326')
