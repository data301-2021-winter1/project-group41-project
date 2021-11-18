import pandas as pd
import numpy as np
df1 = pd.read_csv("../data/raw/recognition_by_generation.csv")

def load_and_process(url_or_path_to_csv_file):
    
    df8 = ( pd.read_csv("../data/raw/time_series_90s.csv")
    .rename(columns={'years_old_13': 'years_old_13(2003)', 'years_old_12': 'years_old_12(2002)','years_old_11': 'years_old_11(2001)','years_old_10': 'years_old_10(2000)','years_old_9': 'years_old_9(1999)','years_old_8': 'years_old_8(1998)', 'years_old_7': 'years_old_7(1997)','years_old_6': 'years_old_6(1996)', 'years_old_5': 'years_old_5(1995)','years_old_4': 'years_old_4(1994)','years_old_3': 'years_old_3(1993)','years_old_2': 'years_old_2(1992)','years_old_1': 'years_old_1(1991)','years_old_0': 'years_old_0(1990)','years_pre_birth_1':'years_pre_birth_1 (1989)','years_pre_birth_2':'years_pre_birth_2 (1988)','years_pre_birth_3':'years_pre_birth_3 (1987)','years_pre_birth_4':'years_pre_birth_4 (1986)', 'years_pre_birth_5':'years_pre_birth_5 (1985)' ,'years_pre_birth_6':'years_pre_birth_6 (1984)' ,'years_pre_birth_7':'years_pre_birth_7 (1983)','years_pre_birth_8':'years_pre_birth_8 (1982)','years_pre_birth_9':'years_pre_birth_9 (1981)','years_pre_birth_10':'years_pre_birth_10 (1980)','years_pre_birth_11':'years_pre_birth_11 (1979)','years_pre_birth_12':'years_pre_birth_12 (1978)','years_pre_birth_13':'years_pre_birth_13 (1977)'})
    .merge(df1)
    .reset_index(drop=True)
    .sort_values("mean_millennial_recognition", ascending=False)
    
)
 


    return df8





 


    



