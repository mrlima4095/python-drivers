import cv2
import sys

def photo(filename='foto.jpg'):
    try:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("[-] Cannot open camera")
            return

        # Captura um único frame
        ret, frame = cap.read()

        if ret:
            # Salva a imagem
            cv2.imwrite(filename, frame)
            print(f"[+] Saved photo as '{filename}'")
        else:
            print("[-] Camera crashed while take photo")

        # Libera a câmera
        cap.release()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def video(filename='video.avi'):
    try:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("[-] Cannot open camera")
            return

        largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (largura, altura))

        print("[+] Recording... Press Ctrl+C to stop.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            out.write(frame)
            cv2.imshow('Gravando...', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    except KeyboardInterrupt:
        print("\n[-] User stopped recording (Ctrl+C).")

    finally:
        # Libera tudo
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print(f"[+] Saved video as '{filename}'")

if __name__ == "__main__":
    if sys.argv[1] == "photo": photo() 
    elif sys.argv[1] == "video": video() 
