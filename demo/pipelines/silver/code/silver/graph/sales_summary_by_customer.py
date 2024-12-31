from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def sales_summary_by_customer(spark: SparkSession, reformatted_order_details: DataFrame) -> DataFrame:
    df1 = reformatted_order_details.groupBy(col("full_name"))

    return df1.agg(
        count(col("order_id")).alias("ORDER_COUNT"), 
        sum(col("CAST_order_amount_AS_DOUBLE_")).alias("SALES_TOTAL")
    )
