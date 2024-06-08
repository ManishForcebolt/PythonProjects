# # open file is in read mode by default

with open("text.txt") as file:
    content = file.read()
    print(content)
    st = type(content)
    print(st)

# content = "Manish Tanwar \nAnne Frank \nAngela Yu"
# #  This will overwrite the content in file
# with open("text.txt", mode="w") as file:
#     file.write("All Gone")

# with open("text.txt", mode="w") as file:
#    file.write(content)
#
# with open("text.txt",mode="a") as file:
#     file.write("\nRajvendra Singh")


with open("") as file:
    file.write("All Gone")



