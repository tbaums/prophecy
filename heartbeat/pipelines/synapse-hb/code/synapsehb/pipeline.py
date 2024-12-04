from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from synapsehb.config.ConfigStore import *
from synapsehb.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("synapse-hb")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/synapse-hb")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/synapse-hb", config = Config)(pipeline)

if __name__ == "__main__":
    main()
