
try:
    f = open("//home//siddiktk//Music//song.txt//sung","w")
    f.write("\n musics are matter but!")
    f.close()

    f = open("//home//siddiktk//Music//song.txt//sung")
    count = 0
    for i in f:
        count = count + 1
        print(f"the file content in line {count}: ",i)
except FileNotFoundError:
    print("file not found.")
    print("try again!.")

