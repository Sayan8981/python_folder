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

# # # Read CSV file into a DataFrame
# # df = spark.read.csv("data.csv", header=True, inferSchema=True)

# df_pyspark = spark.read.option('header', 'true').csv('test_pyspark.csv', inferSchema=True) 
# print(df_pyspark.show())
# print(df_pyspark)
# print(type(df_pyspark))

# #to print schema of dataframe
# print(df_pyspark.printSchema)
# print(df_pyspark.head(df_pyspark.count()-15))

# ########################################################################
# # getting the column names 
# print(df_pyspark.columns)

# #to show particular column 
# print(df_pyspark.select('Name').show())

# #to select multiple columns 
# df_pyspark.select(['Name','Experience']).show()

# df_pyspark.describe().show()

# #to get dtypes
# print (df_pyspark.dtypes)

# #adding columns 
# df_pyspark = df_pyspark.withColumn('Experience after 2 years', df_pyspark['Experience']+2)
# df_pyspark.show()

# #droping columns
# df_pyspark = df_pyspark.drop('Experience after 2 years')
# df_pyspark.show()

# #renaming the colums
# df_pyspark.withColumnRenamed('Name', 'new_name').show()
 
# #filtering data 
# # Create a DataFrame from a list of tuples
# data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
# df = spark.createDataFrame(data, ["Name", "Age"])

# # Filter rows where age is greater than 30
# filtered_df = df.filter(df.Age > 30)

# # Show the filtered DataFrame
# filtered_df.show()

# data_sec = [("Krish", 31, 10, 30000), ("Sunny", 30, 4, None), ("Paul", 24, 3, 20000), ("harsha", 21, 1, 15000), ("Dev", 20, None ,29000), ("Hak", None, 2, None), (None, None, None, 12000), (None, None, None, None), (None, None, None, None)]

# df_pyspark_sec = spark.createDataFrame(data_sec, ["Name","Age","Experience","Salary"])

# df_pyspark_sec = df_pyspark_sec.na.drop(how='any', thresh=2)
# df_pyspark_sec.show()

# #inverse operation with ~
# df_pyspark_sec.filter(~(df_pyspark_sec["Salary"]<=20000)).show()

# #filterout based on salary None value excluded and select particular column with & / |
# df_pyspark_sec = df_pyspark_sec.filter((df_pyspark_sec["Salary"]<=20000) &
#                                        (df_pyspark_sec["Age"]<30)).select(["Name", "Age"])
# df_pyspark_sec.show()

#import pdb;pdb.set_trace()
# Initialize SparkSession
# spark = SparkSession.builder \
#     .appName("Word Count") \
#     .getOrCreate()

# # Read text file into RDD
# lines = spark.sparkContext.textFile("input.txt")

# # Split each line into words
# words = lines.flatMap(lambda line: line.split(" "))

# # Map each word to a tuple (word, 1) for counting
# word_counts = words.map(lambda word: (word, 1))

# # Reduce by key to count occurrences of each word
# word_counts = word_counts.reduceByKey(lambda x, y: x + y)

# # Collect the result back to the driver
# result = word_counts.collect()

# # Print word counts
# for word, count in result:
#     print(f"{word}: {count}")

from pyspark.sql.functions import avg

# Create a DataFrame from a list of tuples
data = [("Alice", "Sales", 1000),
        ("Bob", "IT", 1500),
        ("Alice", "Marketing", 2000),
        ("Bob", "Sales", 1200)]
df = spark.createDataFrame(data, ["Name", "Department", "Salary"])

# Group by department and calculate average salary
avg_salary_df = df.groupBy("Department").agg(avg("Salary").alias("AvgSalary"))

# Show the average salary by department
avg_salary_df.show()

# Create two DataFrames
employees = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
departments = [(1, "Sales"), (2, "Marketing"), (3, "IT")]

employees_df = spark.createDataFrame(employees, ["Name", "DeptId"])
departments_df = spark.createDataFrame(departments, ["DeptId", "DeptName"])

# Join DataFrames on DeptId
joined_df = employees_df.join(departments_df, "DeptId")

# Show the joined DataFrame
joined_df.show()

#Stop SparkSession
spark.stop()

#######this is requires Hadoop installation in system
# from pyspark import SparkContext 

# sc = SparkContext("local", "TestApp")

# new_rdd = sc.parallelize([("Rose", 4), ("John",2), ("Yash", 1)])
# new_rdd.take(2)
