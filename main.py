import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("TreviMC")

versions = {
    "1.8.9": ["1_8_9", "1.8"]
}

print("welcome to TreviMC")

print("select a version:")
print(versions.keys())


#print("version: " + versions[selected_ver + ".root"])