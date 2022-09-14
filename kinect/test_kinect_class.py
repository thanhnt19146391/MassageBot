from pykinect import nui
import numpy as np
import matplotlib.pyplot as plt

class PyKinect():
    def __init__(self):
        self.video_frame = np.empty((480, 640, 4), np.uint8)
        self.depth_frame = self.df = np.empty((480, 640, 1), np.uint16)
        self.ready = 0
        self.kinect = None
        self.count = 0

    def getDepthFrame(self, frame):
        frame.image.copy_bits(self.df.ctypes.data)
        self.df = self.df >> 3
        self.depth_frame = self.df.copy()
        if not self.ready:
            self.count = (self.count + 1) % 1000
        if self.count > 30:
            self.ready = 1
            
        

    # def video_handler_function(frame):
    #     frame.image.copy_bits(video.ctypes.data)

    def Run(self):
        self.kinect = nui.Runtime()
        # Create video frame
        # self.kinect.video_frame_ready += self.video_handler_function
        # self.kinect.video_stream.open(nui.ImageStreamType.Video, 2, nui.ImageResolution.Resolution640x480,nui.ImageType.Color)
        # Create depth frame
        self.kinect.depth_frame_ready += self.getDepthFrame
        self.kinect.depth_stream.open(nui.ImageStreamType.Depth, 2, nui.ImageResolution.Resolution640x480, nui.ImageType.Depth)

    def Stop(self):
        try: 
            self.close()
        except:
            print("Error when stop kinect")
            self.kinect = None

if __name__ == "__main__":
    
    kinectCam = PyKinect()
    kinectCam.Run()
    while True: 
        if kinectCam.ready:
            depthFrame = kinectCam.depth_frame
            plt.imshow(depthFrame)
            plt.show()
        
        
    
    kinectCam.Stop()
    
    
    
    