import webbrowser
import os
def web(url):
    webbrowser.open(url)
# web("https://www.w3schools.com/python/python_file_handling.asp")


# enumerate
f =  open('reg_ex.py', 'r')
for line_no, line in enumerate(f):
    if line_no  == 1: #even number lines (0, 2, 4 ...) go to `lastline`
        print(line)    

#check if file exists or not
if os.path.exists("den.py"):
    print(True)
    os.remove("den.py")
#os.rmdir("myfolder") for deleting entire file