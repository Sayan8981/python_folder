import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Practice').getOrCreate()
# Print Spark session details
print("Spark session details:")
print("Application Name:", spark.sparkContext.appName)
print("Master URL:", spark.sparkContext.master)
print("Spark UI URL:", spark.sparkContext.uiWebUrl)

df_pyspark = spark.read.csv('test_pyspark.csv') 
print(df_pyspark.show())
print(df_pyspark)

# # Read CSV file into a DataFrame
# df = spark.read.csv("data.csv", header=True, inferSchema=True)

df_pyspark = spark.read.option('header', 'true').csv('test_pyspark.csv') 
print(df_pyspark.show())
print(df_pyspark)
print(type(df_pyspark))

#to print schema of dataframe
print(df_pyspark.printSchema)
print(df_pyspark.head(df_pyspark.count()))



# Stop SparkSession
spark.stop()
