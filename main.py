import os


import cv2

from cvzone.HandTrackingModule import HandDetector

folderPath='Presentation'
#variables
width,height = 1280,720
gestureThreshold=300

 #camera setup

cap = cv2.VideoCapture(0)
cap.set(1,width)
cap.set(2,height)

#get the list of presentation images
pathImages = sorted(os.listdir(folderPath),key=len)
print(pathImages)


#variables
imgNumber= 0
hs,ws=int(120*1.2),(213*1)
gestureThreshold = 300
buttonPressed = False
buttonCounter=0
buttonDelay= 40
annotations = [[]]
annotationsNumber=-1
annotationsStart= False


#Hand Detector
detector = HandDetector(detectionCon=0.8,maxHands=1)





while True:
    #iMPORT Images
    success,img = cap.read()
    img = cv2.flip(img,1)
    pathFullImage= os.path.join(folderPath,pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)


    hands, img = detector.findHands(img)

    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)

    if hands and buttonPressed is False :
        hand=hands[0]
        fingers = detector.fingersUp(hand)
        cx,cy=hand['center']
        lmList=hand['lmList']
        indexFinger =lmList[8][0],lmList[8][1]



        if cy <=gestureThreshold : #  if hand isn at the heighy of the face line above


            #Gesture 1
            if fingers == [1,0,0,0,0]:
                print("Left")
                if imgNumber>0:
                   buttonPressed = True
                   annotations = [[]]
                   annotationsNumber = -1
                   annotationsStart = False
                   imgNumber-=1




            # Gesture 2
            if fingers == [ 0, 0, 0, 0,1]:
                print("Right")

                if imgNumber< len(pathImages)-1:
                 buttonPressed = True
                 annotations = [[]]
                 annotationsNumber = -1
                 annotationsStart = False
                 imgNumber+=1




        # Gesture 3 Showpointer
        if fingers == [0,1,1,0,0]:
         cv2.circle(imgCurrent, indexFinger,12,(0,0,255),cv2.FILLED)

        # Gesture 4 draw
        if fingers == [0, 1, 0, 0, 0]:
            if annotationsStart is False:
                annotationsStart= True
                annotationsNumber+=1
                annotations.append([])


            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationsNumber].append(indexFinger)
        else:
         annotationsStart= False





   # button pressed iteration

    if buttonPressed:
        buttonCounter+=1
        if buttonCounter > buttonDelay :
            buttonCounter = 0
            buttonPressed = False



    for i in range( len(annotations)):
        for j in range(len(annotations[i])):
          if j !=0:
           cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,200),12)


   #adding Webcam image on the slide
    imgSmall= cv2.resize(img,(ws,hs))
    h, w, _ = imgSmall.shape
    imgCurrent[0:hs,w-ws:w]= imgSmall


    cv2.imshow("Image",img)
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break