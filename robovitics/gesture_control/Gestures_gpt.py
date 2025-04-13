import cv2
import mediapipe as mp
import socket

ESP32_IP = "192.168.1.100"  # Replace with your ESP32 IP address
ESP32_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8,
    max_num_hands=1
)

cap = cv2.VideoCapture(0)

FINGER_TIPS = [8, 12, 16, 20]
THUMB_TIP = 4
THUMB_IP = 2

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    fingers_extended = 0  # Default to 0 in case no hand is detected

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        hand_label = results.multi_handedness[0].classification[0].label

        # Count fingers
        for tip in FINGER_TIPS:
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                fingers_extended += 1

        # Thumb
        if hand_label == "Right":
            if hand_landmarks.landmark[THUMB_TIP].x < hand_landmarks.landmark[THUMB_IP].x:
                fingers_extended += 1
        else:
            if hand_landmarks.landmark[THUMB_TIP].x > hand_landmarks.landmark[THUMB_IP].x:
                fingers_extended += 1

        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display and Send Data
    cv2.putText(frame, f"Fingers: {fingers_extended}", (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    try:
        sock.sendto(str(fingers_extended).encode(), (ESP32_IP, ESP32_PORT))
        print(f"Sent data: {fingers_extended}")
    except Exception as e:
        print(f"Error sending data: {e}")

    cv2.imshow("Finger Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
sock.close()
