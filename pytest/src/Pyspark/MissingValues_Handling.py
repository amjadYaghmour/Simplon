from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg

spark = SparkSession.builder.appName("MissingValuesHandling").getOrCreate()
data = [
    (1, 34, "Cardiology"),
    (2, None, "Neurology"),
    (3, 50, "Orthopedics"),
    (4, None, None),
    (5, 15, "Neurology"),
]
columns = ["patient_id", "age", "department"]
df = spark.createDataFrame(data, columns)
mean_age = df.select(avg(col("age")).alias("mean_age")).collect()[0]["mean_age"]
df = df.na.fill({"age": mean_age, "department": "Unknown"})
df.show()
