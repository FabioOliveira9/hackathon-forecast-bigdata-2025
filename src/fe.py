import numpy as np
import pandas as pd

KEY  = ['premise','pdv','produto']
TIME = ['iso_year','iso_week']

def add_lag_feats(df_in: pd.DataFrame) -> pd.DataFrame:
    df = df_in.sort_values(KEY + TIME).copy()
    g  = df.groupby(KEY, sort=False)

    for L in [1,2,3,4,8,12]:
        df[f'qty_lag{L}'] = g['qty'].shift(L)
    for W in [4,8,12]:
        df[f'qty_mean_{W}'] = g['qty'].shift(1).rolling(W, min_periods=1).mean()

    for L in [1,4]:
        df[f'price_lag{L}'] = g['price'].shift(L)
        df[f'gv_lag{L}']    = g['gv'].shift(L)
        df[f'gp_lag{L}']    = g['gp'].shift(L)

    df['sku_active_pdv'] = df.groupby(KEY + TIME)['produto'].transform('size')
    df['w_sin'] = np.sin(2*np.pi*df['iso_week']/53.0)
    df['w_cos'] = np.cos(2*np.pi*df['iso_week']/53.0)
    df['year_week'] = (df['iso_year']*100 + df['iso_week']).astype('int32')
    return df