from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *

def car_sales_data_excluding_california(spark: SparkSession, car: DataFrame, car_1: DataFrame, ) -> DataFrame:
    return car\
        .alias("car")\
        .join(car_1.alias("car_1"), (col("car.MAKE") == col("car_1.make")), "inner")\
        .select(col("car.YEAR").alias("`YEAR`"), col("car.MAKE").alias("MAKE"), col("car.MODEL").alias("MODEL"), col("car.TRIM").alias("TRIM"), col("car.BODY").alias("BODY"), col("car.TRANSMISSION").alias("TRANSMISSION"), col("car.VIN").alias("VIN"), col("car.STATE").alias("STATE"), col("car.CONDITION").alias("CONDITION"), col("car.ODOMETER").alias("ODOMETER"), col("car.COLOR").alias("COLOR"), col("car.INTERIOR").alias("INTERIOR"), col("car.SELLER").alias("SELLER"), col("car.MMR").alias("MMR"), col("car.SELLINGPRICE").alias("SELLINGPRICE"), col("car_1.country").alias("COUNTRY"))
