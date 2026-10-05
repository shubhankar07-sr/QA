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
<img width="1920" height="1080" alt="10_Curl_Output" src="https://github.com/user-attachments/assets/ec7155c4-3c77-47dd-ac7a-6d4662192f2e" />

<img width="1920" height="1080" alt="Screenshot 2026-10-05 183217" src="https://github.com/user-attachments/assets/bd431014-0bdd-4a87-82d4-a648eb8adffb" />



```text
curl.exe -v https://crud.qa.instasafe.io/


