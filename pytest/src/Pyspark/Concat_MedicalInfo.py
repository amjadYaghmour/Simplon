from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, concat_ws

spark = SparkSession.builder.appName("StringManipulation").getOrCreate()

data = [
    ("John Doe", "Diabetes"),
    ("Jane Smith", "Heart Disease"),
    ("Alice Brown", "Hypertension"),
]

columns = ["patient_name", "diagnosis"]

df = spark.createDataFrame(data, columns)

df = df.withColumn("diagnosis_lower", lower(col("diagnosis")))
df = df.withColumn(
    "full_info", concat_ws(" - ", col("patient_name"), col("diagnosis_lower"))
)

df.show()
