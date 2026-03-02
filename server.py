import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

print("Iniciando el servidor del regalo...")
print(f"👉 Abre tu navegador y ve a la siguiente dirección: http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor apagado.")