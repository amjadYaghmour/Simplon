import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg
import pandas as pd
import numpy as np


@pytest.fixture(scope="module")
def spark():
    """Fixture to provide a Spark session for testing."""
    spark_session = (
        SparkSession.builder.appName("PySparkTest").master("local[1]").getOrCreate()
    )
    yield spark_session
    spark_session.stop()


def perform_MissingValues_Handling(spark):
    # Initial data
    data = [
        (1, 34, "Cardiology"),
        (2, None, "Neurology"),
        (3, 50, "Orthopedics"),
        (4, None, None),
        (5, 15, "Neurology"),
    ]
    columns = ["patient_id", "age", "department"]

    # Pandas manipulation
    pandas_df = pd.DataFrame(data, columns=columns)
    mean_age = round(pandas_df["age"].mean(), 1)  # rounding to one decimal place
    pandas_df["age"].fillna(mean_age, inplace=True)
    pandas_df["department"].fillna("Unknown", inplace=True)

    # PySpark manipulation
    spark_df = spark.createDataFrame(data, columns)
    mean_age_spark = round(
        spark_df.select(avg(col("age")).alias("mean_age")).collect()[0]["mean_age"], 1
    )
    spark_df = spark_df.na.fill({"age": mean_age_spark, "department": "Unknown"})
    pyspark_df = spark_df.toPandas()

    return pandas_df, pyspark_df


def test_MissingValues_Handling(spark):
    pandas_df, pyspark_df = perform_MissingValues_Handling(spark)
    pd.testing.assert_frame_equal(pandas_df, pyspark_df, check_dtype=False)
