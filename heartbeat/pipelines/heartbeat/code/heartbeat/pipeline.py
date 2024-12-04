from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from heartbeat.config.ConfigStore import *
from heartbeat.functions import *
from prophecy.utils import *
from heartbeat.graph import *

def pipeline(spark: SparkSession) -> None:
    df_heartbeat_data = heartbeat_data(spark)
    df_Limit_1 = Limit_1(spark, df_heartbeat_data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("heartbeat")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/heartbeat")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/heartbeat", config = Config)(pipeline)

if __name__ == "__main__":
    main()
