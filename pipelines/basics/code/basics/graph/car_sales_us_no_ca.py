from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from basics.config.ConfigStore import *
from basics.functions import *

def car_sales_us_no_ca(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").mode("overwrite").save("/Volumes/michael/onboard/sales-data/car-sales-no-ca")
