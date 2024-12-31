from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *

def car(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("YEAR", StringType(), True), StructField("MAKE", StringType(), True), StructField("MODEL", StringType(), True), StructField("TRIM", StringType(), True), StructField("BODY", StringType(), True), StructField("TRANSMISSION", StringType(), True), StructField("VIN", StringType(), True), StructField("STATE", StringType(), True), StructField("CONDITION", StringType(), True), StructField("ODOMETER", StringType(), True), StructField("COLOR", StringType(), True), StructField("INTERIOR", StringType(), True), StructField("SELLER", StringType(), True), StructField("MMR", StringType(), True), StructField("SELLINGPRICE", DecimalType(10, 0), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/michael/onboard/sales-data/car-sales-no-ca/")
