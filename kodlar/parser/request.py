

class RequestHeader:
    def __init__(self, header_str):
        assert header_str != ''
        self.header_str = header_str
        method = ''
        path = ''
        protocol = ''
        http_methods = ['GET', 'POST', 'PUT', 'PATCH',
                        'TRACE', 'HEAD', 'DELETE',
                        'CONNECT', 'OPTIONS']
        header_fields = ['A-IM','Accept','Accept-Charset','Accept-Datetime',
                         'Accept-Encoding','Accept-Language','Access-Control-Request-Method',
                         'Access-Control-Request-Headers','Authorization','Cache-Control',
                         'Connection','Content-Length','Content-MD5','Content-Type','Cookie',
                         'Date','Expect','Forwarded','From','Host','HTTP2-Settings','If-Match',
                         'If-Modified-Since','If-None-Match','If-Range','If-Unmodified-Since',
                         'Max-Forwards','Origin','Pragma','Proxy-Authorization','Range','Referer',
                         'TE','User-Agent','Upgrade','Via']

        header_dict = {}

    # header lari bulan metod
    def get_headers(self):
        pass

    def check_header(self, line):
        pass

    #TODO: ilk header 1'nci satırda ikinci alan path'de hostname olmamalı
    def check_header_path(selfs):
        pass

    #TODO: header parse
    def parse(self):
        first_line = self.header_str[0]
        first_line_lst = first_line.split(' ')
        # istek GET / HTTP/1.1 tarzında değilse NULL
        if len(first_line_lst) != 3:
            raise Exception

    def is_httpd_method(self):




class Request:
    def __init__(self, raw_str):
        header_str = ''
        body_str = ''

    # str_req string i satır satır okuyan reqest objesi yaratır
    def to_request(self, str_req):
        pass

    # raw str nin header ını ayıracak
    def get_header(self):
        pass

    # raw str nin body sini ayıracak
    # metoda gore optional
    # TRACE can not have body
    # POST, PUT, PATCH must have body
    # GET, HEAD, DELETE, CONNECT, OPTIONS optional
    def get_body(self):
        pass




