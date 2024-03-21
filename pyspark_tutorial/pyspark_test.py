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

df_pyspark = spark.read.option('header', 'true').csv('test_pyspark.csv', inferSchema=True) 
print(df_pyspark.show())
print(df_pyspark)
print(type(df_pyspark))

#to print schema of dataframe
print(df_pyspark.printSchema)
print(df_pyspark.head(df_pyspark.count()-15))

########################################################################
# getting the column names 
print(df_pyspark.columns)

#to show particular column 
print(df_pyspark.select('Name').show())

#to select multiple columns 
df_pyspark.select(['Name','Experience']).show()

df_pyspark.describe().show()

#to get dtypes
print (df_pyspark.dtypes)

 
#Stop SparkSession
spark.stop()
