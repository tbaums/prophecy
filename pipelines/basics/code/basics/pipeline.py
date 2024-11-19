from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from basics.config.ConfigStore import *
from basics.functions import *
from prophecy.utils import *
from basics.graph import *

def pipeline(spark: SparkSession) -> None:
    df_car_sales = car_sales(spark)
    df_filter_by_state_ca = filter_by_state_ca(spark, df_car_sales)
    df_car_sales_1 = car_sales_1(spark)
    df_filter_by_state_ca_1 = filter_by_state_ca_1(spark, df_car_sales_1)
    car_sales_us_no_ca(spark, df_filter_by_state_ca_1)
    df_car_sales_us_no_ca_1 = car_sales_us_no_ca_1(spark)
    car_sales_ca(spark, df_filter_by_state_ca)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/basics")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/basics", config = Config)(pipeline)

if __name__ == "__main__":
    main()
