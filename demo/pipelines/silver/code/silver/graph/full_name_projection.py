from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from silver.config.ConfigStore import *
from silver.functions import *

def full_name_projection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(col("first_name"), lit(" "), col("last_name")).alias("full_name"), 
        col("order_id"), 
        col("order_amount")
    )
