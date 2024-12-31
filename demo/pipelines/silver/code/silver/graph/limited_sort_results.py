from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def limited_sort_results(spark: SparkSession, sorted_reformatted_sales: DataFrame) -> DataFrame:
    return sorted_reformatted_sales.limit(25)
