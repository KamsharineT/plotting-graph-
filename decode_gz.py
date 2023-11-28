import gzip

# Open the gzip file in binary mode
with gzip.open('WQPA-MNSR-21_WQPA_pressure_2023-11-22_09 34 35.788499.gz', 'rb') as f:
    # Read the contents of the file
    file_contents = f.read()

# Decode the contents from bytes to string
decoded_contents = file_contents.decode('utf-8')

# Print the contents of the file
# print(decoded_contents)

with open("DECODED.txt", 'w', encoding='utf-8') as output:
    output.write(decoded_contents)
