from threading import Thread, Event
import subprocess
import socket
import time
import json
import sys
import os

class Server_Node():
    def __init__(self) -> None:
        self.local_ip = self.get_ip()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.local_ip, 51000))
        self.clients = {}
        self.clients_buf = {}
        self.client_status = {}
        self.client_status_buf = {}
        self.stop_event = Event()
        self.connect_thread = Thread(target=self.incoming_connect)
        self.ack_thread = Thread(target=self.ack_client)

    def start(self):
        self.server.listen(5)
        self.connect_thread.start()
        self.ack_thread.start()
        print(f"Server started at {self.local_ip}:51000")

    def get_ip(self):
        dummy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dummy.connect(("8.8.8.8", 80))
        return dummy.getsockname()[0]
    
    def get_connection(self):
        client, addr = self.server.accept()
        self.clients_buf[addr] = client
        self.client_status_buf[addr] = {'status':'connected', 'username':''}
        print(f"Connection from {addr}:{client} has been established!")
        self.sendTextViaSocket('ack', addr, mode='ack')
    

    def sendTextViaSocket(self, message, addr, mode='text'):
        def lost_event(addr):
            if self.client_status_buf[addr]["status"] != 'lost':
                print(f'[SERVER INFO] Client{addr} dead.')
            self.client_status_buf[addr]["status"] = 'lost'
            return addr
        
        client: socket.socket = self.clients[addr] if addr in self.clients else self.clients_buf[addr]
        if mode == 'ack':
            encodedMessage = bytes('ack', 'utf-8')
            try:
                client.sendall(encodedMessage)
                # print(f"[server info] Send Ack to {addr}.")
                encodedAckText = client.recv(1024)
                # print(f"[server info] Ack sended.")
                ackText = encodedAckText.decode('utf-8')
                # print(f"[server info] receive Ack from {addr}, payload:{ackText}.")
                if ackText == "":
                    return lost_event(addr)
                else:
                    if self.client_status_buf[addr]["status"] != 'connected':
                        print(f'[SERVER INFO] Client{addr}:{ackText} connected.')
                    self.client_status_buf[addr]["status"] = 'connected'
                    self.client_status_buf[addr]["username"] = ackText
                    return None
                    
            except ConnectionResetError:
                return lost_event(addr)
            except BrokenPipeError:
                return lost_event(addr)
        else:
            encodedMessage = bytes(message, 'utf-8')
            client.sendall(encodedMessage)

    def incoming_connect(self):
        while not self.stop_event.is_set():
            self.get_connection()

    def ack_client(self):
        while not self.stop_event.is_set():
            dead_clients = []
            self.clients = self.clients_buf.copy()
            self.client_status = self.client_status_buf.copy()
            for addr in self.clients:
                kill = self.sendTextViaSocket('ack', addr, mode='ack')
                if kill != None:
                    dead_clients.append(kill)
            for addr in dead_clients:
                self.clients[addr].close()
                del self.clients_buf[addr]
                del self.client_status_buf[addr]
                print(f'[SERVER INFO] Client{addr} removed.')
            self.clients = self.clients_buf.copy()
            self.client_status = self.client_status_buf.copy()
            self.stop_event.wait(3)
    
    def stop(self):
        self.stop_event.set()
        self.server.close()
        self.connect_thread.join()
        print('Server closed.')

if __name__ == '__main__':
    server = Server_Node()
    try:
        server.start()
    except KeyboardInterrupt:
        print('\nServer stopped.')
        server.stop()
