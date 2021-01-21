from application import utils

def parse_request(request_data):
    loc = request_data.find("\r\n")
    request_line = request_data[:loc]
    request_line_list = request_line.split(" ")
    file_path = request_line_list[1]
    print("用户连接成功，正在请求【%s】" % "/myblog" + file_path)
    if file_path == "/":
        file_path = "/index.html"
    return file_path

def application(current_dir,request_data):
    # # 1.响应行
    # response_line = "HTTP/1.1 200 OK\r\n"
    # # 2.响应头
    # response_handler = "Server: PythonKK/3.9\r\n"
    # # 3.响应空行
    # response_blanks = "\r\n"

    file_path = parse_request(request_data)
     # 4.响应主体
     # (2)改进
    try:
        # with open("myblog/index.html" , "rb") as file:
        with open(current_dir + file_path, "rb") as file:
            response_body = file.read()
            response_line = "HTTP/1.1 200 OK\r\n"
            #调用utils获取返回报文
            response_data = utils.creat_http_response(response_line,response_body)
    except Exception as result:
        response_line = "HTTP/1.1 404 Not Found"
        response_body = str(result).encode()
        response_data = utils.creat_http_response(response_line,response_body)
    # 5.拼接
    # response_data = (response_line + response_handler + response_blanks).encode() + response_body

    return response_data