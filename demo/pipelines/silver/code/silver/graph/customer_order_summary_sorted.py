from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def customer_order_summary_sorted(spark: SparkSession, customer_order_summary: DataFrame) -> DataFrame:
    return customer_order_summary.orderBy(col("TOTAL_ORDER_AMOUNT").desc())
