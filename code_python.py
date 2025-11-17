import serial
import time

# ----------------------
# Configuration du port
# ----------------------
PORT = "COM11"      # change selon ton PC (ex: "/dev/ttyACM0" sous Linux)
BAUDRATE = 1000000 # 1 Mbit/s

print("Connexion au port série...")
ser = serial.Serial(PORT, BAUDRATE, timeout=1)

# Attendre que l'Arduino reset (USB)
time.sleep(2)

# ----------------------
# Envoi du caractère spécial
# ----------------------
print("Envoi du caractère spécial pour démarrer l'Arduino...")
ser.write(b"#")  # start char
time.sleep(0.1)

# ----------------------
# Lecture des données
# ----------------------
print("Lecture des messages Arduino :\n")

try:
    while True:
        line = ser.readline().decode(errors='ignore').strip()
        if line:
            print(f"> {line}")

except KeyboardInterrupt:
    print("\nFermeture du port série.")

finally:
    ser.close()