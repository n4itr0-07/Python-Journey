# File Handling in Python

**File:** A collection of data stored on disk.

---

## Importance of File Handling
File handling is crucial because it enables:
- Persistent storage and retrieval of data.
- Sharing data between programs and systems.
- Handling large datasets that exceed memory limitations.
- Working with data in structured formats (e.g., CSV, JSON, XML).
- Organizing and processing data efficiently.

---

## File Types
1. **Text File**: Human-readable; editable with any text editor.
2. **Binary File**: Not human-readable; requires specific tools (e.g., images, videos).
3. **CSV File**: Comma-separated values; editable with Excel or Google Sheets.
4. **JSON File**: JavaScript Object Notation; used for structured data.
5. **XML File**: Extensible Markup Language format.
6. **HTML File**: Hypertext Markup Language; works with web browsers.
7. **PDF File**: Portable Document Format; requires PDF viewers.
8. **Compressed Files (e.g., Zip, RAR)**: Store data compactly.
9. **Disk Images (ISO, DMG)**: Store disk data.

---

## File Handling Methods in Python

### Syntax
```python
file = open(file_name, mode)
file.close()
```

### Common Modes
- `'r'`: Read mode (default).
- `'w'`: Write mode (overwrites content).
- `'a'`: Append mode (adds data at end).
- `'r+'`: Read and write mode.
- `'rb'`: Read binary mode.
- `'wb'`: Write binary mode.

---

## Examples

### 1. **Reading a File**
```python
# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### 2. **Writing to a File**
```python
# Writing text to a file
with open("example.txt", "w") as file:
    file.write("Hello, File Handling!")
```

### 3. **Appending to a File**
```python
# Appending text to a file
with open("example.txt", "a") as file:
    file.write("\nAppending new data.")
```

### 4. **Binary File Operations**
```python
# Writing binary data
with open("example.bin", "wb") as file:
    file.write(b"Binary content")

# Reading binary data
with open("example.bin", "rb") as file:
    data = file.read()
    print(data)
```

### 5. **Using `seek()` and `tell()`**
```python
with open("example.txt", "r") as file:
    # Move file pointer to the 5th byte
    file.seek(5)
    print(file.read(10))  # Read 10 bytes from position 5

    # Get the current position
    position = file.tell()
    print(f"Current pointer position: {position}")
```

### 6. **Working with CSV Files**
```python
import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])

# Reading from a CSV file
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

### 7. **Working with JSON Files**
```python
import json

# Writing JSON data
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON data
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

---
