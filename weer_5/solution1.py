import socket, time



class ClientError(Exception):
    pass


class Client(object):

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def _connector(self, data):
        try:
            response = b''
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.sendall(data.encode())
                chunk = sock.recv(1024)
                try:
                    while chunk:
                        response += chunk
                        chunk = sock.recv(1024)
                except Exception as err:
                    if response:
                        pass
                    else:
                        raise ClientError(err)

            result, values = response.decode().split('\n', 1)
            if result == 'ok':
                return values.strip()
            else:
                raise ClientError(response.decode())
        except Exception as err:
            raise ClientError(err)

    def put(self, metric_name, metric_value, timestamp=None):
        timestamp = timestamp or int(time.time())
        send_str = 'put {0} {1} {2}\n'.format(metric_name, str(metric_value), str(timestamp))
        self._connector(send_str)

    def get(self, metric_name='*'):
        response_dict = {}
        send_str = 'get {0}\n'.format(metric_name)
        data = self._connector(send_str)
        if data:
            for row in data.split('\n'):
                key, value, timestamp = row.split()
                if key not in response_dict:
                    response_dict[key] = []
                response_dict[key].append((int(timestamp), float(value)))
                response_dict[key].sort(key=lambda x: x[0])
        return response_dict