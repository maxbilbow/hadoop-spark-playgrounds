import pyspark as ps

sc = ps.SparkContext()

rdd = sc.parallelize([1, 2, 3, 3])

