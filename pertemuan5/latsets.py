print("\033c")

# PART 1
# Constructing a Set
color_set_1 = {"Red", "Green", "Blue"}
color_set_2 = set(("Red", "Green", "Blue"))
print("Tipe data color_set_1 adalah ", type(color_set_1))
print("Tipe data color_set_2 adalah ", type(color_set_2))
print("Data color_set_1: ", color_set_1)
print("Data color_set_2: ", color_set_2)
print("--------------------------------------------")

# Print every item of color_set_1
print("Warna dalam color_set_1:")
for color in color_set_1:
    print(color)
print("---- ")

# Check the length of the set
print("Jumlah warna dalam color_set_1:", len(color_set_1))

# Check if a key exists
if "Green" in color_set_1:
    print("Yes, 'Green' is an item in color_set_1.")

# Add an item
color_set_1.add("Yellow")
print("Setelah menambahkan warna baru:", color_set_1)

# Add multiple items
color_set_1.update(["Orange", "Purple", "Pink"])
print("Setelah menambahkan beberapa warna:", color_set_1)

# PART 2
# Remove an item (method 1)
color_set_1.remove("Blue")
print("Setelah menghapus warna 'Blue':", color_set_1)

# Remove an item (method 2)
color_set_1.discard("Pink")
print("Setelah menghapus warna 'Pink':", color_set_1)

# Delete (pop) the last inserted key
color_set_1.pop()
print("Setelah menghapus elemen terakhir:", color_set_1)

# Clear the set
color_set_1.clear()
print("Setelah menghapus semua warna:", color_set_1)

# Delete the set
del color_set_1
print("-----")

# Union of two sets
set3 = {"Red", "Green", "Blue"}
set4 = {"Yellow", "Orange", "Purple"}
color_set_3 = set3.union(set4)
print("Gabungan color_set_3:", color_set_3)
print("--------------")

# color_set_5 takes copies of all items of color_set_6
color_set_5 = {"Red", "Green", "Blue"}
color_set_6 = {"Yellow", "Orange", "Purple"}
color_set_5.update(color_set_6)
print("Setelah mengupdate color_set_5:", color_set_5)
