import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("TreviMC")

versions = {
    "1_8_9.ver":  "1.8.9",
    "1_8_9.und":  "1_8_9",
    "1_8_9.root": "1.8"
}

selected_ver = "1_8_9"

print("welcome to TreviMC")
print(f"version: {versions[selected_ver + '.root']}")