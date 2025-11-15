from time import sleep

def readTxtFile(file_path):
    """Returns the text from the file at file_path"""
    try:
        with open(file_path, "r") as f:
            text = f.read().strip()
            return text
    except FileNotFoundError:
        text = ""
        return text
    
def writeTxt(file_path, text):
    """Writes the text to the file at file_path"""
    with open(file_path, "w") as f:
        f.write(text)

def main():
    path = "clockout.txt"
    while True:
        text = input("What EID or \"all\": ")
        writeTxt(path, text)
        while readTxtFile(path) == text:
            continue
        print(F"Text Read: {readTxtFile(path)}")

if __name__ == "__main__":
    main()
