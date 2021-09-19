import asyncio


class ClientServerProtocol(asyncio.Protocol):

    local_storage = dict()

    def connection_made(self, transport):
        self.transport = transport
        # print(self.transport.get_extra_info(name='peername'))

    def _get_data(self, data):
        response = 'ok\n'
        input_key = data[0]
        if input_key == '*':
            for key, values in self.local_storage.items():
                for i in values:
                    response += ' '.join([key, str(i[1]), str(i[0])+'\n'])
        else:
            if input_key in self.local_storage.keys():
                for i in self.local_storage[input_key]:
                    response += ' '.join([input_key, str(i[1]), str(i[0])+'\n'])

        # print(ascii('{0}\n'.format(response)))
        return '{0}\n'.format(response)

    # def _put_data(self, data):
    #     input_key = data[0]
    #     if input_key not in self.local_storage:
    #         self.local_storage[input_key] = []
    #     tup_values = (int(data[2]), float(data[1]))
    #     if tup_values not in self.local_storage[input_key]:             #worked data
    #         self.local_storage[input_key].append(tup_values)
    #         self.local_storage[input_key].sort(key=lambda x: x[0])
    #
    #     return 'ok\n\n'

    def _put_data(self, data):
        input_key = data[0]
        if input_key not in self.local_storage.keys():
            self.local_storage[input_key] = []
        tup_values = (int(data[2]), float(data[1]))

        if input_key in self.local_storage.keys():
            if tup_values[0] in [i for i, j in self.local_storage[input_key]]:
                for idx, data in enumerate(self.local_storage[input_key]):
                    if tup_values[0] == data[0]:
                        self.local_storage[input_key][idx] = tup_values
                        self.local_storage[input_key].sort(key=lambda x: x[0])
            else:
                self.local_storage[input_key].append(tup_values)
                self.local_storage[input_key].sort(key=lambda x: x[0])
        return 'ok\n\n'






    def _process_data(self, data):
        # data_list = data.strip('\r\n').split()
        # method = data_list[0]
        # if method == 'get':
        #     response = self._get_data(data_list[1:])
        # elif method == 'put':
        #     response = self._put_data(data_list[1:])
        # else:
        #     response = 'error\nwrong command\n\n'
        # return response
        response = None
        try:
            data_list = data.strip('\r\n').split()
            # print(data_list)
            method = data_list[0]
            if method == 'get' and len(data_list[1:]) == 1:
                response = self._get_data(data_list[1:])
            elif method == 'put' and len(data_list[1:]) == 3:
                response = self._put_data(data_list[1:])
        except Exception:
            # print("tralala")
            response = 'error\nwrong command\n\n'
        if not isinstance(response, str):
            response = 'error\nwrong command\n\n'
        return response




    def data_received(self, data):
        resp = self._process_data(data.decode())
        # print(resp)
        self.transport.write(resp.encode())


def run_server(host='127.0.0.1', port=8888):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server("127.0.0.1", 8888)