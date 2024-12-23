from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def limited_sort_results(spark: SparkSession, reformatted_sales_ordered: DataFrame) -> DataFrame:
    return reformatted_sales_ordered.limit(25)
