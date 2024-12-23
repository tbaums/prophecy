from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def reformatted_sales_ordered(spark: SparkSession, sales_summary_details: DataFrame) -> DataFrame:
    return sales_summary_details.orderBy(col("CAST_SALES_TOTAL_FORMATTED_AS_DOUBLE_").desc())
