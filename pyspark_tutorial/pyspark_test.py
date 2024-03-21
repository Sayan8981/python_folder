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

#adding columns 
df_pyspark = df_pyspark.withColumn('Experience after 2 years', df_pyspark['Experience']+2)
df_pyspark.show()

#droping columns
df_pyspark = df_pyspark.drop('Experience after 2 years')
df_pyspark.show()

#renaming the colums
df_pyspark.withColumnRenamed('Name', 'new_name').show()
 
#filtering data 
# Create a DataFrame from a list of tuples
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Filter rows where age is greater than 30
filtered_df = df.filter(df.Age > 30)

# Show the filtered DataFrame
filtered_df.show()

data_sec = [("Krish", 31, 10, 30000), ("Sunny", 30, 4, None), ("Paul", 24, 3, 20000), ("harsha", 21, 1, 15000), ("Dev", 20, None ,29000), ("Hak", None, 2, None), (None, None, None, 12000), (None, None, None, None), (None, None, None, None)]

df_pyspark_sec = spark.createDataFrame(data_sec, ["Name","Age", "Experience", "Salary"])

df_pyspark_sec = df_pyspark_sec.na.drop(how='any', thresh=2)
df_pyspark_sec.show()


 
#Stop SparkSession
spark.stop()
