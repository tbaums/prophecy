from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from heartbeat.config.ConfigStore import *
from heartbeat.functions import *

def Limit_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(10)
