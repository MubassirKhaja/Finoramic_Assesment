import json
import subprocess

success_list = []
failed_list = []
with open(r'C:\Users\KhajaMubassiruddin\Desktop\test_fnr\test.json') as fk:
    json_data = json.load(fk)
    for i in json_data["Dependencies"]:

        cmd = f'pip install {i}'.split()
        x = subprocess.run(cmd, capture_output=False)

        if x.returncode == 1:
            failed_list.append(i)
        else:
            success_list.append(i)
if len(success_list) != 0:
    print("Installation Success")
    print("Installed packages are : ")

    for i in success_list:
        print(i)
if len(failed_list) != 0:
    print("Failed packages")
    for i in failed_list:
        print(i)
