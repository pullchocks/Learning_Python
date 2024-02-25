hello_str = "Hello world!"
hello_int = 21
hello_bool = True
hello_tuple = (21, 32)
hello_list = ["Hello,", "this", "is", "a", "list"]
hello_dict = { "first_name" : "Johnathan",
                "last_name" : "Litke",
                "eye_color"  : "Brown" }
print(hello_list[4])
hello_list[4] += "!"
print(hello_list[4])
print(str(hello_tuple[0]))
print(hello_dict["first_name"]+ " " + hello_dict["last_name"] + " has " + hello_dict["eye_color"] + " eyes.")
print("{0} {1} has {2} eyes.".format(hello_dict["first_name"],
                                                              hello_dict["last_name"],
                                                              hello_dict["eye_color"]))