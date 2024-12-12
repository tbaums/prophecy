from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_gold.config.ConfigStore import *
from demo_gold.functions import *

def reformatted_order_summary(spark: SparkSession, reformatted_order_details: DataFrame) -> DataFrame:
    return reformatted_order_details.select(
        col("full_name"), 
        col("ORDER_ID"), 
        round(col("CAST_order_amount_AS_DOUBLE_"), 2).alias("ROUNDED_ORDER_AMOUNT")
    )
