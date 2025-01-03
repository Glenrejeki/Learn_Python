import cv2

detection = cv2.CascadeClassifier("d:\\SEMESTER 3\\Belajar Python\\Part 1\\Sesi 5\\face_reff.xml")
camera = cv2.VideoCapture(0)

def deteksi_wajah(frame):
  optimazed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = detection.detectMultiScale(optimazed_frame, scaleFactor = 1.1)
  return faces

def drawer_box(frame):
  faces = deteksi_wajah(frame)
  for x, y, w, h in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h),(0,0, 255), 4)
  
def close_window():
  camera.release()
  cv2.destroyAllWindows()
  exit()

def main():
  while True:
    _, frame = camera.read()
    drawer_box(frame)
    cv2.imshow("GlenFace AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  

if __name__ == '__main__':
  main()