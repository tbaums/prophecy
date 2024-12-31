from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_gold.config.ConfigStore import *
from demo_gold.functions import *

def sales_summary_sorted(spark: SparkSession, sales_summary_by_customer: DataFrame) -> DataFrame:
    return sales_summary_by_customer.orderBy(col("SALES_TOTAL").desc())
