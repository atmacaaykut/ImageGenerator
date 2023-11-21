import cv2
import os

# Video dosyasının adı ve yolu
video_path = "Video.mp4"

# Çıkış dizini oluştur
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

# Video dosyasını aç
cap = cv2.VideoCapture(video_path)

# Video özelliklerini al
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Çıkış görsel boyutları
output_size = (416, 416)

# Saniye başına bir görsel oluştur
frame_count = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Görseli yeniden boyutlandır
    resized_frame = cv2.resize(frame, output_size)

    # Çıkış dosyasının adını oluştur
    output_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")

    # Görseli kaydet
    cv2.imwrite(output_path, resized_frame)

    frame_count += 1

    # Belirli bir FPS ile sınırla (örneğin, her saniyede bir)
    cv2.waitKey(1000 // fps)

# Video dosyasını kapat
cap.release()

# Pencereyi kapat
cv2.destroyAllWindows()
