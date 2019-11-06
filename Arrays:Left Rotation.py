def reftRotation(list_size, rotation):
    for i in range(1, list_size+1):
        x = i+rotation
        if x > list_size:
            x -= list_size
        print(x)


reftRotation(5, 4)
