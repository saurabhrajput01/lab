# -*- coding: utf-8 -*-
"""untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/saurabhrajput01/baa28b3c8e33b25f4f9ff5ec92b02413/untitled0.ipynb
"""

import pandas as pd
import numpy as np
info = np.array(['p','a','n','d','a'])
a = pd.Series(info)
print(a)

import pandas as pd
# a list of strings
x = ['python','pandas']
#calling data frame constructer on list
df = pd.DataFrame(x)
print(df)



import pandas as pd
import numpy as np
a = pd.Series(['java','c','c++',np.nan])
a.map({'java':'core'})

s = pd.Series(["a","b","c"])
name=("vals")
s.to_frame()

import pandas as pd
import matplotlib.pyplot as plt
emp = ['Parker','john','smith','william']
id = [102,107,109,114]
emp_series = pd.Series(emp)
id_series = pd.Series(id)
frame = {'Emp':emp_series,'ID':id_series}
result = pd.DataFrame(frame)
print(result)