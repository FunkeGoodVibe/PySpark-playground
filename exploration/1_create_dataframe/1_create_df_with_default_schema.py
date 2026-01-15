
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()

data = [(1, "Adam", 29), (2, "Bob", 35)]

df = spark.createDataFrame(data, ["id", "name", "age"])

df.show()