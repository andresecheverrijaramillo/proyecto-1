# **Proyecto 1**
**Curso:** Tópicos Especiales en Telemática <br>
**Título:** Diseño e Implementación de un Middleware que Implemente un Servicio de Mensajería <br>
**Estudiante** Andrés Echeverri Jaramillo, Salomón Vélez Pérez, Jose Manuel Fonseca<br>
### **1. Descripción**
En este laboratorio se desarrollaron 2 microservicios los cuales ambos están hecho en el lenguaje de programación Python: el servicio de pagos (Payment) y el servicio de inventario (Inventory), ademas de los 2 MOM, los cuales fueron implementados usando Nodejs

### **3. Diseño**
Ver el .jpg adjunto en el github con el nombre de "Arquitectura.jpg" <br />

### **4. Requerimientos**
Para este prpyecto se necesita el compilador para archivos .NET, así como tener postman y protobuff instalados..<br />

### **5. Análisis**
 El proyecto está diseñado para poder comunicar los servicios entre ellos a traves de 1 de los MOM, para esto, se usa una comunicación grpc que usa los archivos .proto de los servicios. Desde el MOM, se pide a los microservicios una información, o se solicita que se haga un proceso, y estos responden a estas peticiones usando los métodos y clases implementados. Las peticiones se mandan con cierta información, que es el nombre de usuario, el nombre del producto y una constraseña, tanto el nombre del producto como el nombre del usuario se cifran usado el método de cifrado "Cesar", esto por cuestiones de seguridad, y una vez esta información es recibida por los microservicios, es desencriptada. <br />

### **6. Guía de uso (En local)**
Para implementar el trabajo primero se tendra que acceder a los archivos de este, por lo tanto se duplicara el repositorio donde estan con el comando "git clone https://github.com/andresecheverrijaramillo/microservicios.git", ya cuando se tengan los archivos clonados se procedera a abrir tres terminales diferentes, una por cada servicio, y se ejecutaran los archivos server.py o server.js dependiendo del servicio, cabe aclarar que se necesitara tener python con las librerias grpcio y grpcio-tools, y Node.js v19.X para que se puedan ejecutar. Si no se tienen instalados se correran los siguientes comandos. <br />
Python: <br />
$ sudo apt-get update <br />
$ sudo apt-get upgrade <br />
$ sudo apt-get install python3 <br />
$ sudo apt-get install python3-pip <br />
$ sudo python3 -m pip install grpcio <br />
$ sudo python3 -m pip install grpcio-tools <br />
Node:
$ sudo apt-get update <br />
$ sudo apt-get upgrade <br />
$ sudo curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - && sudo apt-get install -y nodejs <br />
Con esto se asegura que se puedan ejecutar, entonces en el momento que se ejecuten en las diferetes terminales cada una quedara como un servidor, los servidores tienen puertos asociados, el servidor de payment tiene el puerto 8080, el de inventory 8081 y el de Delivery el 8082. teniendo eso encuenta se abre postman para verficar que si funcionen, le decimos que vamos a probar una conección gRPC, en este caso que lo estamos ejecutando los tres server en una misma maquina la coneccion que vamos a probar o en otras palabras el url seria "localhost:####" en el numeral se pondria el puerto del servidor. Para que Postman sepa cuales son los metodos se importara el .proto respectivo como la API y ya se podran hacer las invocaciones de los diferentes metodos que tenga el .proto, en dicho caso de que no se entreguen los parametros que se necesiten o se entreguen mal, la peticion se mandara pero no se hara nada en la terminal del servidor se podra ver mejor esto, en el caso de que se mande se ejecutara sin problema y dara la respuesta que es.
