from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_gold.config.ConfigStore import *
from demo_gold.functions import *

def reformatted_orders(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("order_id"), 
        col("order_amount"), 
        concat(col("first_name"), lit(" "), col("last_name")).alias("full_name")
    )
