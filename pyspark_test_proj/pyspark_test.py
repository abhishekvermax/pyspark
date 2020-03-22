import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
import numpy as np

sc = SparkContext("local[*]", "test_app")

spark = SparkSession.builder.appName('test_app').getOrCreate()

df_1 = spark.read.csv('/Users/abhi/Documents/git/pyspark/pyspark_test_proj/data/data_1.csv', header=True)
df_2 = spark.read.csv('/Users/abhi/Documents/git/pyspark/pyspark_test_proj/data/data_2.csv', header=True)

from pyspark.sql.functions import udf, col
from pyspark.sql.types import BooleanType

from pyspark.sql import Row

document_row = Row("document_id", "document_text")
keyword_row = Row("keyword")

documents_df = sc.parallelize([
    document_row(1, "contour global,Guadaloupe"),
    document_row(2, "blackfiled limited"),
    document_row(3, "google limited")
]).toDF()

keywords_df = sc.parallelize([
    keyword_row("contour global,Capuava"),
    keyword_row("blacfield"),
    keyword_row("gg")
]).toDF()


def string_match_percentage(col_1, col_2):
    s = col_1.lower()
    t = col_2.lower()

    global row, col
    rows = len(s) + 1
    cols = len(t) + 1
    array_diffrence = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for k in range(1, cols):
            array_diffrence[i][0] = i
            array_diffrence[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 2
            array_diffrence[row][col] = min(array_diffrence[row - 1][col] + 1,
                                            array_diffrence[row][col - 1] + 1,
                                            array_diffrence[row - 1][col - 1] + cost)
    match_percentage = ((len(s) + len(t)) - array_diffrence[row][col]) / (len(s) + len(t)) * 100
    print(match_percentage)
    if match_percentage > 58:
        return True
    else:
        return False


contains = udf(lambda s, q: string_match_percentage(s, q), BooleanType())

like_with_python_udf = (documents_df.crossJoin(keywords_df)
                        .where(contains(col("document_text"), col("keyword")))
                        .select(col("document_id"), col("keyword"), col("document_text")))
like_with_python_udf.show()
