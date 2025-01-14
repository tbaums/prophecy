from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def order_summary_by_customer(spark: SparkSession, full_name_order_amount: DataFrame) -> DataFrame:
    df1 = full_name_order_amount.groupBy(col("full_name"))

    return df1.agg(
        count(col("order_id")).alias("ORDER_COUNT"), 
        sum(col("CAST_order_amount_AS_DOUBLE_")).alias("TOTAL_ORDER_AMOUNT")
    )
