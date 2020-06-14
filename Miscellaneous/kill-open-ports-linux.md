# Killing Open Ports in Linux
<!--27 Jan 27 2020 -->
I had this weird error while running Django Development Server.

```
System check identified no issues (0 silenced).
January 27, 2020 - 16:42:39
Django version 2.2.9, using settings 'codeclassroom.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Error: That port is already in use.
```

## Solution
1. Run `netstat -ntlp` to see available open ports.
```
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:42405         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:5940          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      12054/python3       
tcp6       0      0 ::1:631                 :::*                    LISTEN      -  
```

Here is a `man netstat` for what it does
> netstat  -  Print  network connections, routing tables, interface statistics,
       masquerade connections, and multicast memberships

You see the _python3_ one? Kill 😈 this process

2. Run `kill -9 12054`
Kill is used for Removing a background process or job, `-9` specifies SIGKILL (Forced termination) where `12054` is the PID

3. Run the development server again.
