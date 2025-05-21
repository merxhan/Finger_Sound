# Hand Music Player

Este proyecto utiliza visión por computadora para transformar tus manos en un instrumento musical. Mediante el uso de una webcam, detecta qué dedos están presionados (posición abajo) y reproduce notas musicales asignadas a cada dedo.

## 🎯 Objetivo

Permitir que el usuario reproduzca sonidos musicales en tiempo real al mover sus dedos frente a la cámara, simulando un instrumento musical sin contacto físico.

## 📸 Tecnologías Utilizadas

- [OpenCV](https://opencv.org/) — Captura y visualización de video.
- [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker?hl=es-419) — Detección y seguimiento de manos y dedos.
- [Pygame](https://www.pygame.org/) — Reproducción de archivos de audio.

## 🎵 Mapeo de Dedos a Notas

| Mano         | Dedo        | Índice en código | Nota | Archivo de sonido     |
|--------------|-------------|------------------|------|------------------------|
| Derecha      | Anular      | 0                | DO   | `sounds/do.mp3`        |
| Derecha      | Medio       | 1                | RE   | `sounds/re.mp3`        |
| Derecha      | Índice      | 2                | MI   | `sounds/mi.mp3`        |
| Izquierda    | Índice      | 3                | FA   | `sounds/fa.mp3`        |
| Izquierda    | Medio       | 4                | SOL  | `sounds/sol.mp3`       |
| Izquierda    | Anular      | 5                | LA   | `sounds/la.mp3`        |
| Izquierda    | Meñique     | 6                | SI   | `sounds/si.mp3`        |

## 🧠 Lógica del Funcionamiento

- Se usa `MediaPipe` para obtener los puntos clave (landmarks) de cada mano.
- Se evalúa si un dedo está presionado (su punta está por debajo de la base MCP).
- Al detectar un dedo presionado, se reproduce su sonido correspondiente y se muestra el nombre de la nota en pantalla.
- La detección se reinicia cuando el dedo es levantado, permitiendo una nueva reproducción al volver a presionar.

## ▶️ Ejecución

1. Asegúrate de tener una webcam conectada.
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```
   
3. Coloca los archivos de sonido .mp3 dentro de la carpeta sounds/:

4.	Ejecuta el script:

   ````bash
   python main.py
   ````

5.	Usa tus manos frente a la cámara para tocar las notas.

## ⌨️ Controles

Presiona la tecla ESC para salir del programa.

## 📂 Estructura del Proyecto

    Finger_Sound/
    ├── main.py
    └── sound/
        ├── do.mp3
        ├── re.mp3
        ├── mi.mp3
        ├── fa.mp3
        ├── sol.mp3
        ├── la.mp3
        └── si.mp3

## 💡 Ideas Futuras

 - Añadir grabación de secuencias.
 - Cbiar de escala o instrumento.
 - Visualizaciones de onda de sonido.
 - Soporte para múltiples usuarios.

## 🛠️ Requisitos

- Python 3.10
- Webcam funcional

## 📄 Licencia

Este proyecto es de código abierto y puedes modificarlo y redistribuirlo libremente.