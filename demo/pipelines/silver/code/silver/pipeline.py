from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from silver.config.ConfigStore import *
from silver.functions import *
from prophecy.utils import *
from silver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_orders = orders(spark)
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_full_name_projection = full_name_projection(spark, df_order_customer_details)
    df_full_name_order_amount = full_name_order_amount(spark, df_full_name_projection)
    df_order_summary_by_customer = order_summary_by_customer(spark, df_full_name_order_amount)
    df_customer_order_summary = customer_order_summary(spark, df_order_summary_by_customer)
    df_customer_order_summary_sorted = customer_order_summary_sorted(spark, df_customer_order_summary)
    df_limited_sort_results = limited_sort_results(spark, df_customer_order_summary_sorted)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/silver", config = Config)(pipeline)

if __name__ == "__main__":
    main()
