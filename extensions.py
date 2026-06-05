def main():
    file = str(input("File: ")).strip().lower()

    def mediaType(ext):
        if ext.endswith(("jpeg", "jpg")):
                print("image/jpeg")
        elif ext.endswith("gif"):
                print("image/gif")
        elif ext.endswith("png"):
                print("image/png")
        elif ext.endswith("pdf"):
                print("application/pdf")
        elif ext.endswith("txt"):
                print("text/plain")
        elif ext.endswith("zip"):
                print("application/zip")
        else:
                print("application/octet-stream")
            
    mediaType(file)

main()
            