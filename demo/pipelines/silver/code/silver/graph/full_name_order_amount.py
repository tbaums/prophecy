from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def full_name_order_amount(spark: SparkSession, full_name_projection: DataFrame) -> DataFrame:
    return full_name_projection.select(
        col("full_name"), 
        col("order_id").alias("ORDER_ID"), 
        col("order_amount").cast(DoubleType()).alias("CAST_order_amount_AS_DOUBLE_")
    )
