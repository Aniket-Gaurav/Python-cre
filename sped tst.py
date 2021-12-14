 # Required Module:- pip install speedtest-cli

import speedtest

spd = speedtest.Speedtest()

print("Testing...\n")

down_spd = spd.download() /1048576

up_spd = spd.upload() / 1048576

pingResult = round(spd.results.ping)

print(f"Download Speed : {down_spd:.2f} Mbps")

print(f"Download Speed : {up_spd:.2f} Mbps")

print(f"Ping : {pingResult} ms")

#  # Display Your Download Speed
# print("Your Download Speed is:", down_spd ,"bytes") 

#  # Display Your Upload Speed
# print("Your Upload Speed is:", up_spd ,"bytes")