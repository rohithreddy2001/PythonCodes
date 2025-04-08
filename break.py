key_location = 3
locations = [1,4,2,3,6,8]
for key in locations:
    if key == key_location:
        print("Key found at:",key)
        break
    else:
        print("Key not found at:", key)
