#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

from numpy.random import RandomState

PORT = 7777

FLAG = """IlxxxUHHxxxxxxRPmxx0pv5TClTkDHLwLjzbUwNk1Jh5hUKefZ1QhYWRzxxxxxxzVRlyhc2xxh7v63fTK4q4c131sBGJktlAwNrfMbVAvefWYkXlxxxxxxxxOpgoSvjuKFWVIfR8xxssxxBhxxZVVUGGwCGsK4xxxEm4U
pxxbc5SxxRUjoxx8LxxMvHCjcZtkPz9ZQoaDDBwY8bhPlOSqvlAPsJYslBnxxnK2kIIQu6SxxbzWCMuZQkYYNBOmUpMiFLaknwPKUuOUb0E8FCJ4xxguAX6QvbTHCqi90Ljsk8CZrD5NxxvENd4esV7z2R9qHRN2xx7Fg
lxxMJHNxxXBbGoN80xxkI5xxxxxxBCTqxxxxxxTt5Co0ZJUxxu4JFaCutDgxxPprXAI8l4ixxOllxxxxxx0oTxxOi4QUxx7vmxxxxxxuYdVahXNOxx76eFg5bYxxxxxxpxxxxNsSxxB8xx3axx2swxxxxxxRqay7xxgdS
xxxhhgwxxxxDPX8iUxxwv3C5qFYxxiKxxDzsXxxHWFupcGrdStzR7iUl9a9xxB1ZcTHrMNixxKkxxqqMyxxMErxxoTZxxbvWxxzh5VxxuDfaYDjjxxxxxGsXGuxxkimxxfCrxxcmxxMBxxD9xx8k8cHE9FxxF66yxxxmY
Axx4Y8fxxnv2q5H9qxxmoaxxxxxxxLGxxlL4Zxx6U8gXteNJHtSPHaWzT4axxt0WU9lut0exxk6xx7ZNbxxmS77xxzxxM4QRxxxxxxxx5NUNjOBzxxtFAfVUA9xxwjZxxJFLxxFpxx3XxxzkxxXNNxxxxxxx8i3Bxx8bu
0xxrlTwxxlDvK38tWxxylxxdgMexxo4xxpI5zxx6nVAYMzXxxSC07k0l0AfxxPkXZhUD0Zoxxtwxx76Mjxxro2BixxxmYXhaxxBoIdaUTbyUzr7CxxoyDiXXvyxxnu2xxJvZxx96xx8kxxEpxxFlxxppkbxxw6Ecxx8ZW
pqxxxTCxxHO9EMTJpxxIyixxxxxxxnPCxxxxxxx16y0NWru8z0ai9pZpUxxxxxxFWgBGIWtxxcOzxxxxxxsbpAcv3xTNEuIAJxxxxxxxut34ggCzxxxxxxxxn2xx80uxx25VxxTyxxhYxxWgxxbydxxxxxxx2RxxxZnlw
RIomTr9zeELOvpjMfBpKnynObsGMvPfWh71ftxx9iu883H6jfMyh8MHKeZJYXudXbsSWabKvkWAmjzHoBe3UYIPzFwMtFrsiZP6U6a4orDVaQIwRTnlMcuz4ai5weCDMEnvzmKNAVW03Bj10oGIuK7CDnodgG7Tnv4LwP
CV55COjvEFHbkZ2g67aL4DcnJsQBv80xxOwnqxx8M98lTs2iEpZonAnvIwgdKsMqtFfpTq9gI8CfbtLoBKQMAqAY0Vu1KGA33Z01v5fKZGWmdRP1PO2rVvqbXa4pz9yRSnIhsD9kZTOVUEEwionIP7IYB6m8tLyLNGMDe
AmvJYyiNalA9YSM5h58O2WEJYOKhU3EsxxxxxxJOP979kT7yWZ6YdlDOiPUl6mE0Suprt1vSlUH7SSiuJfBq7oClpM0e6rqB8ptUWMbcQSqqQgI8HOIiSX4JwM27PTSF9Zw5RyAJmOVYapd8hXtwokuEy4cgbfeCfuqzI
9lIJEm8DMsnL2TJMRrUo57pipc6yI7cTQLLRnMXyibP6jtTOw1P19UgylNoR54RyK12itLkj8ZyTJtsHZV8hUcX47Inp1TcZJyrmMTnFBAAcLIiUCKuBWMNOErnc0GIf5c5JG4mTlccfklIza1rXGDs7rcmZ8XkVQKR5q"""

ENCODED_FLAG = [[ord(x) for x in x] for x in FLAG.split()]
PASSWORD = 84


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=printable-ascii')
        self.end_headers()
        if self.headers['password'] is None or self.headers['password'] == '':
            self.wfile.write(b'Header password missing')
            return
        try:
            password = int(self.headers['password'])
        except ValueError:
            self.wfile.write(b'uint8 expected')
            return
        if password > 256 or password < 0:
            self.wfile.write(b'uint8 expected')
            return

        diff = abs(PASSWORD - password) * 10

        if diff == 0:
            self.wfile.write(b'\n')
            self.wfile.write(b'\n'.join(map(bytes, ENCODED_FLAG)))
            self.wfile.write(b'\n')
            return

        random_state = RandomState(seed=1143)
        generated_mask = random_state.randint(diff, size=(11, 165))
        generated_flag = generated_mask + ENCODED_FLAG
        self.wfile.write(b'\n')
        self.wfile.write(b'\n'.join(map(bytes, generated_flag)))
        self.wfile.write(b'\n')
        return


httpd = HTTPServer(('', PORT), myHandler)
httpd.serve_forever()
