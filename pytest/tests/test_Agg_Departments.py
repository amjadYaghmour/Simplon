import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_, avg
import pandas as pd


@pytest.fixture(scope="module")
def spark():
    spark_session = (
        SparkSession.builder.appName("PySparkTest").master("local[1]").getOrCreate()
    )
    yield spark_session
    spark_session.stop()


def test_aggregate_functions(spark):
    data = [
        (1, 34, "Cardiology", 10),
        (2, 45, "Neurology", 20),
        (3, 50, "Orthopedics", 15),
        (4, 20, "Cardiology", 5),
        (5, 15, "Neurology", 25),
    ]
    columns = ["patient_id", "age", "department", "visit_count"]

    # Create Spark DataFrame directly
    spark_df = spark.createDataFrame(data, schema=columns)

    # Create Pandas DataFrame from the same data for validation
    pandas_df = pd.DataFrame(data, columns=columns)

    # Pandas aggregation
    pandas_agg = (
        pandas_df.groupby("department")
        .agg({"visit_count": "sum", "age": "mean"})
        .reset_index()
    )

    # PySpark aggregation
    spark_agg = (
        spark_df.groupBy("department")
        .agg(sum_("visit_count").alias("visit_count"), avg("age").alias("age"))
        .toPandas()
    )

    # Renaming columns for consistency in comparison
    spark_agg.columns = pandas_agg.columns

    # Sorting and resetting index for accurate comparison
    pandas_agg.sort_values("department", inplace=True)
    spark_agg.sort_values("department", inplace=True)
    pandas_agg.reset_index(drop=True, inplace=True)
    spark_agg.reset_index(drop=True, inplace=True)

    assert pandas_agg.equals(spark_agg)
