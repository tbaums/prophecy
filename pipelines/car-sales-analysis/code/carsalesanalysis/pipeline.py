from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("car-sales-analysis")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/car-sales-analysis")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/car-sales-analysis", config = Config)(pipeline)

if __name__ == "__main__":
    main()
