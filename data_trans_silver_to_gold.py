# Data Transformation from silver to gold layer
# Column name transformation in all the tables

dbutils.fs.ls('mnt/silver/SalesLT')

dbutils.fs.ls('mnt/gold/')

from pyspark.sql import SaprkSession
from pyspark.functions import col, regexp_replace

table_name = []

for i in dbutils.fs.ls('/mnt/silver/SalesLT'):
    table_name.append(i.name.split('/'[0]))

table_name

for i in table_name:
    path = '/mnt/silver/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)
    column_names = df.columns
    for old_col_name in column_names:
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() 
                                else char for i, char in enumerate(old_col_name)]).lstrip("_")
        
        df = df.withColumnRename(old_col_name, new_col_name)

        output_path = '/mnt/gold/SalesLT' + name +'/'
        df.write.format('delta').mode('overwrite').save(output_path)

display(df)
