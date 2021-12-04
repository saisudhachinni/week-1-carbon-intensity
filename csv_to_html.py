import pandas as pd
import numpy as np
  
  
df_new = pd.read_csv('carbon intensity.csv')
  
df_new = pd.ExcelWriter('carbon intensity.xlsx')
df_new.to_excel(GFG, index = False)
  
df_new.save()
