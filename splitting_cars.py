def write_file():
    buffer = []
    with open("cars_exercise.txt", "r") as file:
        for line in file:
            buffer.append(line.strip())
    print(buffer)
    cars = []
    i = 0
    while i < len(buffer):
        make = buffer[i]
        model = buffer[i + 1]
        year = buffer[i + 2]
        cars.append({
            "make": make,
            "model": model,
            "year": year
        })
        i += 3
    print(cars)

    j = 0
    while j < len(cars):
        with open(cars[j]["make"]+"_"+cars[j]["model"]+"_"+cars[j]["year"]+".txt", mode="w") as my_file:
          my_file.write(str(cars[j]["make"]+"\n"+cars[j]["model"]+"\n"+cars[j]["year"]))
          j += 1

write_file()
