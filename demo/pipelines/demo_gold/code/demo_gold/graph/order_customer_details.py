from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_gold.config.ConfigStore import *
from demo_gold.functions import *

def order_customer_details(spark: SparkSession, orders: DataFrame, customers: DataFrame, ) -> DataFrame:
    return orders\
        .alias("orders")\
        .join(customers.alias("customers"), (col("orders.customer_id") == col("customers.customer_id")), "inner")\
        .select(col("orders.order_id").alias("order_id"), col("orders.order_date").alias("order_date"), col("orders.order_amount").alias("order_amount"), col("orders.order_status").alias("order_status"), col("customers.customer_id").alias("customer_id"), col("customers.first_name").alias("first_name"), col("customers.last_name").alias("last_name"), col("customers.email").alias("email"), col("customers.phone_number").alias("phone_number"), col("customers.address").alias("address"))
