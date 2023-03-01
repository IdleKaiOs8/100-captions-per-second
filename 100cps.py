import datetime;

msstart = 0
msend = 1
index = 0

f = open("result.srt", "a")

# Default: 10000
while index < 10000:
    index = index + 1
    f.write(str(index) + "\n")
    f.write((str(datetime.timedelta(milliseconds=msstart * 10))[:11] + " --> " + str(datetime.timedelta(milliseconds=msend * 10))[:11] + "\n"))
    f.write(str(index) + "\n\n")
    msstart = msstart + 1
    msend = msend + 1

print("Success!")
f.close()