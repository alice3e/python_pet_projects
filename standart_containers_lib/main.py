from hash_table import HashTable

if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable()

    # Insert some key-value pairs
    hash_table.insert('key1', 'value1')
    hash_table.insert('key2', 'value2')
    hash_table.insert('key3', 'value3')

    # Retrieve values
    print(hash_table.get('key1'))  # Output: value1
    print(hash_table.get('key2'))  # Output: value2
    print(hash_table.get('key4'))  # Output: None

    # Update a value
    hash_table.insert('key1', 'new_value3')
    print(hash_table.get('key1'))  # Output: new_value3

    # Delete a key
    hash_table.delete('key2')
    print(hash_table.get('key2'))  # Output: None

    print('\niteration over key-value pairs:')
    # Iterate over key-value pairs
    for key, value in hash_table:
        print(f'{key}: {value}')
