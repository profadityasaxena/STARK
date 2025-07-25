import socket
import json

log_data = {
    "service": "stark-agent",
    "level": "INFO",
    "message": "Agent started successfully",
    "timestamp": "2025-07-25T15:00:00"
}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5044))
sock.sendall(json.dumps(log_data).encode("utf-8"))
sock.close()
