class orange_apple():
    ##data about apples and oranges
    #line up object name with index of properties
    _object = ["orange", "apple", "orange", "apple", "orange", "orange", "apple", "apple"]
    #properties for orange, then apple (learning data)
    _properties = [[155, "bumpy"], [120, "smooth"], [160, "bumpy"], [130, "smooth"], [165, "bumpy"], [138, "bumpy"], [128, "smooth"], [138, "smooth"]]
    while 1:
        #orange stats
        average_orange_weight = []
        average_orange_texture = []
        orange_bumpy_counter = 0
        orange_smooth_counter = 0
        orange_common = ""
        #apple stats
        average_apple_weight = []
        average_apple_texture = []
        apple_bumpy_counter = 0
        apple_smooth_counter = 0
        apple_common = ""
        for x in range(len(_object)):
            if _object[x] == "orange":
                average_orange_weight.append(_properties[x][0])
                average_orange_texture.append(_properties[x][1])
                #find how many of the oranges are bumpy or smooth
                if "bumpy" in _properties[x][1]:
                    orange_bumpy_counter+=1
                elif "smooth" in _properties[x][1]:
                    orange_smooth_counter+=1
            if _object[x] == "apple":
                average_apple_weight.append(_properties[x][0])
                average_apple_texture.append(_properties[x][1])

                #find how many of the apples are bumpy oe smooth
                if "bumpy" in _properties[x][1]:
                    apple_bumpy_counter+=1
                elif "smooth" in _properties[x][1]:
                    apple_smooth_counter+=1
        #calculate most common texture for apples and oranges
        if orange_bumpy_counter > orange_smooth_counter:
            orange_common = "bumpy"
        elif orange_smooth_counter > orange_bumpy_counter:
            orange_common = "smooth"
        if apple_bumpy_counter > apple_smooth_counter:
            apple_common = "bumpy"
        elif apple_smooth_counter > apple_bumpy_counter:
            apple_common = "smooth"
        avg_orange_weight_sum = int(sum(average_orange_weight)/len(average_orange_weight))
        avg_apple_weight_sum = int(sum(average_apple_weight)/len(average_apple_weight))
        print("#"*40)
        data_weight = int(input(">>Enter weight of fruit (g): "))
        data_texture = str(input(">>Enter texture of fruit (bumpy or smooth): "))
        if data_weight >= avg_apple_weight_sum and data_weight <= max(average_orange_weight):
            if orange_common == data_texture:
                print("From what I know, its most likely an Orange.")
            else:
                print("The weight suggests it is an Orange but the texture says otherwise...")

        elif data_weight <= avg_orange_weight_sum and data_weight >= min(average_apple_weight):
            if apple_common == data_texture:
                print("From the data I have, its probably an Apple.")
            else:
                print("The weight of the object says it could be an Orange however the texture is of an Apple??...")
        elif data_weight < min(average_apple_weight):
            print("Thats too small to be a fruit on record.")
        else:
            print("That value seems too large to be a fruit on record.")
        append_properties = [data_weight, data_texture]
        correct = input("What was the answer? orange or apple?: ")
        if correct == "orange":
            print("Learning from data...")
            _object.append("orange")
            _properties.append(append_properties)
        elif correct == "apple":
            print("Learning from result...")
            _object.append("apple")
            _properties.append(append_properties)
orange_apple()
