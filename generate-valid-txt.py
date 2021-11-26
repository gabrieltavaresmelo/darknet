import os

image_files = []
os.chdir(os.path.join("data", "valid"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        image_files.append("data/valid/" + filename)
os.chdir("..")

print(image_files)

with open("valid.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")



# colocar esse arquivo na raiz do diretorio darknet