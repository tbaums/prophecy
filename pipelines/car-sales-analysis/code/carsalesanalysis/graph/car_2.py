from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *

def car_2(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("/Volumes/michael/onboard/sales-data/car-sales-ca/")
