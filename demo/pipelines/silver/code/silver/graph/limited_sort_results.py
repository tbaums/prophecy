from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def limited_sort_results(spark: SparkSession, customer_order_summary_sorted: DataFrame) -> DataFrame:
    return customer_order_summary_sorted.limit(25)
