import socket
import serial

# Serial port settings (change to the port your ESP32 is connected to)
SERIAL_PORT = "COM8"  # or '/dev/ttyUSB0' for Linux/macOS
BAUD_RATE = 115200  # Baud rate of the ESP32

# TCP Server Information
TCP_IP = "0.0.0.0"  # Accept connections from all network interfaces
TCP_PORT = 1234  # Port the server listens on

# Open the serial port connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Start the TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(5)
print(f"Server started: {TCP_IP}:{TCP_PORT}")

# Accept a TCP client connection
conn, addr = server_socket.accept()
print(f"Connection received from: {addr}")

try:
    while True:
        # Read data from the serial port
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"Received from Serial Port: {line}")
            # Send the data to the TCP client
            conn.sendall((line + "\n").encode('utf-8'))
except KeyboardInterrupt:
    print("Shutting down the server...")

finally:
    # Close all connections and sockets
    ser.close()
    conn.close()
    server_socket.close()
