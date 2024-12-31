from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def sales_summary(spark: SparkSession, sales_summary_by_customer: DataFrame) -> DataFrame:
    return sales_summary_by_customer.select(
        col("full_name"), 
        col("ORDER_COUNT"), 
        format_number(col("SALES_TOTAL"), 2).alias("SALES_TOTAL_FORMATTED")
    )
