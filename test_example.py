import socket

def query_server(query):
    HOST = '135.181.96.160'
    PORT = 44445

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(query.encode())
        data = s.recv(1024)
    return data.decode()

def main():
    while True:

        # query = "3;0;1;28;0;7;5;0;"
        query = input("Enter a search string (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        
        response = query_server(query)
        print("Server response:", response)

if __name__ == "__main__":
    main()