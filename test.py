from subprocess import call

c  = ["./imdb.py", "imdb-template.tex"]
c += map(lambda i: "tt"+str(i), range(100))

try:
    call(c)
except:
    print " ".join(c)
