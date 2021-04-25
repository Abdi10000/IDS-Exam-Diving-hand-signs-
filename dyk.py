import cv2 as cv
import os 
import hand

# The size of webcamera screen
webcamWidth = 1200
webcamHeight = 800

webcam = cv.VideoCapture(0)

webcam.set(cv.CAP_PROP_FRAME_WIDTH, webcamWidth)
webcam.set(cv.CAP_PROP_FRAME_HEIGHT, webcamHeight)

# The folderPath where the diving hand signs are stored  
folderPath = "C:/Users/Abdi/Downloads/DivingHandSigns"
myList = os.listdir(folderPath)
#print(myList)

# Creating a list of images from the diving hand sign file
overlayList = []
for imagePath in myList:
    image = cv.imread(f'{folderPath}/{imagePath}') 
    overlayList.append(image)
    #print(len(overlayList))
    detector = hand.handDetector(detectionCon=0.75)


while True:
    succes, img = webcam.read()
    img = detector.findHands(img)
    ImList = detector.findPosition(img, draw=False)
    img = cv.flip(img, 1)
    
    img [0:120, 0:120] = overlayList[0]

    if len(ImList) != 0:

        # The "Thumbs up/Closed first" statement
        if ImList[8][2] > ImList[6][2] and ImList[12][2] > ImList[10][2] and ImList[16][2] > ImList[14][2] and ImList[20][2] > ImList[18][2]:
            img [0:120, 0:120] = overlayList[0]
            #print("Thumbs up/Closed fist")

        # The "OK sign" statement
        if ImList[8][2] > ImList[6][2] and ImList[12][2] < ImList[10][2] and ImList[16][2] < ImList[14][2] and ImList[20][2] < ImList[18][2]:
            img [0:120, 0:120] = overlayList[1]
            #print("OK sign")            

        # The "Stop sign" statement
        if ImList[8][2] < ImList[6][2] and ImList[12][2] < ImList[10][2] and ImList[16][2] < ImList[14][2] and ImList[20][2] < ImList[18][2]:
            img [0:120, 0:120] = overlayList[2]
            #print("Stop sign")
            
    cv.imshow('Diving Communication Signs', img)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()