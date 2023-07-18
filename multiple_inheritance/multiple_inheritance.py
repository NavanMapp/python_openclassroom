# Define the Camera, MobilePhone and CameraPhone classes here
class Camera:
    def take_picture(self):
        print("Say cheese!")

class MobilePhone:
    def __init__(self, memory):
        self.memory = memory

class CameraPhone(Camera, MobilePhone):
    pass

if __name__ == '__main__':
    cameraphone = CameraPhone("200KB")
    cameraphone.take_picture()
    print(cameraphone.memory)
