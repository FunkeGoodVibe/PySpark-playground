
#How do you read large files effeciently in pyspark? 


import spark 

df = spark.read \
          .option("header", "true") \
          .option("inferSchema", "false") \
          .csv("s3://data/input") 


"""
Best practices 

- Avoid 'inferschema' for large datasets 
- Define schema explicitly 
- Prefer *parquet* over CSV for performance 

ref- (techtitans)
"""

from pyspark.sql.types import * 

schema = StructType([ 
                StructField("id", IntegerType(), True), 
                StructField("name", StringType(), True)
])