from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from heartbeat.config.ConfigStore import *
from heartbeat.functions import *

def heartbeat_data(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("id", StringType(), True), StructField("price", StringType(), True), StructField("brand", StringType(), True), StructField("model", StringType(), True), StructField("year", StringType(), True), StructField("title_status", StringType(), True), StructField("mileage", StringType(), True), StructField("color", StringType(), True), StructField("vin", StringType(), True), StructField("lot", StringType(), True), StructField("state", StringType(), True), StructField("country", StringType(), True), StructField("condition", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/michael/heartbeat/heartbeat_data/cars_title.csv")
