# with open("tempfile.txt", "r") as f:
#     content = f.read()
#     print(content)

with open("tempfile.txt", "a") as f:
    f.write("\nBello")

with open("tempfile.txt", "r") as f:
    print(f.read())