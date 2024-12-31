from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *

def car_sales_data_with_country(spark: SparkSession, car_2: DataFrame, car_1: DataFrame, ) -> DataFrame:
    return car_2\
        .alias("car_2")\
        .join(car_1.alias("car_1"), (col("car_2.MAKE") == col("car_1.make")), "inner")\
        .select(col("car_2.YEAR").alias("`YEAR`"), col("car_2.MAKE").alias("MAKE"), col("car_2.MODEL").alias("MODEL"), col("car_2.TRIM").alias("TRIM"), col("car_2.BODY").alias("BODY"), col("car_2.TRANSMISSION").alias("TRANSMISSION"), col("car_2.VIN").alias("VIN"), col("car_2.STATE").alias("STATE"), col("car_2.CONDITION").alias("CONDITION"), col("car_2.ODOMETER").alias("ODOMETER"), col("car_2.COLOR").alias("COLOR"), col("car_2.INTERIOR").alias("INTERIOR"), col("car_2.SELLER").alias("SELLER"), col("car_2.MMR").alias("MMR"), col("car_2.SELLINGPRICE").alias("SELLINGPRICE"), col("car_1.country").alias("COUNTRY"))
