from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_gold.config.ConfigStore import *
from demo_gold.functions import *

def limited_sort_results(spark: SparkSession, sales_summary_sorted: DataFrame) -> DataFrame:
    return sales_summary_sorted.limit(25)
