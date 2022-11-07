**Descripcion**

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/WebNet0]
└─$ ssldump -r capture.pcap -k picopico.key -d
New TCP connection #1: 128.237.140.23(57567) <-> 172.31.22.220(443)
1 1  0.0288 (0.0288)  C>S  Handshake
      ClientHello
        Version 3.3 
        cipher suites
        TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
        TLS_DH_DSS_WITH_AES_256_GCM_SHA384
        TLS_DH_RSA_WITH_AES_256_GCM_SHA384
        TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
        TLS_DH_RSA_WITH_AES_256_CBC_SHA256
        TLS_DH_DSS_WITH_AES_256_CBC_SHA256
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA
        TLS_DH_RSA_WITH_AES_256_CBC_SHA
        TLS_DH_DSS_WITH_AES_256_CBC_SHA
        TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384
        TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384
        TLS_ECDH_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA
        TLS_RSA_WITH_AES_256_GCM_SHA384
        TLS_RSA_WITH_AES_256_CBC_SHA256
        TLS_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
        TLS_DH_DSS_WITH_AES_128_GCM_SHA256
        TLS_DH_RSA_WITH_AES_128_GCM_SHA256
        TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
        TLS_DH_RSA_WITH_AES_128_CBC_SHA256
        TLS_DH_DSS_WITH_AES_128_CBC_SHA256
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA
        TLS_DH_RSA_WITH_AES_128_CBC_SHA
        TLS_DH_DSS_WITH_AES_128_CBC_SHA
        TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256
        TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256
        TLS_ECDH_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA
        TLS_RSA_WITH_AES_128_GCM_SHA256
        TLS_RSA_WITH_AES_128_CBC_SHA256
        TLS_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA
        TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA
        TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA
        TLS_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_EMPTY_RENEGOTIATION_INFO_SCSV
        compression methods
                  NULL
        extensions
          server_name
              host_name: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
          ec_point_formats

          supported_groups

          session_ticket
          signature_algorithms
          heartbeat
          padding
        ja3 string: 771,49200-49196-49192-49188-49172-49162-165-161-159-107-105-104-57-55-54-49202-49198-49194-49190-49167-49157-157-61-53-49199-49195-49191-49187-49171-49161-164-160-158-103-63-62-51-49-48-49201-49197-49193-49189-49166-49156-156-60-47-49170-49160-22-16-13-49165-49155-10-255,0-11-10-35-13-15-21,23-25-28-27-24-26-22-14-13-11-12-9-10,0-1-2
        ja3 fingerprint: b6782c18655e47a83cfc082c8e71afd9
1 2  0.0295 (0.0006)  S>C  Handshake
      ServerHello
        Version 3.3 
        session_id[0]=

        cipherSuite         TLS_RSA_WITH_AES_256_GCM_SHA384
        compressionMethod                   NULL
        extensions
          renegotiation_info
          session_ticket
        ja3s string: 771,157,65281-35
        ja3s fingerprint: 7c02dbae662670040c7af9bd15fb7e2f
1 3  0.0295 (0.0000)  S>C  Handshake
      Certificate
1 4  0.0295 (0.0000)  S>C  Handshake
      ServerHelloDone
