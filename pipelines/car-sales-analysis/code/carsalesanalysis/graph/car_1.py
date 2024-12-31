from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *

def car_1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("make", StringType(), True), StructField("country", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/michael/onboard/sales-data/car-mfg-by-country - list.csv")
