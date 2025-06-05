#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
# Carregando os dados coletados
data = pd.read_csv('../reports/tables/piastri_norris_laps_2025.csv')

#%%
# Garantindo que o tempo de volta seja interpretado como timedelta
data['LapTime'] = pd.to_timedelta(data['LapTime'])

#%%
# Lista dos pilotos
drivers = data['Driver'].unique()

# Lista dos GPs
gps = data['GrandPrix'].unique()

#%%
# Criar pasta para relatórios se não existir
import os
os.makedirs('../reports/tables', exist_ok=True)

# %%
# Calculando a média de tempo de volta por piloto e GP
mean_lap_times = data.groupby(['GrandPrix', 'Driver'])['LapTime'].mean().reset_index()

# Convertendo LapTime para segundos para facilitar a visualização
mean_lap_times['LapTime_sec'] = mean_lap_times['LapTime'].dt.total_seconds()

# Salvando a tabela
mean_lap_times.to_csv('../reports/tables/mean_lap_times.csv', index=False)

print('Tabela de média de tempo de volta salva em reports/tables/mean_lap_times.csv')

# %%
# Contar número de pit stops: voltas com tempo de entrada e saída de box não nulos
data['DidPit'] = data['PitInTime'].notnull() & data['PitOutTime'].notnull()

pit_counts = data[data['DidPit']].groupby(['GrandPrix', 'Driver']).size().reset_index(name='PitStops')

# Salvando a tabela
pit_counts.to_csv('../reports/tables/pit_stops.csv', index=False)

print('Tabela de número de pit stops salva em reports/tables/pit_stops.csv')

# %%
# Pegando a melhor volta de cada piloto por GP
best_laps = data.groupby(['GrandPrix', 'Driver'])['LapTime'].min().reset_index()

# Convertendo para segundos
best_laps['BestLap_sec'] = best_laps['LapTime'].dt.total_seconds()

# Salvando a tabela
best_laps.to_csv('../reports/tables/best_laps.csv', index=False)

print('Tabela de melhor volta salva em reports/tables/best_laps.csv')

# %%
# Pegando a última volta registrada por cada piloto em cada GP
final_positions = data.groupby(['GrandPrix', 'Driver']).apply(lambda x: x.sort_values('LapNumber').iloc[-1]).reset_index(drop=True)

# Mantendo só o necessário
final_positions = final_positions[['GrandPrix', 'Driver', 'Position']]

# Salvando a tabela
final_positions.to_csv('../reports/tables/final_positions.csv', index=False)

print('Tabela de posição final salva em reports/tables/final_positions.csv')

# %%
# Contar o uso de compostos de pneus
tyre_usage = data.groupby(['GrandPrix', 'Driver', 'Compound']).size().reset_index(name='Stints')

# Salvando a tabela
tyre_usage.to_csv('../reports/tables/tyre_usage.csv', index=False)

print('Tabela de uso de compostos de pneus salva em reports/tables/tyre_usage.csv')

# %%
# Sistema de pontuação oficial F1
points_dict = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10,
    6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}

# Adicionando coluna de pontos baseada na posição final
final_positions['Points'] = final_positions['Position'].map(points_dict).fillna(0)

# Garantindo que Points seja int
final_positions['Points'] = final_positions['Points'].astype(int)

# Acumulando pontos corrida a corrida
points_cumsum = final_positions.sort_values(['Driver', 'GrandPrix']).groupby('Driver').apply(
    lambda x: x.assign(CumulativePoints = x['Points'].cumsum())
).reset_index(drop=True)

# Salvando a tabela
points_cumsum.to_csv('../reports/tables/cumulative_points.csv', index=False)

print('Tabela de pontos acumulados salva em reports/tables/cumulative_points.csv')

# %%
# Calculando desvio padrão do tempo de volta por piloto e GP
lap_time_variability = data.groupby(['GrandPrix', 'Driver'])['LapTime'].std().reset_index()

# Convertendo para segundos
lap_time_variability['LapTime_std_sec'] = lap_time_variability['LapTime'].dt.total_seconds()

# Salvando a tabela
lap_time_variability.to_csv('../reports/tables/lap_time_variability.csv', index=False)

print('Tabela de variabilidade do tempo de volta salva em reports/tables/lap_time_variability.csv')
