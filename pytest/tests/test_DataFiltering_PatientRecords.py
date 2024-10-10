import pytest
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import col


@pytest.fixture(scope="module")
def spark():
    """Fixture to provide a Spark session for testing."""
    spark_session = (
        SparkSession.builder.appName("PySparkTest").master("local[1]").getOrCreate()
    )
    yield spark_session
    spark_session.stop()


def perform_DataFiltering_PatientRecords(spark):
    # Initial data
    data = [
        (1, 34, "Cardiology"),
        (2, 45, "Neurology"),
        (3, 50, "Orthopedics"),
        (4, 20, "Cardiology"),
        (5, 15, "Neurology"),
    ]
    columns = ["patient_id", "age", "department"]

    # Pandas manipulation
    pandas_df = pd.DataFrame(data, columns=columns)
    pandas_filtered = pandas_df[pandas_df["age"] > 30]

    # PySpark manipulation
    spark_df = spark.createDataFrame(data, columns)
    spark_filtered = spark_df.filter(col("age") > 30)
    pyspark_filtered_df = spark_filtered.toPandas()

    return pandas_filtered, pyspark_filtered_df


def test_DataFiltering_PatientRecords(spark):
    pandas_filtered, pyspark_filtered_df = perform_DataFiltering_PatientRecords(spark)
    assert pandas_filtered.reset_index(drop=True).equals(
        pyspark_filtered_df.reset_index(drop=True)
    )
