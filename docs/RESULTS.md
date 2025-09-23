# RESULTS.md

## Resumo
- **Objetivo**: prever quantidade semanal (PDV×SKU) para W01–W05/2023.  
- **Métrica oficial**: WMAPE (micro).  
- **Melhor submissão**: **S2 — LGBM+Optuna** · **WMAPE=0.6389** · **Rank: 13º**.  
- **Stack**: Pandas/DuckDB/LightGBM/Optuna.  
- **Anti-vazamento**: valores financeiros só via **lags**; treino restrito a 2022.

## Leaderboard (equipes)
| Submissão | WMAPE | Observações |
|---|---:|---|
| S1 – baseline naïve/mean4 | — | sanity check |
| **S2 – LGBM+Optuna** | **0.6389** | melhor até o encerramento |
| S3 – heurística recência+sazonal | >0.6389 | piorou vs S2 |
| S-last tight/boost | pendente | não superou S2 |

## Dados e EDA essencial
- **Cobertura e chaves**: merge 100% PROD, 100% PDV; `pdv×produto×semana` sem duplicatas.  
- **Qualidade**: `quantity` ≥0; `price=net_value/quantity` winsor 1%/99% para gráficos.  
- **Temporal**: série 2022 On/Off mostra pico anômalo em W37–W38; **flag** (`anomaly_flag`) para uso apenas em rollings.  
- **Sazonalidade**: `season_idx` de Jan por `categoria×premise` usada para ajustar heurísticas.  
- **Forecastability**: mix com alta intermitência em cauda; GBM > métodos puramente lineares.  

## Features (FE)
- **Transacionais** por PDV×SKU: `qty_lag{1,2,3,4,8,12}`, `qty_mean_{4,8,12}`.  
- **Preço/valor**: `price_lag{1,4}`, `gv_lag{1,4}`, `gp_lag{1,4}` (apenas lags).  
- **Sazonais**: `w_sin/w_cos`.  
- **Densidade**: `sku_active_pdv` (ativos na semana).  
- **Categóricas**: `premise,categoria,marca,fabricante,tipos,categoria_pdv` (category).

## Modelagem
- **Modelo**: LightGBM Regressor (`goss`, `num_leaves≈187`, `lr≈0.015`, regularização L1/L2).  
- **Validação**: `TimeSeriesSplit` em 2022; **seleção por WMAPE micro** no fold.  
- **Baseline**: naïve last-week e média W49–W52 com ajuste de Jan; S2 > baselines.

## Decisões de desenho
- Nada de `zipcode` granular; se necessário, `zip3/densidade`.  
- `gross_value/net_value/gross_profit` **não contemporâneo** no treino.  
- W37–W38 **não removidas** do dataset, só mascaradas em rollings/flags.

## Conexão com portfólio Big Data
- **OCO**: quadrantes **Quantidade×GP** por canal guiam sortimento e nível de serviço.  
- **PriceO**: `price_per_unit` + elasticidade rápida por **Marca×Premise** orientam ajustes.  
- **TargAtom**: metas bottom-up por PDV via potencial (medianas 12s, momentum 4–8 vs 12–26).  
- **Media Hero**: PDVs Q1 e pareto 80/20 mapeiam praças com melhor retorno de mídia.

## Reprodutibilidade
```bash
pip install -r requirements.txt
# EDA
jupyter nbopen notebooks/01_EDA_FE.ipynb
# FE+FS+LGBM
jupyter nbopen notebooks/02_FE_FS_LGBM.ipynb

