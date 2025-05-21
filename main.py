import cv2  # Para capturar video
import mediapipe as mp  # Para detectar manos
import pygame  # Para reproducir sonidos

# Inicializar módulos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
pygame.mixer.init()

# Cargar sonidos asignados por dedo
sounds = [
    pygame.mixer.Sound("sounds/do.mp3"),     # 0 - Anular Derecho
    pygame.mixer.Sound("sounds/re.mp3"),     # 1 - Medio Derecho
    pygame.mixer.Sound("sounds/mi.mp3"),     # 2 - Índice Derecho
    pygame.mixer.Sound("sounds/fa.mp3"),     # 3 - Índice Izquierdo
    pygame.mixer.Sound("sounds/sol.mp3"),    # 4 - Medio Izquierdo
    pygame.mixer.Sound("sounds/la.mp3"),     # 5 - Anular Izquierdo
    pygame.mixer.Sound("sounds/si.mp3")      # 6 - Meñique Izquierdo
]

# Etiquetas de notas para mostrar en pantalla
note_labels = [
    "DO",   # 0
    "RE",   # 1
    "MI",   # 2
    "FA",   # 3
    "SOL",  # 4
    "LA",   # 5
    "SI"    # 6
]

# Verificar si el dedo está presionado (tip debajo del mcp)
def is_finger_down(landmarks, tip_idx, mcp_idx):
    return landmarks[tip_idx].y > landmarks[mcp_idx].y

# Captura de cámara
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

# Modelo de manos
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    finger_state = [False] * 7  # Estado de los dedos (presionado o no)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Espejar imagen
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for h_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if h_index == 1:  # Mano derecha → índices 0-2
                    tip_ids = [16, 12, 8]  # Anular, Medio, Índice
                    mcp_ids = [13, 9, 5]
                    for i in range(3):
                        idx = i  # global 0,1,2
                        if is_finger_down(hand_landmarks.landmark, tip_ids[i], mcp_ids[i]):
                            if not finger_state[idx]:
                                sounds[idx].play()
                                finger_state[idx] = True
                            cv2.putText(frame, note_labels[idx], (10, 50 + idx * 40), font, 1, (0, 255, 0), 2)
                        else:
                            finger_state[idx] = False

                elif h_index == 0:  # Mano izquierda → índices 3-6
                    tip_ids = [8, 12, 16, 20]  # Índice, Medio, Anular, Meñique
                    mcp_ids = [5, 9, 13, 17]
                    for i in range(4):
                        idx = i + 3  # global 3,4,5,6
                        if idx < len(finger_state):
                            if is_finger_down(hand_landmarks.landmark, tip_ids[i], mcp_ids[i]):
                                if not finger_state[idx]:
                                    sounds[idx].play()
                                    finger_state[idx] = True
                                cv2.putText(frame, note_labels[idx], (10, 50 + idx * 40), font, 1, (255, 255, 0), 2)
                            else:
                                finger_state[idx] = False

        cv2.imshow("Hand Music", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
            break

cap.release()
cv2.destroyAllWindows()