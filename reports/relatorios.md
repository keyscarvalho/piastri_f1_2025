# Relatório de Análise: Desempenho de Oscar Piastri vs Lando Norris na Temporada Fórmula 1 2025

## 1. Introdução

A Fórmula 1 é uma das modalidades esportivas mais competitivas e tecnologicamente avançadas do mundo. Nesta análise, focamos na comparação entre dois pilotos promissores da temporada 2025: Oscar Piastri e Lando Norris, ambos da equipe McLaren. O objetivo principal é avaliar o desempenho de cada piloto ao longo das corridas, considerando métricas como tempos de volta, estratégias de pit stop, variabilidade de performance e uso de pneus.

## 2. Dados Utilizados

Para realizar esta análise, foram utilizados dados estruturados em diferentes tabelas CSV contendo informações detalhadas das corridas da temporada:

- **best_laps.csv**: melhores voltas de cada piloto por GP.
- **cumulative_points.csv**: evolução dos pontos acumulados durante a temporada.
- **final_positions.csv**: posições de largada e chegada em cada corrida.
- **lap_time_variability.csv**: variabilidade dos tempos de volta.
- **mean_lap_times.csv**: tempos médios por piloto e GP.
- **piastri_norris_laps_2025.csv**: voltas detalhadas de Piastri e Norris.
- **pit_stops.csv**: dados sobre paradas nos boxes.
- **summary_table.csv**: resumo geral da temporada.
- **tyre_usage.csv**: uso dos diferentes compostos de pneus.

## 3. Metodologia

Os dados foram processados utilizando Python e bibliotecas como Pandas para manipulação, Matplotlib e Seaborn para visualização, e Plotly para gráficos interativos. O projeto seguiu as etapas:

1. **Carregamento e limpeza dos dados:** remoção de inconsistências e preparação para análise.
2. **Filtragem por Grandes Prêmios selecionados:** para foco na comparação dos pilotos.
3. **Análises exploratórias:** geração de tabelas resumo e gráficos para identificar padrões e diferenças.
4. **Visualizações específicas:** heatmaps, gráficos de barras, linha temporal, radar charts e scatter plots para insights detalhados.

## 4. Principais Resultados

- **Tempos de volta:** Piastri apresentou tempos médios levemente inferiores aos de Norris, indicando maior consistência em algumas corridas.
- **Variabilidade de performance:** Norris mostrou maior variação nos tempos, possivelmente refletindo estratégias de corrida mais agressivas ou condições variáveis.
- **Pit stops:** O número e o timing dos pit stops diferiram entre os pilotos, influenciando diretamente nos resultados de corrida.
- **Uso dos pneus:** Ambos os pilotos usaram os compostos de pneus de maneira estratégica, adaptando-se às condições específicas de cada GP.
- **Evolução dos pontos:** A análise da pontuação acumulada mostra momentos de recuperação e picos de desempenho ao longo da temporada.

## 5. Conclusões

O estudo revelou nuances importantes na comparação entre Piastri e Norris, mostrando que além do talento individual, fatores como estratégia de corrida, consistência e escolhas táticas impactam diretamente no desempenho geral. As análises fornecem um panorama detalhado para entender melhor a dinâmica da equipe McLaren e dos seus pilotos.

## 6. Sugestões para Trabalhos Futuros

- Incluir análise de telemetria para avaliar estilo de pilotagem.
- Explorar dados meteorológicos para entender impacto nas estratégias.
- Expandir a comparação para incluir outros pilotos e equipes.
- Desenvolver dashboard interativo para visualização dinâmica dos dados.

## 7. Referências

- Dados extraídos da temporada oficial da Fórmula 1 2025.
- Documentação das bibliotecas utilizadas: Pandas, Matplotlib, Seaborn, Plotly.
- Literatura sobre análise esportiva e estratégias na Fórmula 1.

---

## Apêndices

### A. Estrutura dos arquivos CSV

Breve descrição das colunas presentes em cada arquivo de dados utilizado.

