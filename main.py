from tkinter import image_names


try:
    print("Packages Importing...")
    import cv2
    print("Packages Imported")
except:
    print("Packages cannot imported")

def empty(a):
    pass
#opens a new window in name TrackBars
cv2.namedWindow("TrackBars")
#makes the window since 64x240
cv2.resizeWindow("TrackBars",640 ,240)
#then creates a track bar 0 min 179 max
cv2.createTrackbar("Brightness", "TrackBars", 0, 179, empty)
        
cap = cv2.VideoCapture(0)
#define width
cap.set(3,640)
#define height
cap.set(4,480)
img_counter = 0
#3, 4, 10, is id for options like brightness or height of the frame




while True:
    success, img = cap.read()
    cv2.imshow("Cam", img)   
    #getting the value of brigness from trackbar
    brigthtness = cv2.getTrackbarPos("Brightness", "TrackBars")
     #change the brighness by value of track pos   
    cap.set(10,brigthtness)

    k = cv2.waitKey(1)
    # When press esc close all
    if k%256 == 27:
        break
    # Take screen shoot with space
    elif k%256  == 32:
        #for my photo capture it's create a name and include the location where I want to save my photo
        img_name = f'photos/Photo{img_counter}.jpg'
    #Malik abi bunu hic bilgisayara kaydetmeden yapabiliyoruz demistin ama nasil yapacagimi bulamadim
        cv2.imwrite(img_name, img)
        # img_temp -> temporary image
        img_temp = cv2.imread(img_name)
        print("Screenshot Taken")
        img_counter += 1 
        cv2.imshow(img_name, img_temp)
    #gray when press g
    elif cv2.waitKey(1) & 0xFF == ord('g'):
        gray = cv2.cvtColor(img_temp,    cv2.COLOR_BGR2GRAY)     
        cv2.imshow("Gray", gray)
    elif cv2.waitKey(1) & 0xFF == ord('s'):
            try:
                cv2.imwrite(img_name,gray)
                print("Saved")
            except:
                print("ERROR::Unsaved")
            break
        
        
        
    
            
        
            
            
        
            
            

        
        
        