New TCP connection #2: 128.237.140.23(57578) <-> 172.31.22.220(443)
2 1  0.0332 (0.0332)  C>S  Handshake
      ClientHello
        Version 3.3 
        cipher suites
        TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
        TLS_DH_DSS_WITH_AES_256_GCM_SHA384
        TLS_DH_RSA_WITH_AES_256_GCM_SHA384
        TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
        TLS_DH_RSA_WITH_AES_256_CBC_SHA256
        TLS_DH_DSS_WITH_AES_256_CBC_SHA256
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA
        TLS_DH_RSA_WITH_AES_256_CBC_SHA
        TLS_DH_DSS_WITH_AES_256_CBC_SHA
        TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384
        TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384
        TLS_ECDH_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA
        TLS_RSA_WITH_AES_256_GCM_SHA384
        TLS_RSA_WITH_AES_256_CBC_SHA256
        TLS_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
        TLS_DH_DSS_WITH_AES_128_GCM_SHA256
        TLS_DH_RSA_WITH_AES_128_GCM_SHA256
        TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
        TLS_DH_RSA_WITH_AES_128_CBC_SHA256
        TLS_DH_DSS_WITH_AES_128_CBC_SHA256
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA
        TLS_DH_RSA_WITH_AES_128_CBC_SHA
        TLS_DH_DSS_WITH_AES_128_CBC_SHA
        TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256
        TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256
        TLS_ECDH_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA
        TLS_RSA_WITH_AES_128_GCM_SHA256
        TLS_RSA_WITH_AES_128_CBC_SHA256
        TLS_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA
        TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA
        TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA
        TLS_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_EMPTY_RENEGOTIATION_INFO_SCSV
        compression methods
                  NULL
        extensions
          server_name
              host_name: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
          ec_point_formats

          supported_groups

          session_ticket
          signature_algorithms
          heartbeat
          padding
        ja3 string: 771,49200-49196-49192-49188-49172-49162-165-161-159-107-105-104-57-55-54-49202-49198-49194-49190-49167-49157-157-61-53-49199-49195-49191-49187-49171-49161-164-160-158-103-63-62-51-49-48-49201-49197-49193-49189-49166-49156-156-60-47-49170-49160-22-16-13-49165-49155-10-255,0-11-10-35-13-15-21,23-25-28-27-24-26-22-14-13-11-12-9-10,0-1-2
        ja3 fingerprint: b6782c18655e47a83cfc082c8e71afd9
2 2  0.0335 (0.0003)  S>C  Handshake
      ServerHello
        Version 3.3 
        session_id[0]=

        cipherSuite         TLS_RSA_WITH_AES_256_GCM_SHA384
        compressionMethod                   NULL
        extensions
          renegotiation_info
          session_ticket
        ja3s string: 771,157,65281-35
        ja3s fingerprint: 7c02dbae662670040c7af9bd15fb7e2f
2 3  0.0335 (0.0000)  S>C  Handshake
      Certificate
2 4  0.0335 (0.0000)  S>C  Handshake
      ServerHelloDone
1 5  0.0596 (0.0301)  C>S  Handshake
      ClientKeyExchange
1 6  0.0596 (0.0000)  C>S  ChangeCipherSpec
1 7  0.0596 (0.0000)  C>S  Handshake
      Finished
1 8  0.0613 (0.0017)  S>C  Handshake
1 9  0.0613 (0.0000)  S>C  ChangeCipherSpec
1 10 0.0613 (0.0000)  S>C  Handshake
      Finished
2 5  0.0672 (0.0336)  C>S  Handshake
      ClientKeyExchange
2 6  0.0672 (0.0000)  C>S  ChangeCipherSpec
2 7  0.0672 (0.0000)  C>S  Handshake
      Finished
2 8  0.0689 (0.0016)  S>C  Handshake
2 9  0.0689 (0.0000)  S>C  ChangeCipherSpec
2 10 0.0689 (0.0000)  S>C  Handshake
      Finished
New TCP connection #3: 128.237.140.23(57581) <-> 172.31.22.220(443)
3 1  0.0297 (0.0297)  C>S  Handshake
      ClientHello
        Version 3.3 
        cipher suites
        TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
        TLS_DH_DSS_WITH_AES_256_GCM_SHA384
        TLS_DH_RSA_WITH_AES_256_GCM_SHA384
        TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
        TLS_DH_RSA_WITH_AES_256_CBC_SHA256
        TLS_DH_DSS_WITH_AES_256_CBC_SHA256
        TLS_DHE_RSA_WITH_AES_256_CBC_SHA
        TLS_DH_RSA_WITH_AES_256_CBC_SHA
        TLS_DH_DSS_WITH_AES_256_CBC_SHA
        TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384
        TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384
        TLS_ECDH_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA
        TLS_RSA_WITH_AES_256_GCM_SHA384
        TLS_RSA_WITH_AES_256_CBC_SHA256
        TLS_RSA_WITH_AES_256_CBC_SHA
        TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
        TLS_DH_DSS_WITH_AES_128_GCM_SHA256
        TLS_DH_RSA_WITH_AES_128_GCM_SHA256
        TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA256
        TLS_DH_RSA_WITH_AES_128_CBC_SHA256
        TLS_DH_DSS_WITH_AES_128_CBC_SHA256
        TLS_DHE_RSA_WITH_AES_128_CBC_SHA
        TLS_DH_RSA_WITH_AES_128_CBC_SHA
        TLS_DH_DSS_WITH_AES_128_CBC_SHA
        TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256
        TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256
        TLS_ECDH_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA
        TLS_RSA_WITH_AES_128_GCM_SHA256
        TLS_RSA_WITH_AES_128_CBC_SHA256
        TLS_RSA_WITH_AES_128_CBC_SHA
        TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA
        TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA
        TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA
        TLS_RSA_WITH_3DES_EDE_CBC_SHA
        TLS_EMPTY_RENEGOTIATION_INFO_SCSV
        compression methods
                  NULL
        extensions
          server_name
              host_name: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
          ec_point_formats

          supported_groups

          session_ticket
          signature_algorithms
          heartbeat
          padding
        ja3 string: 771,49200-49196-49192-49188-49172-49162-165-161-159-107-105-104-57-55-54-49202-49198-49194-49190-49167-49157-157-61-53-49199-49195-49191-49187-49171-49161-164-160-158-103-63-62-51-49-48-49201-49197-49193-49189-49166-49156-156-60-47-49170-49160-22-16-13-49165-49155-10-255,0-11-10-35-13-15-21,23-25-28-27-24-26-22-14-13-11-12-9-10,0-1-2
        ja3 fingerprint: b6782c18655e47a83cfc082c8e71afd9
