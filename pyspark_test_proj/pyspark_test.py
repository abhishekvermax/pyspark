import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local[*]", "test_app")

spark = SparkSession.builder.appName('test_app').getOrCreate()

df=spark.read.csv('/Users/abhi/Documents/python_functional_advance_programming/pyspark_test_proj/data/test.csv',header=True)
df.show(truncate=False)

