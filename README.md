# Análise de Desempenho: Oscar Piastri vs Lando Norris - Temporada Fórmula 1 2025

## Objetivo

Este projeto tem como objetivo analisar e comparar o desempenho dos pilotos Oscar Piastri e Lando Norris ao longo da temporada 2025 da Fórmula 1. A análise aborda aspectos como tempos de volta, variabilidade de desempenho, estratégias de pit stop, uso de pneus e evolução dos pontos durante a temporada.

## Dados Utilizados

Os dados foram coletados e organizados em tabelas CSV contendo informações detalhadas de cada corrida, incluindo:

- **best_laps.csv**: Melhores voltas dos pilotos por GP
- **cumulative_points.csv**: Pontuação acumulada ao longo da temporada
- **final_positions.csv**: Posições finais e de largada em cada GP
- **lap_time_variability.csv**: Variabilidade dos tempos de volta
- **mean_lap_times.csv**: Tempos médios de volta por GP e piloto
- **piastri_norris_laps_2025.csv**: Dados detalhados das voltas de Piastri e Norris
- **pit_stops.csv**: Informações sobre paradas nos boxes
- **summary_table.csv**: Resumo geral da temporada para os pilotos analisados
- **tyre_usage.csv**: Uso de compostos de pneus em cada GP

## Principais Análises

- **Número de pit stops por corrida:** Quantidade e comparação entre os pilotos
- **Uso dos compostos de pneus:** Frequência e escolha de pneus em cada GP
- **Tempos médios de volta:** Heatmap comparativo entre pilotos e corridas
- **Evolução dos pontos acumulados:** Linha do tempo dos pontos conquistados
- **Radar chart comparativo:** Visualização das estatísticas médias por piloto
- **Posição de largada vs. posição final:** Dispersão das posições ao longo dos GPs

## Como Executar o Projeto

1. Clone este repositório em sua máquina local:
    ```bash
    git clone https://github.com/seuusuario/projeto-f1-piastri-norris-2025.git
    ```

2. Instale as dependências necessárias (recomenda-se usar um ambiente virtual):
    ```bash
    pip install -r requirements.txt
    ```

3. Certifique-se de que os arquivos CSV estejam na pasta `reports/tables/` conforme estruturado no projeto.

4. Execute o script principal para gerar as análises e visualizações:
    ```bash
    python app.py
    ```

5. Os gráficos serão exibidos usando bibliotecas de visualização (Matplotlib, Seaborn, Plotly).

---

## Observações

- O projeto foi desenvolvido para análise exploratória e visualização dos dados de desempenho dos pilotos na temporada de 2025.
- Adaptar caminhos e versões das bibliotecas conforme seu ambiente local.
- Sinta-se à vontade para contribuir com melhorias e novas análises!

---

## Autor

Seu Nome - [seulinkedin](https://www.linkedin.com/in/seuusuario)  
Projeto desenvolvido para fins educacionais e portfólio pessoal.
