from pprint import pformat
from cgi import parse_qsl, escape

def application(environ, start_response):
	data = ['Hello world\n']
	
	d = parse_qsl(environ['QUERY_STRING'])
	if environ['REQUEST_METHOD'] == 'POST':
		data.append(pformat(environ['wsgi.input'].read()))
	if environ['REQUEST_METHOD'] == 'GET':
		if environ['QUERY_STRING'] != '':
			data.append('Get data\n')
			for ch in d:
				data.append(' = '.join(ch))
				data.append('\n')

	data_len = sum(len(line) for line in data)	
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(data_len))
	])
	return data
