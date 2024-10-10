import pytest
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import col, lower, concat_ws


@pytest.fixture(scope="module")
def spark():
    """Fixture to provide a Spark session for testing."""
    spark_session = (
        SparkSession.builder.appName("PySparkTest").master("local[1]").getOrCreate()
    )
    yield spark_session
    spark_session.stop()


def perform_string_manipulations(spark):
    # Define test data as a list of tuples
    data = [
        ("John Doe", "Diabetes"),
        ("Jane Smith", "Heart Disease"),
        ("Alice Brown", "Hypertension"),
    ]
    columns = ["patient_name", "diagnosis"]

    # Creating Pandas DataFrame for comparison
    pandas_df = pd.DataFrame(data, columns=columns)
    pandas_df["diagnosis_lower"] = pandas_df["diagnosis"].str.lower()
    pandas_df["full_info"] = (
        pandas_df["patient_name"] + " - " + pandas_df["diagnosis_lower"]
    )

    # PySpark DataFrame creation directly from data
    spark_df = spark.createDataFrame(data, schema=columns)
    spark_df = spark_df.withColumn("diagnosis_lower", lower(col("diagnosis")))
    spark_df = spark_df.withColumn(
        "full_info", concat_ws(" - ", col("patient_name"), col("diagnosis_lower"))
    )
    pyspark_df = spark_df.toPandas()

    return pandas_df, pyspark_df


def test_string_manipulation(spark):
    pandas_df, pyspark_df = perform_string_manipulations(spark)
    assert pandas_df.equals(pyspark_df)
