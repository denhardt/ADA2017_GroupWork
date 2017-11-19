from pyspark import *

textFile = spark.read.text("/home/mbanga/README.txt")
textFile.count()
