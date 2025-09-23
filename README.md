<<<<<<< HEAD
# Hackathon Forecast Big Data 2025

## Objetivo
=======
🛒 Hackathon Forecast Big Data 2025
🎯 Objetivo
>>>>>>> fd281fd (add src modules, notebooks e docs; update README)

Este projeto foi desenvolvido como solução para o desafio do Hackathon Forecast Big Data 2025, com o objetivo de prever a quantidade semanal de vendas por PDV/SKU para as cinco semanas de janeiro/2023, com base no histórico de 2022.

A previsão de demanda é um problema real enfrentado por empresas de varejo e distribuição, sendo parte essencial de produtos como o One-Click Order (OCO) da BigData Tech
.

<<<<<<< HEAD
### Visão Estratégica
=======
💡 Visão Estratégica
>>>>>>> fd281fd (add src modules, notebooks e docs; update README)

A solução vai além de um modelo de previsão. Foi construída com base em:

Entendimento profundo do negócio (sortimento, ruptura, margem, elasticidade)

Robustez técnica (Optuna, SHAP, N-BEATSx, Ensemble, decomposição)

Clareza operacional: impacto direto em ruptura evitada, markdown e margem preservada

Escalabilidade: pipeline modular, automatizado e adaptável

<<<<<<< HEAD
### Estrutura do Projeto

Organizado em notebooks Jupyter numerados, cada um representando uma etapa clara do pipeline:

1. EDA & Pré-processamento

Durante a fase de EDA (Análise Exploratória de Dados), foram aplicadas as seguintes transformações:

- Conversão de datas para semana ISO (corrigindo `semana` para formato `int` de 1 a 52).
- Exclusão de colunas redundantes (ex: `reference_date`, `gross_value`, `net_value`, `estimated_cost_ops`, `estimated_net_profit`, etc.)
- Tratamento de variáveis categóricas: padronização e verificação de cardinalidade.
- Correlação de variáveis numéricas via Pearson (eliminação de multicolinearidade).
- Extração de features temporais:
  - `num_semana`: número da semana ISO (1 a 52)
  - `idade`: tempo de vida do produto na base
  - `ano`: extraído da semana
- Definição de variáveis a manter para modelagem:
  - Categóricas: `categoria`, `categoria_pdv`, `marca`, `premise`, `produto`, `pdv`
  - Numérica alvo: `quantidade`
  - Temporais: `semana`
- Exclusão de variáveis que não agregam à previsão (ex: `label`, `distributor_id`, etc.)

Os dados processados foram salvos em `data/processed/` para uso nos modelos.

---


### 📚 Referências Utilizadas
=======
📁 Estrutura do Projeto

Organizado em notebooks Jupyter numerados, cada um representando uma etapa clara do pipeline:

📈 Resultados e Métricas

⚠️ Resultados abaixo serão atualizados após execução completa dos notebooks.

WMAPE (Total): xx.x%

Redução de ruptura: xx.x%

Receita preservada: R$ xxx mil

Precisão do N-BEATSx: até x% sobre baseline nas séries curtas

Margem evitada por overforecast: R$ xx mil

Melhoria frente ao modelo Naive: +xx% em acurácia geral

📚 Referências Utilizadas
>>>>>>> fd281fd (add src modules, notebooks e docs; update README)

BigData Tech

One-Click Order e Price Optimization (documentos internos)

ai-driven-operations-forecasting-in-data-light-environments.pdf (BCG)

Demand Forecasting II - HBR

Materiais próprios:

Demand Forecasting: Concept, Significance, Objectives and Factors

Recap - Monetization & Pricing Strategy
<<<<<<< HEAD
=======

✨ Considerações Finais

Este projeto é fruto de resiliência, consistência e paixão por dados.

A ideia foi construir algo completo, robusto, e com aplicabilidade real. Cada etapa foi pensada para entregar valor de negócio com clareza técnica.

Mais do que uma submissão, esse repositório representa minha evolução como profissional e minha visão sobre o poder da ciência de dados aplicada a problemas reais de negócio.
>>>>>>> fd281fd (add src modules, notebooks e docs; update README)
