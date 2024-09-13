from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, mean, max

spark = SparkSession.builder.appName("AggregationExample").getOrCreate()
data = [
    (1, 34, "Cardiology", 10),
    (2, 45, "Neurology", 12),
    (3, 23, "Cardiology", 5),
    (4, 64, "Orthopedics", 8),
    (5, 52, "Cardiology", 9),
]
columns = ["patient_id", "age", "department", "visit_count"]
df = spark.createDataFrame(data, columns)

agg_df = df.groupBy("department").agg(
    sum("visit_count").alias("total_visits"),
    mean("age").alias("average_age"),
    max("age").alias("max_age"),
)

# Show the results
agg_df.show()
