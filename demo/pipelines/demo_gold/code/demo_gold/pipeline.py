from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_gold.config.ConfigStore import *
from demo_gold.functions import *
from prophecy.utils import *
from demo_gold.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_customers = customers(spark)
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_reformatted_orders = reformatted_orders(spark, df_order_customer_details)
    df_reformatted_order_details = reformatted_order_details(spark, df_reformatted_orders)
    df_reformatted_order_summary = reformatted_order_summary(spark, df_reformatted_order_details)
    df_sales_summary_by_customer = sales_summary_by_customer(spark, df_reformatted_order_summary)
    df_sales_summary_sorted = sales_summary_sorted(spark, df_sales_summary_by_customer)
    df_limited_sort_results = limited_sort_results(spark, df_sales_summary_sorted)
    top_25(spark, df_limited_sort_results)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("demo_gold")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/demo_gold")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/demo_gold", config = Config)(pipeline)

if __name__ == "__main__":
    main()
