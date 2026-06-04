def main():
    # No .lower() here since file extensions must always be lowercase
    file = str(input("File: ")).strip()
    _, extension = file.split(".", 1)

    def mediaType(ext):
        match ext:
            case "jpeg" | "jpg":
                return print("image/jpeg")
            case "gif":
                return print("image/gif")
            case "png":
                return print("image/png")
            case "pdf":
                return print("application/pdf")
            case "txt":
                return print("text/plain")
            case "zip":
                operatingSystem = str(input("What's your OS? ")).strip().lower()
                return print("application/x-zip-compressed") if operatingSystem == "windows" or operatingSystem == "win" else print("application/zip")
            case _:
                return print("Unknown")
            
    mediaType(extension)

main()
            