import os
import subprocess
import sys


def install(package):
    os.system("pip install " + str(package))
    reqs = subprocess.check_output([sys.executable, "-m", "pip", "show", str(package)])

    print(str(reqs) + "\n")
    print("Installed " + package.upper() + "\n")


install("PyTweening")
install("python-dateutil")
install("pytz")
install("PyScreeze")
install("PyRect")
install("pyperclip")
install("PyMsgBox")
install("PyGetWindow")
install("PyAutoGUI")
install("numpy")
install("Pillow")
install("pandas")
install("opencv-python")
install("six")
install("MouseInfo")
install("keyboard")
install("pynput")
install("selenium")
install("urllib3")
