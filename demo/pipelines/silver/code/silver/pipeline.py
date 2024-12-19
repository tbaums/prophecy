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
    df_reformatted_orders = reformatted_orders(spark, df_order_customer_details)
    df_reformatted_order_details = reformatted_order_details(spark, df_reformatted_orders)
    df_sales_summary_by_customer = sales_summary_by_customer(spark, df_reformatted_order_details)
    df_sales_summary = sales_summary(spark, df_sales_summary_by_customer)
    df_sales_summary_details = sales_summary_details(spark, df_sales_summary)
    df_sorted_reformatted_sales = sorted_reformatted_sales(spark, df_sales_summary_details)
    df_limited_sort_results = limited_sort_results(spark, df_sorted_reformatted_sales)

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
