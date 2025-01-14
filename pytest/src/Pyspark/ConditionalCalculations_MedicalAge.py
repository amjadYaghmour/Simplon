from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("AgeCategorization").getOrCreate()
data = [
    (1, 34, "Cardiology"),
    (2, 70, "Neurology"),
    (3, 50, "Orthopedics"),
    (4, 20, "Cardiology"),
    (5, 15, "Neurology"),
]

columns = ["patient_id", "age", "department"]

df = spark.createDataFrame(data, columns)

df = df.withColumn(
    "age_category",
    when(col("age") > 60, "senior").when(col("age") > 18, "adult").otherwise("minor"),
)

df.show()
