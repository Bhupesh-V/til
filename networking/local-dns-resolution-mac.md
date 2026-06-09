# Discovering devices on your local network (Mac)

## DNS Resolvers

Find which DNS servers your macOS system is querying for website lookups and how network traffic is being routed

```
scutil --dns
```

sample output

```
DNS configuration

resolver #1
  nameserver[0] : 2405:201:1006:e906::c0a8:1d01
  nameserver[1] : 192.168.29.1
  if_index : 12 (en0)
  flags    : Request A records, Request AAAA records
  reach    : 0x00020002 (Reachable,Directly Reachable Address)

resolver #2
  domain   : local
  options  : mdns
  timeout  : 5
  flags    : Request A records, Request AAAA records
  reach    : 0x00000000 (Not Reachable)
  order    : 300000

resolver #3
  domain   : 254.169.in-addr.arpa
  options  : mdns
  timeout  : 5
  flags    : Request A records, Request AAAA records
  reach    : 0x00000000 (Not Reachable)
  order    : 300200

resolver #4
  domain   : 8.e.f.ip6.arpa
  options  : mdns
  timeout  : 5
  flags    : Request A records, Request AAAA records
  reach    : 0x00000000 (Not Reachable)
  order    : 300400

resolver #5
  domain   : 9.e.f.ip6.arpa
  options  : mdns
  timeout  : 5
  flags    : Request A records, Request AAAA records
  reach    : 0x00000000 (Not Reachable)
  order    : 300600

resolver #6
  domain   : a.e.f.ip6.arpa
  options  : mdns
  timeout  : 5
  flags    : Request A records, Request AAAA records
  reach    : 0x00000000 (Not Reachable)
  order    : 300800

resolver #7
  domain   : b.e.f.ip6.arpa
  options  : mdns
  timeout  : 5
  flags    : Request A records, Request AAAA records
  reach    : 0x00000000 (Not Reachable)
  order    : 301000

DNS configuration (for scoped queries)

resolver #1
  nameserver[0] : 2405:201:1006:e906::c0a8:1d01
  nameserver[1] : 192.168.29.1
  if_index : 12 (en0)
  flags    : Scoped, Request A records, Request AAAA records
  reach    : 0x00020002 (Reachable,Directly Reachable Address)

```

- `resolver #1` points to IP address of the router that will be queried for outside traffic, you can see this address change when you connect to work VPN or your personal device hotspot.
- The local devices (`resolver #2`) which are reversed looked using mdns are part of non-scoped queries (which by definition seem like will be used for outside queries, however that's not the case).
  - Unlike resolver #1, Resolver #2 has a strict rule: `domain : local`. It catches anything ending in `.local` and tells the system to use the mDNS protocol instead of traditional DNS.
  - By keeping Resolver #2 non-scoped, mac ensures that if you switch from Wi-Fi to a wired Ethernet cable, local device discovery keeps working seamlessly without restarting your apps (separation of concerns).

## DNS discovery using `dns-sd`

### Watch for printers

```
dns-sd -B _printer._tcp local.
```
or
```
dns-sd -B _http._tcp local.
```

sample output

```
Browsing for _printer._tcp.local.
DATE: ---Tue 09 Jun 2026---
13:26:57.770  ...STARTING...
Timestamp     A/R    Flags  if Domain               Service Type         Instance Name
13:26:57.771  Add        2  12 local.               _printer._tcp.       Canon XXXX series
13:27:21.554  Rmv        0  12 local.               _printer._tcp.       Canon XXXX series
```

### Watch for shared computers/file sharing

```
dns-sd -B _smb._tcp local.
```

sample output

```
Browsing for _smb._tcp.local.
DATE: ---Tue 09 Jun 2026---
13:26:28.548  ...STARTING...
Timestamp     A/R    Flags  if Domain               Service Type         Instance Name
13:26:28.549  Add        2  12 local.               _smb._tcp.           Some Device
13:27:21.554  Rmv        0  12 local.               _smb._tcp.           Some Device
13:27:53.038  Add        2  12 local.               _smb._tcp.           Some Device
13:27:55.302  Rmv        0  12 local.               _smb._tcp.           Some Device
```

## Fun Stuff

### Creating a fake printer

```
dns-sd -R "Fake Office Printer" _printer._tcp local 9100
```

This might not be visible to other devices on the network if AP Isolation is enabled.

For the sake of this infutile exercise, I connected my mac to my phone's hotspot (android, realme)

1. Start a demo http server
   ```
   sudo python3 -m http.server 631
   ```
2. In another term window start a printer

   ```
   dns-sd -R "Narzo Test Printer" _ipp._tcp local 631 txtvers=1 pdl=application/pdf
   ```
3. Download the [Service Browser App](https://play.google.com/store/apps/details?id=com.druk.servicebrowser&hl=en) to check if the mDNS local device is visible. Copy the IP address.
4. Go to android option's to add a printer by IP address.
5. You will see following log on the http server
   ```
   Serving HTTP on :: port 631 (http://[::]:631/) ...
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST /ipp/print HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST /ipp/print HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST /ipp/printer HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST /ipp/printer HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST /ipp HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST /ipp HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST / HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('POST')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "POST / HTTP/1.1" 501 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 400, message Bad request version ('@ßI^')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "ùõ
                                                       +n}¯@ßI^" 400 -
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] code 501, message Unsupported method ('OPTIONS')
   ::ffff:10.233.72.164 - - [09/Jun/2026 14:52:02] "OPTIONS * HTTP/1.1" 501 -
   ```
6. Simulating a printer
   1. Generate a ssl certificate.
   2. Run the following script
      ```
      sudo python3 -c '
      from http.server import BaseHTTPRequestHandler, HTTPServer
      import ssl

      class SecureFakePrinterHandler(BaseHTTPRequestHandler):
          def do_POST(self):
              # 1. Read incoming data length to ensure clean processing
              content_length = int(self.headers.get("Content-Length", 0))
              if content_length > 0:
                  self.rfile.read(content_length)

              # 2. Build a valid, minimal IPP successful response header
              # Bytes represent: IPP version 2.0, status 0x0000 (successful-ok), 
              # request-id 1, operation-attributes-tag, and end-of-attributes-tag.
              ipp_successful_header = b"\x02\x00\x00\x00\x00\x00\x00\x01\x01\x47\x00\x12\x61\x74\x74\x72\x69\x62\x75\x74\x65\x73\x2d\x63\x68\x61\x72\x73\x65\x74\x00\x05\x75\x74\x66\x2d\x38\x03"

              # 3. Send headers matching the expected secure printing format
              self.send_response(200)
              self.send_header("Content-Type", "application/ipp")
              self.send_header("Content-Length", str(len(ipp_successful_header)))
              self.end_headers()
              
              # 4. Write the binary payload back to the Narzo
              self.wfile.write(ipp_successful_header)

          def do_OPTIONS(self):
              self.send_response(200)
              self.send_header("Allow", "POST, OPTIONS")
              self.end_headers()

      print("Secure Fake Printer with IPP payload listening on port 631...");
      server = HTTPServer(("", 631), SecureFakePrinterHandler)
      context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
      context.load_cert_chain(certfile="server.pem")
      server.socket = context.wrap_socket(server.socket, server_side=True)
      server.serve_forever()
      '
      ```
  3. Start a secure broadcast: `dns-sd -R "Narzo Secure Printer" _ipps._tcp local 631 txtvers=1 pdl=application/pdf`
  4. The log should NOT show any error logs, however the android will still say "no printer found", I will leave this as a TODO for future me.