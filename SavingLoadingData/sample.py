import numpy as np
my_numpy_array = np.random.rand(3)
type(my_numpy_array)
my_numpy_array[0]
import pandas as pd
my_series = pd.Series(my_numpy_array)
my_series[0]
my_series = pd.Series(my_numpy_array, index=["First","Second", "Third"])
my_series["First"]
my_series
my_series.index
array_2d = np.random.rand(3,2)
df=pd.DataFrame(array_2d)
df
df.columns = ["First", "Second"]
