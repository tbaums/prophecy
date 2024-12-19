from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def sales_summary_details(spark: SparkSession, sales_summary: DataFrame) -> DataFrame:
    return sales_summary.select(
        col("full_name"), 
        col("ORDER_COUNT"), 
        col("SALES_TOTAL_FORMATTED"), 
        col("SALES_TOTAL_FORMATTED").cast(DoubleType()).alias("CAST_SALES_TOTAL_FORMATTED_AS_DOUBLE_")
    )
