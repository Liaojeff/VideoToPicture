import cv2
import os

# 開啟影片檔案 Open the file
cap = cv2.VideoCapture('original.avi')

#設定輸出的資料夾，預設是此檔案所在位置在建立一個output Set output folder here
output_dir = './output'

#如果沒有上述資料夾就建立資料夾 If no output_dir floder than create one
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#設定第一幀的編號 Set first frame's name
c=1

# 用迴圈從影片檔案讀取幀，並顯示出來 Use while to get the frame from video
while(cap.isOpened()):
  ret, frame = cap.read()
  cv2.imwrite(output_dir+'/'+str(c)+'.jpg', frame)
  cv2.imshow('frame',frame)
  c=c+1
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
