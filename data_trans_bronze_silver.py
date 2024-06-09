# Initial Data Transformation from bronze to silver layers
# Transformation of date column from date time to date format in all the tables

dbutils.fs.ls('mnt/bronze/SalesLT')

dbutils.fs.ls('mnt/silver/')

table_name = []

for i in dbutils.fs.ls('/mnt/bronze/SalesLT'):
    table_name.append(i.name.split('/'[0]))

table_name

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimeStampType

for i in table_name:
    path = '/mnt/bronze/SalesLT/' + i + '/'+ '.parquet'

    df = spark.read.format('parquet').load(path)
    column = df.columns
    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col,date_format(from_utc_timestamp(df[col].cast(TimeStampType()), "UTC"), "YYYY-MM-dd"))
            output_path = "/mnt/silver/SalesLT/" + i + "/"
            df.write.format('delta').mode('overwrite').save(output_path)

display(df)
