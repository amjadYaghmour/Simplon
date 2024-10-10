from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("FilteringPatientRecords").getOrCreate()
data = [
    (1, 34, "Cardiology"),
    (2, 45, "Neurology"),
    (3, 50, "Orthopedics"),
    (4, 20, "Cardiology"),
    (5, 15, "Neurology"),
]
columns = ["patient_id", "age", "department"]
df = spark.createDataFrame(data, columns)
filtered_df = df.filter(col("age") > 30)
filtered_df.show()
