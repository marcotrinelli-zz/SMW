import time
import sys
import SimpleHTTPServer
import SocketServer
from urlparse import urlparse
import urllib
import io
import json
from snips_nlu import load_resources, SnipsNLUEngine

NLU_engine = None

def sendToHost(s, result):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write(result)
 
class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):    
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        
    def do_GET(s):
        global NLU_engine
        ''' Parse the query, send to NLU to receive the JSON answer, and send it to the user '''
        query = urlparse(s.path).query
        print "Query: " + query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        user_query = query_components["text"]
        user_query = urllib.unquote(user_query).decode('utf8')
        #Send query to NLU
        parsing = NLU_engine.parse(u"%s" % user_query)
        result = json.dumps(parsing, indent=2)
        print(result)
        sendToHost(s, result)
                
if __name__ == '__main__':
    global NLU_engine
    
    if len(sys.args) < 1:
        print "Syntax: %s <trained_assistant_path> [<port>]" % sys.argv[0]
        sys.exit(1)
        
    DATASET_PATH = sys.argv[1]
	
    PORT = sys.argv[2] if len(sys.argv) == 2 else 80
    if not isdigit(PORT) or PORT > 65535:
        print "Error. Provide a valid port number"
        sys.exit(1)
        
    with io.open(DATASET_PATH) as ds:
        dataset_dict = json.load(ds)
         
    load_resources(u"en")
    NLU_engine = SnipsNLUEngine.from_dict(dataset_dict)
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print time.asctime(), "Server Starts - port:%s" % (PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - port:%s" % (PORT)
