#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import plotly.express as px
import plotly.graph_objects as go
# %%
os.makedirs('../reports/figures', exist_ok=True)
# %%
# Carregando dados de pontos acumulados
points = pd.read_csv('../reports/tables/cumulative_points.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(data=points, x='GrandPrix', y='CumulativePoints', hue='Driver', marker='o')
plt.title('Pontuação Acumulada - Temporada 2025')
plt.xlabel('GP')
plt.ylabel('Pontos Acumulados')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../reports/figures/line_cumulative_points.png')
plt.close()
# %%
pit = pd.read_csv('../reports/tables/pit_stops.csv')

plt.figure(figsize=(10, 6))
sns.barplot(data=pit, x='GrandPrix', y='PitStops', hue='Driver')
plt.title('Número de Pit Stops por Corrida')
plt.xlabel('GP')
plt.ylabel('Pit Stops')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../reports/figures/bar_pit_stops.png')
plt.close()

# %%
tyres = pd.read_csv('../reports/tables/tyre_usage.csv')

plt.figure(figsize=(12, 6))
sns.barplot(data=tyres, x='GrandPrix', y='Stints', hue='Compound')
plt.title('Compostos Utilizados por Corrida')
plt.xlabel('GP')
plt.ylabel('Quantidade de Stints')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../reports/figures/bar_tyre_usage.png')
plt.close()

# %%
laps = pd.read_csv('../reports/tables/piastri_norris_laps_2025.csv')
laps['LapTime'] = pd.to_timedelta(laps['LapTime']).dt.total_seconds()

plt.figure(figsize=(10, 6))
sns.boxplot(data=laps, x='Driver', y='LapTime')
plt.title('Distribuição dos Tempos de Volta')
plt.xlabel('Piloto')
plt.ylabel('Tempo de Volta (s)')
plt.tight_layout()
plt.savefig('../reports/figures/boxplot_lap_times.png')
plt.close()

# %%
from math import pi

# Preparando dados
mean_lap = pd.read_csv('../reports/tables/mean_lap_times.csv')
final_pos = pd.read_csv('../reports/tables/final_positions.csv')
pit = pd.read_csv('../reports/tables/pit_stops.csv')
best = pd.read_csv('../reports/tables/best_laps.csv')

summary = {}

for driver in ['PIASTRI', 'NORRIS']:
    pos_med = final_pos[final_pos['Driver'] == driver]['Position'].mean()
    lap_med = mean_lap[mean_lap['Driver'] == driver]['LapTime_sec'].mean()
    best_lap = best[best['Driver'] == driver]['BestLap_sec'].min()
    pit_med = pit[pit['Driver'] == driver]['PitStops'].mean()
    
    summary[driver] = [pos_med, lap_med, best_lap, pit_med]

# Radar chart
categories = ['Posição Média', 'Tempo Médio (s)', 'Melhor Volta (s)', 'Pit Stops Médios']
fig = go.Figure()

for driver in summary:
    fig.add_trace(go.Scatterpolar(
        r=summary[driver],
        theta=categories,
        fill='toself',
        name=driver
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True)
    ),
    showlegend=True,
    title='Radar Chart - Comparação de Desempenho'
)

fig.write_image('../reports/figures/radar_chart.png')

# %%
# Estimando posição de largada pela primeira volta
first_laps = laps[laps['LapNumber'] == 1][['GrandPrix', 'Driver', 'Position']]
first_laps = first_laps.rename(columns={'Position': 'StartPosition'})

final_pos = pd.read_csv('../reports/tables/final_positions.csv')

# Mesclando
positions = pd.merge(first_laps, final_pos, on=['GrandPrix', 'Driver'], suffixes=('_Start', '_Final'))

plt.figure(figsize=(8, 6))
sns.scatterplot(data=positions, x='StartPosition', y='Position', hue='Driver')
plt.plot([1, 20], [1, 20], 'k--', label='Sem mudanças')
plt.title('Posição de Largada x Posição Final')
plt.xlabel('Largada')
plt.ylabel('Final')
plt.legend()
plt.tight_layout()
plt.savefig('../reports/figures/scatter_start_vs_final.png')
plt.close()

# %%
# Exemplo simples: tempo médio de volta por GP e piloto

heat = laps.groupby(['GrandPrix', 'Driver'])['LapTime'].mean().reset_index()
heat_pivot = heat.pivot(index='Driver', columns='GrandPrix', values='LapTime')

plt.figure(figsize=(12, 6))
sns.heatmap(heat_pivot, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Tempo Médio de Volta por GP')
plt.xlabel('GP')
plt.ylabel('Piloto')
plt.tight_layout()
plt.savefig('../reports/figures/heatmap_avg_lap.png')
plt.close()
