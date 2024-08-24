File = input("File Name: ").strip().lower()
name = None
extension = None
if "." in File:
    name, *extension = File.split(".")

if extension and extension[-1] in ("gif", "png"):
    print(f"image/{extension[-1]}")
elif extension and extension[-1] in ("jpg", "jpeg"):
    print("image/jpeg")
elif extension and extension[-1] in ("pdf", "zip"):
    print(f"application/{extension[-1]}")
elif extension and extension[-1] == "txt":
    print("text/plain")
else:
    print("application/octet-stream")
