import pandas as pd
from trimming import trim
from special_character import check_special_character
from reduce_memory import reduce_memory

data = pd.read_csv("titanic.csv")
data = trim(data)
check_special_character(data, ["!", "@"])
print(data.head())
data = reduce_memory(data)
data.to_parquet("titanic.parquet.gzip", compression="gzip", index=False)