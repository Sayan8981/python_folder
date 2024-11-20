
# PyTables is a Python library for managing hierarchical datasets and designed to efficiently and easily manipulate large amounts of data. It's built on top of the HDF5 library and allows you to store and query massive datasets using tables and arrays.

# Here's a detailed explanation with code examples:

# Key Concepts of PyTables
# HDF5 Format: PyTables uses the HDF5 file format, which is highly efficient for storing large datasets.
# Nodes: The structure of a PyTables file includes nodes such as:
# Groups: Containers for other nodes, similar to directories in a filesystem.
# Tables: Data structures for storing structured data (rows and columns).
# Arrays: Multidimensional datasets, similar to NumPy arrays.
# Queries: PyTables supports querying tables efficiently using conditions.


import tables

# Define a data structure
class Particle(tables.IsDescription):
    name = tables.StringCol(16)  # 16-character string
    id = tables.Int32Col()       # 32-bit integer
    temperature = tables.Float32Col()  # 32-bit float
    
filename = "example.h5"
h5file = tables.open_file(filename, mode="w", title="test data file")

group = h5file.create_group("/", 'experiment', 'Experimant Data Group')

table = h5file.create_table(group, 'reading', Particle, "Reading Table")

particle = table.row
for i in range(10):
    particle['name'] = f"particle{i}"
    particle['id'] = i
    particle['temperature'] = 20.5 + i
    particle.append()
    
table.flush()
table.close()  

# Print the structure of the file
print(h5file)

# List all nodes under the root group
for node in h5file.root:
    print(node)

# Access the table
table = h5file.root.experiment.reading

for row in table:
    print (f"name: {row['name']}, id: {row['id']}, temperature: {row['temperature']}\n")
    
table = h5file.root.experiment.reading

# Query rows where temperature > 25
for row in table.where('temperature > 25'):
    print(f"Temp > 25: \n Name: {row['name']}, Temp: {row['temperature']}\n")
        
h5file.close()    