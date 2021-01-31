import serial
import time
import urllib.request

arduinoData = serial.Serial('com3', 9600, timeout= 1)
time.sleep(1)


arduinoData.write('enable'.encode())
time.sleep(1)


URL = 'http://www.robotarm.net/download'

urllib.request.urlretrieve(URL,'command_info.txt')
file_object = open(r"command_info.txt", "r")
lines= file_object.readlines()
    
joint1_original = str(lines[1])
joint2_original = str(lines[2])
joint3_original = str(lines[3])
joint4_original= str(lines[4])
joint5_original = str(lines[5])
joint6_original = str(lines[6])
speed_original = str(lines[7])
gripper_original = int(lines[8])

arduinoData.write(('ss' + speed_original).encode())
time.sleep(1)
arduinoData.write(('s1' + joint1_original).encode())
time.sleep(1)
arduinoData.write(('s2' + joint2_original).encode())
time.sleep(1)
arduinoData.write(('s3' + joint3_original).encode())
time.sleep(1)
arduinoData.write(('s4' + joint4_original).encode())
time.sleep(1)
arduinoData.write(('s5' + joint5_original).encode())
time.sleep(1)
arduinoData.write(('s6' + joint6_original).encode())
time.sleep(1)


if gripper_original == 1:
    #print("close")
    arduinoData.write(('close').encode())
    time.sleep(1)
elif gripper_original == 0:
    #print("open")
    arduinoData.write(('open').encode())
    time.sleep(1)

while True:
    urllib.request.urlretrieve(URL,'command_info.txt')
    file_object = open(r"command_info.txt", "r")
    lines= file_object.readlines()

    joint1 = str(lines[1])
    joint2 = str(lines[2])
    joint3 = str(lines[3])
    joint4 = str(lines[4])
    joint5 = str(lines[5])
    joint6 = str(lines[6])
    speed = str(lines[7])
    gripper = int(lines[8])

    if speed != speed_original:
        arduinoData.write(('ss' + speed).encode())
        time.sleep(2)
        speed_original = speed

    if gripper != gripper_original:
        if gripper == 1:
            arduinoData.write(('close').encode())
            time.sleep(1)
        elif gripper == 0:
            arduinoData.write(('open').encode())
            time.sleep(1)
        gripper_original = gripper
        
    if joint1 != joint1_original:
        arduinoData.write(('s1' + joint1).encode())
        time.sleep(1)
        joint1_original = joint1
        
    if joint2 != joint2_original:
        arduinoData.write(('s2' + joint2).encode())
        time.sleep(1)
        joint2_original = joint2
        
    if joint3 != joint3_original:
        arduinoData.write(('s3' + joint3).encode())
        time.sleep(1)
        joint3_original = joint3

    if joint4 != joint4_original:
        arduinoData.write(('s4' + joint4).encode())
        time.sleep(1)
        joint4_original = joint4
        
    if joint5 != joint5_original:
        arduinoData.write(('s5' + joint5).encode())
        time.sleep(1)
        joint5_original = joint5
        
    if joint6 != joint6_original:
        arduinoData.write(('s6' + joint6).encode())
        time.sleep(1)
        joint6_original = joint6

    
        

























        
    
        
