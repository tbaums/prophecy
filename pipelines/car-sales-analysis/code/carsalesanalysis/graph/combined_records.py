from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from carsalesanalysis.config.ConfigStore import *
from carsalesanalysis.functions import *

def combined_records(
        spark: SparkSession,
        car_sales_data_excluding_california: DataFrame, 
        car_sales_data_with_country: DataFrame
) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    car_sales_data_excluding_california.createOrReplaceTempView("car_sales_data_excluding_california")
    car_sales_data_with_country.createOrReplaceTempView("car_sales_data_with_country")
    df1 = spark.sql(
        "SELECT *\nFROM car_sales_data_excluding_california\nUNION\nSELECT *\nFROM car_sales_data_with_country"
    )

    return df1
