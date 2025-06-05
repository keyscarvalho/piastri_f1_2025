#%%
# Importação das bibliotecas necessárias
import fastf1
from fastf1 import plotting
from fastf1.core import Laps
import pandas as pd
import os

#%%
# Configurações iniciais
fastf1.Cache.enable_cache('../data/cache')  # Ativando o cache para evitar downloads repetidos

#%%
# Definindo pilotos e número de corridas
drivers = ['PIA', 'NOR']  # Abreviações de Piastri e Norris
rounds = list(range(1, 10))  # GPs 1 a 9

#%%
# Função para coletar e preparar dados de uma corrida
def collect_race_data(year, rnd, drivers):
    # Carrega a sessão de corrida (Race)
    session = fastf1.get_session(year, rnd, 'R')
    session.load()
    
    # Obtém todas as voltas da corrida
    laps = session.laps

    # Filtra apenas os dados dos dois pilotos
    driver_laps = laps[laps['Driver'].isin(drivers)].copy()

    # Adiciona informações úteis
    driver_laps['GrandPrix'] = session.event['EventName']
    driver_laps['RoundNumber'] = rnd

    # Retorna DataFrame com as voltas dos dois pilotos
    return driver_laps

#%%
# Lista para armazenar todos os DataFrames das corridas
all_races_laps = []

# Loop para coletar dados das 9 primeiras corridas
for rnd in rounds:
    try:
        race_laps = collect_race_data(2025, rnd, drivers)
        all_races_laps.append(race_laps)
        print(f'Dados coletados para a corrida {rnd}')
    except Exception as e:
        print(f'Erro ao coletar dados da corrida {rnd}: {e}')

#%%
# Concatenar todos os DataFrames em um só
all_laps_df = pd.concat(all_races_laps, ignore_index=True)

#%%
# Salvar o DataFrame bruto para uso posterior
os.makedirs('../reports/', exist_ok=True)
all_laps_df.to_csv('../reports/tables/piastri_norris_laps_2025.csv', index=False)

print('Coleta e preparo dos dados finalizados. Arquivo salvo em data/piastri_norris_laps_2025.csv')