import numpy as np
import pandas as pd
np.random.seed(0)
df1 = pd.DataFrame(np.random.randint(0,10,size=(5, 6)), columns=list('ABCDEF'))
print(df1)
print(df1.head(2)[['A','B']])