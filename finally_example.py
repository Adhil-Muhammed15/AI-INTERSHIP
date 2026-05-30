try:
    f = open("sample.txt", "w")
    f.write("Hello")

except:
    print("Some error occurred")

finally:
    f.close()
    print("File closed")