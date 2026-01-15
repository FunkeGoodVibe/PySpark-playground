

from pyspark.sql.types import StructType, StructField, IntegerType,
StringType
schema = StructType([
StructField("id"
StructField("name"
StructField("age"
, IntegerType(), True),
, StringType(), True),
, IntegerType(), True)
])
df = spark.createDataFrame(data, schema)
df.printSchema()
df.show()
# Schema as a string
data = [(1,
"Alice"
, 29), (2,
"Bob"
, 35)]
schema =
"id INT, name STRING, age INT"
df = spark.createDataFrame(data, schema=schema)
# Schema String with Float and Boolean Types
schema =
"id INT, name STRING, salary FLOAT, is
active BOOLEAN"
_
data = [(1,
"Alice"
, 50000.75, True), (2,
"Bob"
, 60000.50, False)]
df = spark.createDataFrame(data, schema=schema)
# Schema String with Date and Timestamp
from datetime import date, datetime
schema = "id INT, name STRING, join
_
date DATE, last
_
login TIMESTAMP"
data = [(1,
(2,
"Alice"
"Bob"
, date(2023, 1, 15), datetime(2024, 3, 10, 14, 30, 0)),
, date(2023, 1, 15), datetime(2024, 3, 10, 14, 30, 0))]
df = spark.createDataFrame(data, schema=schema)