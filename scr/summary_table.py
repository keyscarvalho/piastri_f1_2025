#%%
import pandas as pd
import os

tables_dir = '../reports/tables/'
summary_file = os.path.join(tables_dir, 'summary_table.csv')

# Carregar tabelas
points = pd.read_csv(os.path.join(tables_dir, 'cumulative_points.csv'))
final_pos = pd.read_csv(os.path.join(tables_dir, 'final_positions.csv'))
lap_times = pd.read_csv(os.path.join(tables_dir, 'mean_lap_times.csv'))
best_laps = pd.read_csv(os.path.join(tables_dir, 'best_laps.csv'))
pit_stops = pd.read_csv(os.path.join(tables_dir, 'pit_stops.csv'))

# === Conversões necessárias ===

lap_times['LapTime'] = pd.to_timedelta(lap_times['LapTime']).dt.total_seconds()
best_laps['BestLapTime'] = pd.to_timedelta(best_laps['BestLapTime']).dt.total_seconds()

final_pos['FinalPosition'] = pd.to_numeric(final_pos['FinalPosition'], errors='coerce')
pit_stops['PitStops'] = pd.to_numeric(pit_stops['PitStops'], errors='coerce')

# ===== 1. Pontos Totais =====
points_total = points.groupby('Driver')['Points'].max().reset_index()
points_total.rename(columns={'Points': 'Pontos Totais'}, inplace=True)

# ===== 2. Posição Média =====
pos_media = final_pos.groupby('Driver')['FinalPosition'].mean().reset_index()
pos_media.rename(columns={'FinalPosition': 'Posição Média'}, inplace=True)
#%%
# ===== 3. Tempo Médio de Volta =====
lap_media = lap_times.groupby('Driver')['LapTime_sec'].mean().reset_index()
lap_media.rename(columns={'LapTime_sec': 'Tempo Médio de Volta (s)'}, inplace=True)

# # ===== 4. Melhor Volta =====
best_lap = best_laps.groupby('Driver')['BestLap_sec'].min().reset_index()
best_lap.rename(columns={'BestLap_sec': 'Melhor Volta (s)'}, inplace=True)

#%%


# ===== 5. Média de Pit Stops =====
pit_media = pit_stops.groupby('Driver')['PitStops'].mean().reset_index()
pit_media.rename(columns={'PitStops': 'Média de Pit Stops'}, inplace=True)

# ===== 6. Unir tudo =====
summary = points_total.merge(pos_media, on='Driver') \
                      .merge(lap_media, on='Driver') \
                      .merge(best_lap, on='Driver') \
                      .merge(pit_media, on='Driver')

# ===== 7. Salvar =====
summary.to_csv(summary_file, index=False)

print(f"Tabela resumo gerada e salva em: {summary_file}")