3 2  0.0301 (0.0003)  S>C  Handshake
      ServerHello
        Version 3.3 
        session_id[0]=

        cipherSuite         TLS_RSA_WITH_AES_256_GCM_SHA384
        compressionMethod                   NULL
        extensions
          renegotiation_info
          session_ticket
        ja3s string: 771,157,65281-35
        ja3s fingerprint: 7c02dbae662670040c7af9bd15fb7e2f
3 3  0.0301 (0.0000)  S>C  Handshake
      Certificate
3 4  0.0301 (0.0000)  S>C  Handshake
      ServerHelloDone
3 5  0.0598 (0.0296)  C>S  Handshake
      ClientKeyExchange
3 6  0.0598 (0.0000)  C>S  ChangeCipherSpec
3 7  0.0598 (0.0000)  C>S  Handshake
      Finished
3 8  0.0607 (0.0009)  S>C  Handshake
3 9  0.0607 (0.0000)  S>C  ChangeCipherSpec
3 10 0.0607 (0.0000)  S>C  Handshake
      Finished
3 11 0.0953 (0.0345)  C>S  application_data
    ---------------------------------------------------------------
    GET / HTTP/1.1
    Host: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    Pragma: no-cache
    Cache-Control: no-cache
    
    ---------------------------------------------------------------
