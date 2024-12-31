from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bronze.config.ConfigStore import *
from bronze.functions import *

def customers(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("customer_id", StringType(), True), StructField("first_name", StringType(), True), StructField("last_name", StringType(), True), StructField("email", StringType(), True), StructField("phone_number", StringType(), True), StructField("address", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/michael/demo/sales-data/customers_cleaned.csv")
