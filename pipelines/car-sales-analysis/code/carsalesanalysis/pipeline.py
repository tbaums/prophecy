from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *
from prophecy.utils import *
from carsalesanalysis.graph import *

def pipeline(spark: SparkSession) -> None:
    df_car = car(spark)
    df_car_1 = car_1(spark)
    df_car_sales_data_excluding_california = car_sales_data_excluding_california(spark, df_car, df_car_1)
    df_car_2 = car_2(spark)
    df_car_sales_data_with_country = car_sales_data_with_country(spark, df_car_2, df_car_1)
    df_combined_records = combined_records(
        spark, 
        df_car_sales_data_excluding_california, 
        df_car_sales_data_with_country
    )

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