3 12 0.0958 (0.0004)  S>C  application_data
    ---------------------------------------------------------------
    48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d    HTTP/1.1 200 OK.
    0a 44 61 74 65 3a 20 46 72 69 2c 20 32 33 20 41    .Date: Fri, 23 A
    75 67 20 32 30 31 39 20 31 35 3a 35 36 3a 33 36    ug 2019 15:56:36
    20 47 4d 54 0d 0a 53 65 72 76 65 72 3a 20 41 70     GMT..Server: Ap
    61 63 68 65 2f 32 2e 34 2e 32 39 20 28 55 62 75    ache/2.4.29 (Ubu
    6e 74 75 29 0d 0a 4c 61 73 74 2d 4d 6f 64 69 66    ntu)..Last-Modif
    69 65 64 3a 20 4d 6f 6e 2c 20 31 32 20 41 75 67    ied: Mon, 12 Aug
    20 32 30 31 39 20 31 36 3a 35 30 3a 30 35 20 47     2019 16:50:05 G
    4d 54 0d 0a 45 54 61 67 3a 20 22 35 66 66 2d 35    MT..ETag: "5ff-5
    38 66 65 65 35 30 64 63 33 66 62 30 2d 67 7a 69    8fee50dc3fb0-gzi
    70 22 0d 0a 41 63 63 65 70 74 2d 52 61 6e 67 65    p"..Accept-Range
    73 3a 20 62 79 74 65 73 0d 0a 56 61 72 79 3a 20    s: bytes..Vary: 
    41 63 63 65 70 74 2d 45 6e 63 6f 64 69 6e 67 0d    Accept-Encoding.
    0a 43 6f 6e 74 65 6e 74 2d 45 6e 63 6f 64 69 6e    .Content-Encodin
    67 3a 20 67 7a 69 70 0d 0a 50 69 63 6f 2d 46 6c    g: gzip..Pico-Fl
    61 67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67    ag: picoCTF{nong
    73 68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63    shim.shrimp.crac
    6b 65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c    kers}..Content-L
    65 6e 67 74 68 3a 20 38 32 31 0d 0a 4b 65 65 70    ength: 821..Keep
    2d 41 6c 69 76 65 3a 20 74 69 6d 65 6f 75 74 3d    -Alive: timeout=
    35 2c 20 6d 61 78 3d 31 30 30 0d 0a 43 6f 6e 6e    5, max=100..Conn
    65 63 74 69 6f 6e 3a 20 4b 65 65 70 2d 41 6c 69    ection: Keep-Ali
    76 65 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 65    ve..Content-Type
    3a 20 74 65 78 74 2f 68 74 6d 6c 0d 0a 0d 0a 1f    : text/html.....
    8b 08 00 00 00 00 00 00 03 a5 54 5d 73 da 3a 14    ..........T]s.:.
    7c 4e 7e 85 e2 d7 c4 16 2e 04 c8 1d 9b 99 24 34    |N~...........$4
    05 67 28 e1 23 40 f2 26 6c d9 96 2b 4b 42 12 1f    .g(.#@.&l..+KB..
    e6 d7 5f d9 84 90 66 da 4e ef 5c 5e 2c 1f 2d 47    .._...f.N.\^,.-G
    bb 7b d6 f2 2e 22 1e ea 42 60 90 ea 9c 76 ce bd    .{..."..B`...v..
    f2 01 28 62 89 6f 61 66 75 ce 01 f0 52 8c a2 72    ..(b.oafu...R..r
    61 96 17 b6 0d c6 78 b5 26 12 47 20 c7 1a 01 8d    a.....x.&.G ....
    12 05 6c fb 6d bf 2a 85 29 92 0a 6b df 5a eb d8    ..l.m.*.)..k.Z..
    6e 5b 1f b7 18 ca b1 6f 6d 08 de 0a 2e b5 05 42    n[.....om......B
    ce 34 66 06 ba 25 91 4e fd 08 6f 48 88 ed ea e5    .4f..%.N..oH....
    0a 10 46 34 41 d4 56 21 a2 d8 77 af 80 4a 25 61    ..F4A.V!..w..J%a
    3f 6c cd ed 98 68 9f 71 d3 fa 44 eb 8e 73 ad b4    ?l...h.q..D..s..
    44 02 dc 4f 26 27 46 d4 fc 03 48 4c 7d 4b e9 82    D..O&'F...HL}K..
    62 95 62 6c ce 4d 25 8e 7d 2b d5 5a a8 7f 20 54    b.bl.M%.}+.Z.. T
    1a 85 3f 04 d2 a9 b3 3c 36 09 23 e6 84 3c 87 ef    ..?....<6.#..<..
    05 d8 70 ea 8e 0b 43 a5 4e 35 27 27 06 a5 94 65    ..p...C.N5''...e
    a8 6a 9c 48 a2 0b 73 4c 8a ea ed 86 9d 24 c3 62    .j.H..sL.....$.b
    5c 23 8b fb e5 60 b4 a9 2f 88 c8 51 bd 31 e8 5e    \#...`../..Q.1.^
    46 3d e8 c6 a3 56 bb 01 b3 66 f8 02 49 30 1d 3d    F=...V...f..I0.=
    0f d3 70 2e 5b bb 9b 60 c3 c7 bb e9 97 c1 eb d6    ..p.[..`........
    9d 1a 6f 24 57 8a 4b 92 10 e6 5b 88 71 56 e4 7c    ..o$W.K...[.qV.|
    ad ac 0f 93 b8 5f 2b cd 73 70 10 06 62 2e 81 4e    ....._+.sp..b..N
    89 02 1a e7 82 22 8d 3f 99 70 d0 6c b4 4a 8d a5    .....".?.p.l.J..
    7d 04 1d f8 7f 36 e8 68 ac 26 9a e2 4e 0f 53 ca    }....6.h.&..N.S.
    af c0 96 4b 1a 5d 78 f0 50 2c 93 01 8f d1 f0 96    ...K.]x.P,......
    3c 2a 3a e7 67 5e 44 36 20 a4 48 29 df 2a 67 8b    <*:.g^D6 .H).*g.
    08 c3 f2 8d 32 00 67 3f ed 7f 66 f2 0e ab 80 a9    ....2.g?..f.....
    db 99 63 6a 46 80 81 e6 e0 16 4c 90 41 61 f0 84    ..cjF.....L.Aa..
    12 6c 8e 75 7f c2 8a 63 4b 6a e8 98 36 67 e6 37    .l.u...cKj..6g.7
    4d b1 c4 c0 b8 41 71 42 34 60 dc 58 c3 92 b2 97    M....AqB4`.X....
    c2 26 ec 66 d3 f1 96 b2 c2 7a 50 7c 60 08 0d c5    .&.f.....zP|`...
    52 49 f5 ac 6c 86 ce bb 94 ca d2 d3 00 86 42 13    RI..l.........B.
    ce 10 05 01 da a0 49 28 89 d0 27 d3 4b 40 36 5a    ......I(..'.K@6Z
    63 59 80 98 48 a5 af cc 74 30 03 4f 5c 08 2c 9d    cY..H...t0.O\.,.
    4c bd bd 9f 72 1b 7c 88 ad 3a 34 53 32 3c c5 34    L...r.|..:4S2<.4
    e4 11 76 b2 55 d9 b1 ca e6 61 69 d7 cb 60 3a 8a    ..v.U....ai..`:.
    92 bc ca 63 f6 cb 38 ae da 04 2e 2e 6f 9a d7 dd    ...c..8.....o...
    fd b0 26 a7 2d b4 7c 6c b8 c1 44 8f fa b7 ab 59    ..&.-.|l..D....Y
    32 9e ed c5 72 cf af 55 be 78 14 8d 97 78 bc e9    2...r..U.x...x..
    5d b6 d1 52 4f bf ba 4f a4 99 91 3d ff 7d 1c 3d    ]..RO..O...=.}.=
    78 e0 fa 27 e2 11 cb 94 13 52 be 8e 62 8a 8c f3    x..'.....R..b...
    25 7b 94 a1 1d a4 64 a9 a0 38 3a 02 5d c7 6d 38    %{....d..8:.].m8
    2d b8 ce a3 63 f1 f7 8a 9e 87 5f f0 b4 76 2f 7a    -...c....._..v/z
    ab 68 12 8c 9a 69 a0 8b eb c7 99 48 f5 53 ba 9f    .h...i.....H.S..
    67 37 f3 a1 1b d2 de 74 f0 0d d5 83 ee eb 56 b2    g7.....t......V.
    d1 aa a1 1e da cd a8 df fb de dd d7 e6 ee ff 52    ...............R
    f4 1f 6e 8c ec f3 85 f1 6b 39 41 36 c9 67 49 11    ..n.....k9A6.gI.
    d5 44 5d 2c ee 5c 39 26 cb d7 e7 db 17 de ef 17    .D],.\9&........
    cd a1 1c 35 67 32 eb 7f 45 0f 31 64 c1 b7 7d 7f    ...5g2..E.1d..}.
    f7 d0 55 71 63 57 db f5 07 97 77 b5 56 36 1e fc    ..UqcW....w.V6..
    9d 1c 0f 1e 3e 54 f3 09 55 d7 fd bf 29 b5 3f 87    ....>T..U...).?.
    ff 05 00 00                                        ....
    ---------------------------------------------------------------
