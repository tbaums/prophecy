from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from basics.config.ConfigStore import *
from basics.functions import *

def filter_by_state_ca(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("state") == lit("ca")))
