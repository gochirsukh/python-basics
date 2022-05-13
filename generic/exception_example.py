import os.path

if os.path.exists("/etc/hosts"):
    print("host file exists")
else:
    print("no host file")