1 11 0.3571 (0.2957)  C>S  application_data
    ---------------------------------------------------------------
    GET /starter-template.css HTTP/1.1
    Host: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
    Accept: text/css,*/*;q=0.1
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Referer: https://ec2-18-223-184-200.us-east-2.compute.amazonaws.com/
    Pragma: no-cache
    Cache-Control: no-cache
    
    ---------------------------------------------------------------
1 12 0.3575 (0.0004)  S>C  application_data
    ---------------------------------------------------------------
    48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d    HTTP/1.1 200 OK.
    0a 44 61 74 65 3a 20 46 72 69 2c 20 32 33 20 41    .Date: Fri, 23 A
    75 67 20 32 30 31 39 20 31 35 3a 35 36 3a 33 36    ug 2019 15:56:36
    20 47 4d 54 0d 0a 53 65 72 76 65 72 3a 20 41 70     GMT..Server: Ap
    61 63 68 65 2f 32 2e 34 2e 32 39 20 28 55 62 75    ache/2.4.29 (Ubu
    6e 74 75 29 0d 0a 4c 61 73 74 2d 4d 6f 64 69 66    ntu)..Last-Modif
    69 65 64 3a 20 4d 6f 6e 2c 20 31 32 20 41 75 67    ied: Mon, 12 Aug
    20 32 30 31 39 20 31 36 3a 34 37 3a 30 35 20 47     2019 16:47:05 G
    4d 54 0d 0a 45 54 61 67 3a 20 22 36 32 2d 35 38    MT..ETag: "62-58
    66 65 65 34 36 32 62 66 32 32 37 2d 67 7a 69 70    fee462bf227-gzip
    22 0d 0a 41 63 63 65 70 74 2d 52 61 6e 67 65 73    "..Accept-Ranges
    3a 20 62 79 74 65 73 0d 0a 56 61 72 79 3a 20 41    : bytes..Vary: A
    63 63 65 70 74 2d 45 6e 63 6f 64 69 6e 67 0d 0a    ccept-Encoding..
    43 6f 6e 74 65 6e 74 2d 45 6e 63 6f 64 69 6e 67    Content-Encoding
    3a 20 67 7a 69 70 0d 0a 50 69 63 6f 2d 46 6c 61    : gzip..Pico-Fla
    67 3a 20 70 69 63 6f 43 54 46 7b 6e 6f 6e 67 73    g: picoCTF{nongs
    68 69 6d 2e 73 68 72 69 6d 70 2e 63 72 61 63 6b    him.shrimp.crack
    65 72 73 7d 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65    ers}..Content-Le
    6e 67 74 68 3a 20 31 30 30 0d 0a 4b 65 65 70 2d    ngth: 100..Keep-
    41 6c 69 76 65 3a 20 74 69 6d 65 6f 75 74 3d 35    Alive: timeout=5
    2c 20 6d 61 78 3d 31 30 30 0d 0a 43 6f 6e 6e 65    , max=100..Conne
    63 74 69 6f 6e 3a 20 4b 65 65 70 2d 41 6c 69 76    ction: Keep-Aliv
    65 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 65 3a    e..Content-Type:
    20 74 65 78 74 2f 63 73 73 0d 0a 0d 0a 1f 8b 08     text/css.......
    00 00 00 00 00 00 03 4b ca 4f a9 54 a8 e6 52 50    .......K.O.T..RP
    28 48 4c 49 c9 cc 4b d7 2d c9 2f b0 52 30 2d 4a    (HLI..K.-./.R0-J
    cd b5 e6 aa e5 d2 2b 2e 49 2c 2a 49 2d d2 2d 49    ......+.I,*I-.-I
    cd 2d c8 49 2c 49 45 56 6a a5 60 0c 54 a6 60 a8    .-.I,IEVj.`.T.`.
    07 51 ad a0 50 92 5a 51 a2 9b 98 93 99 9e 67 a5    .Q..P.ZQ......g.
    90 9c 9a 07 d4 07 32 03 00 20 cc fb a0 62 00 00    ......2.. ...b..
    00                                                 .
    ---------------------------------------------------------------
1 13 0.8170 (0.4595)  C>S  application_data
    ---------------------------------------------------------------
    GET /favicon.ico HTTP/1.1
    Host: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
    Accept: image/webp,*/*
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    
    ---------------------------------------------------------------
1 14 0.8173 (0.0003)  S>C  application_data
    ---------------------------------------------------------------
    HTTP/1.1 404 Not Found
    Date: Fri, 23 Aug 2019 15:56:37 GMT
    Server: Apache/2.4.29 (Ubuntu)
    Content-Length: 326
    Keep-Alive: timeout=5, max=99
    Connection: Keep-Alive
    Content-Type: text/html; charset=iso-8859-1
    
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html><head>
    <title>404 Not Found</title>
    </head><body>
    <h1>Not Found</h1>
    <p>The requested URL /favicon.ico was not found on this server.</p>
    <hr>
    <address>Apache/2.4.29 (Ubuntu) Server at ec2-18-223-184-200.us-east-2.compute.amazonaws.com Port 443</address>
    </body></html>
    ---------------------------------------------------------------
Cleaned 3 remaining connection(s) from connection pool
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/WebNet0]
└─$ 
```
revisamos todo lo que nos da y vemos la bandera 

picoCTF{nonghim.shrimp.crackers}

