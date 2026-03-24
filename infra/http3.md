# Brief intro to HTTP 3

## HTTP/1.1
- Many parallel TCP connections
- Ineffective TCP use
- HTTP head-of-line blocking: finite set of connections, where to put request from a pool of connection

## HTTP/2
- use single connection per host
- Parallel streams.
- TCP head-of-line blocking

## Google QUIC
- Google deployed http2 frames over UDP in 2013

## IETF QUIC
- Faster handshakes
- Earlier data
- Connection-id
- Built on top of UDP instead of IP.
- Its a transport protocol, means different types of application protocols can be built on top of it. One example is HTTP3.
- HTTP3 is built on top of UDP instead of TCP
- QUIC looks like a DDoS Attack.
- High CPU usage (x2)


