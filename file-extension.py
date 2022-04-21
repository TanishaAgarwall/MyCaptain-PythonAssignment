filename = input("Input the filename: ")
extension = filename.split(".")
t = repr(extension[-1])
print(t)
if t is 'py':
    print("The extension of the file is python")
