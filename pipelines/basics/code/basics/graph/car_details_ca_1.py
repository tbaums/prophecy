from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from basics.config.ConfigStore import *
from basics.functions import *

def car_details_ca_1(spark: SparkSession, filter_by_state_ca: DataFrame) -> DataFrame:
    return filter_by_state_ca.select(
        col("year").alias("`YEAR`"), 
        upper(col("make")).alias("MAKE"), 
        col("model").alias("MODEL"), 
        col("trim").alias("TRIM"), 
        col("body").alias("BODY"), 
        col("transmission").alias("TRANSMISSION"), 
        col("vin").alias("VIN"), 
        col("state").alias("STATE"), 
        col("condition").alias("CONDITION"), 
        col("odometer").alias("ODOMETER"), 
        col("color").alias("COLOR"), 
        col("interior").alias("INTERIOR"), 
        col("seller").alias("SELLER"), 
        col("mmr").alias("MMR"), 
        col("sellingprice").alias("SELLINGPRICE"), 
        col("saledate").alias("SALEDATE")
    )
