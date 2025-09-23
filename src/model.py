import pandas as pd
import lightgbm as lgb

def fit_lgbm(train: pd.DataFrame, X_cols, y_col, params: dict, num_boost_round=5000,
             early_stopping_rounds=200):
    dtrain = lgb.Dataset(train[X_cols], label=train[y_col])
    model = lgb.train(
        params | {'objective':'regression','metric':'mae','verbosity':-1},
        dtrain,
        num_boost_round=num_boost_round,
        valid_sets=[dtrain],
        valid_names=['train'],
        early_stopping_rounds=early_stopping_rounds,
        verbose_eval=False
    )
    return model, (model.best_iteration or num_boost_round)

def forecast_jan_2023(base_weekly: pd.DataFrame, model, X_cols):
    KEY  = ['premise','pdv','produto']
    hist = base_weekly.copy()
    out  = []
    for wk in [1,2,3,4,5]:
        grid = (hist[hist['iso_year']==2022][KEY].drop_duplicates()
                .assign(iso_year=2023, iso_week=wk, qty=0.0, gv=0.0, gp=0.0))
        tmp  = pd.concat([hist, grid], ignore_index=True)
        from fe import add_lag_feats
        tmp  = add_lag_feats(tmp)
        cur  = tmp[(tmp['iso_year']==2023) & (tmp['iso_week']==wk)].copy()
        cur['qty'] = model.predict(cur[X_cols]).clip(min=0.0)
        out.append(cur[KEY+['iso_year','iso_week','qty']])
        hist = pd.concat([hist, cur[hist.columns]], ignore_index=True)
    return pd.concat(out, ignore_index=True)