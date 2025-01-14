from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def customer_order_summary(spark: SparkSession, order_summary_by_customer: DataFrame) -> DataFrame:
    return order_summary_by_customer.select(
        col("full_name"), 
        col("ORDER_COUNT"), 
        round(col("TOTAL_ORDER_AMOUNT"), 2).alias("TOTAL_ORDER_AMOUNT")
    )
