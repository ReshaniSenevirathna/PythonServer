import socket
import threading

directory = 'My_documents'
host , port= '' ,8000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

def start():
    try:
        server_socket.bind((host, port))
        print("Now you can find your page\n")
        relation()
    except OSError:
        print("USE")
        stop()

    
def relation():
    server_socket.listen(2)
    while True:
        (user, address) = server_socket.accept()
        
        threading.Thread(target=handle_user, args=(user,)).start()
        
    

def stop():
    try:
        my_socket.shutdown(socket.SHUT_RDWR)  

    except Exception:
        pass

 

def main_head(code, file):
    print("Selected File Type : " + file)

    main_head = ''
    if code == 404:
        main_head =main_head + 'HTTP/1.1 404 Not Found\n'
        print("Your file respond can be possible or not:" + main_head)
    elif code == 200:
        main_head =main_head + 'HTTP/1.1 200 OK\n'
        print("Your file respond can be possible or not:" + main_head)

    if file == 'png':
        main_head =main_head + 'Content-Type: image/png\n'
    elif file == 'jpg' or file == 'jpeg':
        main_head =main_head + 'Content-Type: image/jpeg\n'
    elif file == 'ico':
        main_head =main_head + 'Content-Type: image/x-icon\n'
        
    elif file == 'htm' or file == 'html':
        main_head =main_head + 'Content-Type: text/html\n'
    elif file == 'css':
        main_head =main_head + 'Content-Type: text/css\n'
    elif file == 'js':
        main_head=main_head + 'Content-Type:application/javascript\n'

    elif file == 'mp4':
        main_head=main_head + 'video/mp4\n'
    elif file == 'jpgv':
        main_head=main_head + 'Content-Type:video/jpeg\n'
        
    elif file == 'docx':
        main_head=main_head + 'Content-Type:application/vnd.openxmlformats-officedocument.wordprocessingml.document\n'
    elif file == 'pdf':
         main_head=main_head + 'Content-Type: application/pdf\n'
    main_head =main_head + 'Connection: close\n\n'
    print("Your file respond:" + main_head)
    return main_head


def handle_user(user):
    while True:
        

        try:
            message = user.recv(1024).decode()
            if not message:
                break
            print(message)
            request = message.split(' ')
            file=request[1]
            print("Your file request with id :" +file)

            

            file = file.split('?')
            page=file[0]
            print("Your file request :" +page)

            my = page.split('/')
            n_my=my[1]
            print("Your file :" +n_my)

            if page == "/":
                page = "/my.jpg"

            path = directory + page
            print( "Your file path:" +path)
            file_t = page.split('.')[1]

            f = open(path, 'rb')
            r_message = f.read()
            print("we got your message correctly")
            f.close()
            
            header = main_head(200, file_t)


            
        except FileNotFoundError:
            f = open('My_documents/error.html', 'rb')
            r_message = f.read()
            
            f.close()
            header = main_head(404, file_t)
            print("this is"+r_message)
            
        
        response = header.encode()
        

        response = response+ r_message
       
        user.send(response)
        user.close()
        print("This is the message user received:")
        print(header)
        break


start()
