def retrieve_charset(content_type):


    charset=None
    if content_type.find(';')>0:    #index()如果没有查找到则会抛出valueError异常     find（）如果没有则返回-1
        content_type,charset=tuple(content_type.split(';'))
        charset=charset.split('=')[-1]
    return content_type,charset


def decode_html(bytes,content_type):
    ctype,charset=retrieve_charset(content_type)
    if charset:
        return bytes.decode(charset)
    return bytes.decode()