from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from basics.config.ConfigStore import *
from basics.functions import *

def input0(spark: SparkSession) -> DataFrame:
    return spark.read.table("`hive_metastore`.`nyc_taxi`.`nyc_taxi`")
