from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from basics.config.ConfigStore import *
from basics.functions import *

def car_mfg_by_country(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("make", StringType(), True), StructField("country", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/michael/onboard/sales-data/car-mfg-by-country - list.csv")
