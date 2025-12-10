disk_size_mb = 1.44
pages = 100
lines = 50
chars = 25
bytes_for_char = 4
BYTES_IN_KB = 1024
BYTES_IN_MB = BYTES_IN_KB * 1024
total_chars = pages * lines * chars
book_size_bytes = total_chars * bytes_for_char
book_size_mb = book_size_bytes / BYTES_IN_MB
disk_size_bytes = disk_size_mb * BYTES_IN_MB
books_on_disk = int(disk_size_bytes // book_size_bytes)


print("Количество книг, помещающихся на дискету:", books_on_disk)
