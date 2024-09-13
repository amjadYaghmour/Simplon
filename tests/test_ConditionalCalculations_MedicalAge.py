import pytest
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import col, lower, concat_ws, when
import pandas as pd


@pytest.fixture(scope="module")
def spark():
    """Fixture to provide a Spark session for testing."""
    spark_session = (
        SparkSession.builder.appName("PySparkTest").master("local[1]").getOrCreate()
    )
    yield spark_session
    spark_session.stop()


def perform_ConditionalCalculations_MedicalAge(spark):
    # Initial data
    data = [
        (1, 34, "Cardiology"),
        (2, 70, "Neurology"),
        (3, 50, "Orthopedics"),
        (4, 20, "Cardiology"),
        (5, 15, "Neurology"),
    ]
    columns = ["patient_id", "age", "department"]

    # Pandas manipulation
    pandas_df = pd.DataFrame(data, columns=columns)
    pandas_df["age_category"] = pandas_df["age"].apply(
        lambda x: "senior" if x > 60 else "adult" if x > 18 else "minor"
    )

    # PySpark DataFrame creation directly from data
    spark_df = spark.createDataFrame(data, schema=columns)
    spark_df = spark_df.withColumn(
        "age_category",
        when(col("age") > 60, "senior")
        .when(col("age") > 18, "adult")
        .otherwise("minor"),
    )
    pyspark_df = spark_df.toPandas()

    return pandas_df, pyspark_df


def test_ConditionalCalculations_MedicalAge(spark):
    pandas_df, pyspark_df = perform_ConditionalCalculations_MedicalAge(spark)
    assert pandas_df.equals(pyspark_df)
