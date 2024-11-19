from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from basics.config.ConfigStore import *
from basics.functions import *

def car_sales(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("year", StringType(), True), StructField("make", StringType(), True), StructField("model", StringType(), True), StructField("trim", StringType(), True), StructField("body", StringType(), True), StructField("transmission", StringType(), True), StructField("vin", StringType(), True), StructField("state", StringType(), True), StructField("condition", StringType(), True), StructField("odometer", StringType(), True), StructField("color", StringType(), True), StructField("interior", StringType(), True), StructField("seller", StringType(), True), StructField("mmr", StringType(), True), StructField("sellingprice", StringType(), True), StructField("saledate", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/michael/onboard/sales-data/car_prices.csv")
