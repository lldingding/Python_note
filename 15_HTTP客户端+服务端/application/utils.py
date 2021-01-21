def creat_http_response(response_line,response_body):
# 1.响应行
#     response_line = "HTTP/1.1 200 OK\r\n"
    # 2.响应头
    response_handler = "Server: PythonKK/3.9\r\n"
    # 3.响应空行
    response_blanks = "\r\n"
    #拼接
    response_data = (response_line + response_handler + response_blanks).encode() + response_body
    return  response_data