import dask.dataframe as dd
import time

start = time.time()
ddf = dd.read_csv(r'C:\data_science\dataset\atlas2010.csv', encoding='utf-8')
mortos_ano = ddf.groupby('ano')['mortos'].sum().compute()
print(mortos_ano)
end = time.time()