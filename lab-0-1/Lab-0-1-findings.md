# Lab 0.1 – Network Fundamentals

## Wireshark Login Capture

A Wireshark packet capture was analyzed to understand the network communication during access to the InstaSafe application.

### TCP Connection

The TCP three-way handshake was observed on port 443:

1. TCP SYN – Client initiates the connection.
2. TCP SYN-ACK – Server responds to the connection request.
3. TCP ACK – Client acknowledges and establishes the TCP connection.

### TLS Communication

The capture shows encrypted HTTPS communication using TLS 1.3.

- TLS Client Hello – Client initiates the secure TLS connection to `secureaccess.instasafe.com`.
- TLS Server Hello – Server responds and continues the TLS handshake.
- TLS Application Data – Encrypted application data is exchanged.

The communication uses HTTPS over TCP port 443.

## Curl Output

A verbose HTTPS request was performed using:
```text
curl.exe -v https://crud.qa.instasafe.io/

<img width="1920" height="1080" alt="10_Curl_Output" src="https://github.com/user-attachments/assets/e349c1b2-29d1-40a3-bfc6-47feffea30af" />

## TLS Client Hello

<img width="1920" height="1080" alt="01_TLS_Client_Hello" src="https://github.com/user-attachments/assets/c2255f50-8b39-43a8-981c-4ad4353eb46f" />

## TLS Server Hello

<img width="1920" height="1080" alt="02_TLS_Server_Hello" src="https://github.com/user-attachments/assets/f5ef15bf-56ce-42da-a69b-9d9a5c4960a8" />

## HTTPS TLS Communication

<img width="1920" height="1080" alt="03_HTTPS_TLS_Communication" src="https://github.com/user-attachments/assets/02f1e3c4-08ac-4823-a695-dcdb6375bcfd" />

## DNS Query and Response

<img width="1920" height="1080" alt="04_DNS_Query_Response" src="https://github.com/user-attachments/assets/cfbf1805-4c29-4b3a-a513-c1519262114b" />

## TCP Three-Way Handshake 

<img width="1920" height="1080" alt="05_TCP_Three_Way_Handshake (2)" src="https://github.com/user-attachments/assets/3f5175b9-be52-408e-a98e-5b327f2461a6" />






