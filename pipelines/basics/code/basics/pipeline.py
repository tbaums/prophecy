from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from basics.config.ConfigStore import *
from basics.functions import *
from prophecy.utils import *
from basics.graph import *

def pipeline(spark: SparkSession) -> None:
    df_input0 = input0(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("basics")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/basics")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/basics", config = Config)(pipeline)

if __name__ == "__main__":
    main()
