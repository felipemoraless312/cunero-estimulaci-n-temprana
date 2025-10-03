import cv2
import numpy as np

def get_color_name(b, g, r):
    if r > 150 and g < 80 and b < 80:
        return "Rojo"
    elif r < 100 and g > 200 and b < 100:
        return "Verde"
    elif r < 100 and g > 90 and b > 210:
        return "Azul"
    elif r > 200 and g > 200 and b < 100:
        return "Amarillo"
    elif r > 60 and g > 50 and b > 50:
        return "Negro"
    elif r > 200 and g > 200 and b > 200:
        return "Blanco"
    else:
        return "Otro"
    
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w, _ = frame.shape
    roi_size = 50
    x1 = w // 2 - roi_size
    y1 = h // 2 - roi_size
    x2 = w // 2 + roi_size
    y2 = h // 2 + roi_size

    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 230), 2)

    roi = frame[y1:y2, x1:x2]
    b, g, r = np.mean(roi, axis=(0, 1))
    color_name = get_color_name(b, g, r)

    color_info = f"{color_name} (R:{int(r)} G:{int(g)} B:{int(b)})"
    cv2.putText(frame, color_info, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Detector de Colores", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()