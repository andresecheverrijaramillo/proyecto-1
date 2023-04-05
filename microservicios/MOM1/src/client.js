import dotenv from 'dotenv';
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';
import fs from 'fs';

dotenv.config()

const PROTO_PATH = process.env.PROTO_PATH;
const REMOTE_HOST = process.env.REMOTE_HOST;
const REMOTE_HOST2 = process.env.REMOTE_HOST2;
const MOM = process.env.MOM;
global.mainServer = false;

// definir atributos para la conexion con el servidor
const packageDefinition = protoLoader.loadSync(
  PROTO_PATH,
  {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  });

console.info("Consumer service is started...");
const proto = grpc.loadPackageDefinition(packageDefinition);
const server = new grpc.Server();

const replicationService = grpc.loadPackageDefinition(packageDefinition).ReplicationService;
const productService = grpc.loadPackageDefinition(packageDefinition).ProductService;
const inventoryService = grpc.loadPackageDefinition(packageDefinition).InventoryService;
// se crea la coexion con el servidor
const externalServer = new replicationService(MOM, grpc.credentials.createInsecure());
const client = new productService(REMOTE_HOST, grpc.credentials.createInsecure());
const client2 = new inventoryService(REMOTE_HOST2, grpc.credentials.createInsecure());

function checkServer() {
  externalServer.waitForReady(new Date().setTime(new Date().getTime() + 5000), (err) => {
    if (err) {
      console.log('El servidor externo 3 está caído.');
      // Si el servidor externo 3 está caído, continuar verificando
      global.mainServer=true;
      instrucciones();
      setTimeout(checkServer, 5000);
    } 
    else {
      console.log('El servidor externo 3 está prendido.');
      // Si el servidor externo 3 está prendido, continuar con la ejecución del servidor
      if(global.mainServer){
        //metodo de actualizar el otro mom
        instrucciones();
      }
      setTimeout(checkServer, 5000);
      }
    }
  );
}
//añadir un usario
function addUser(userName, userPassword) {
  fs.readFile('users.json', 'utf-8', (err, data) => {
    if (err) throw err;
    const json = JSON.parse(data);
    if (json.hasOwnProperty('user')) {
      // Verificar si ya existe un usuario con el mismo nombre
      const userExists = json.user.some(user => user.name === userName);
      if (userExists) {
        console.log(`User ${userName} already exists in ${'users.json'}`);
        return;
      }
      json.user.push({ name: userName, password: userPassword });
    } else {
      json['user'] = [{ name: userName, password: userPassword }];
    }
    const newJson = JSON.stringify(json);
    fs.writeFile('users.json', newJson, 'utf-8', (err) => {
      if (err) throw err;
      console.log(`User ${userName} added to ${'users.json'}`);
    });
  });
}
//encontrar un usuario
function findUser(userName, userPassword) {
  const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));
  const foundUser = users.user.find(user => user.name === userName && user.password === userPassword);
  return foundUser;
}
//añadir una peticion a la queue
function addToQueue(userName, method, variables) {
  const existingJSON = JSON.parse(fs.readFileSync('queues.json', 'utf-8'));
  const newJSON = { [userName]: [{ "method": method, "variables": variables }] }
  const combinedJSON = { ...existingJSON, ...newJSON };
  fs.writeFileSync('queues.json', JSON.stringify(combinedJSON));
}

//verificar si tiene algo en la cola
function hasData(obj, prop) {
  if (obj.hasOwnProperty(prop)) {
    if (Array.isArray(obj[prop])) {
      return obj[prop].length > 0;
    } else {
      return Object.keys(obj[prop]).length > 0;
    }
  } else {
    return false;
  }
}
//borrar usuario del json de queues
function deleteUserFromQueue(userToDelete) {
  const existingJSON = JSON.parse(fs.readFileSync('queues.json', 'utf-8'));
  delete existingJSON[userToDelete];
  fs.writeFileSync('queues.json', JSON.stringify(existingJSON));
}

//borrar request de un usuario
function deleteFirstFromUser(userName) {
  const existingJSON = JSON.parse(fs.readFileSync('queues.json', 'utf-8'));
  if (existingJSON.hasOwnProperty(userName)) {
    existingJSON[userName].shift();
    fs.writeFileSync('queues.json', JSON.stringify(existingJSON));
  }
}
//ejecucion de la instruccion en cola
function doSomethingForKey(user, key, value) {
  const method = value.method;
  const variables = value.variables;
  while(hasData(key)){
    key
    switch (method) {
      //getinventory
      case 2:{
        client2.GetInventory((err, data) => {
          if(err){
            callback(null,"0");
          } else {
            callback(null,data);
          }
        })
      }
      //addProducts to inventory
      case 3:{
        const userArray = variables[username];
        const userObj = userArray[0].variables; 
        const idProduct=userObj.id_product;
        const productName=userObj.name;
        client2.addProducts({id:idProduct,name:productName},(err, data) => {
          if(err){
            callback(null,"0");
          } else {
            callback(null,data);
          }
        })
      }
      //GetInventoryLastIdd
      case 4:{
        client2.GetInventoryLastIdd((err, data) => {
          if(err){
            callback(null,"0");
          } else {
            callback(null,data);
          }
        })
      }
      //AddProduct to car
      case 5:{
        const userArray = variables[username];
        const userObj = userArray[0].variables; 
        const idProduct=userObj.id_product;
        const productName=userObj.name;
        client.AddProduct({id:idProduct,name:productName,userName:username},(err, data) => {
          if(err){
            callback(null,"0");
          } else {
            callback(null,data);
          }
        })
      }
      //DeleteProduct from car
      case 6:{
        const userArray = variables[username];
        const userObj = userArray[0].variables; 
        const idProduct=userObj.id_product;
        const productName=userObj.name;
        client.DeleteProduct({id:idProduct,name:productName,userName:username},(err, data) => {
          if(err){
            callback(null,"0");
          } else {
            callback(null,data);
          }
        })}
    }
  }
  
}

//verificar si hay instrucciones
function instrucciones(){
  const existingJSON = JSON.parse(fs.readFileSync('queues.json', 'utf-8'));
  for (const user in existingJSON) {
    if (user !== "userName2") {
      const values = existingJSON[user];
      for (const user in existingJSON) {
        if (user !== "userName2") {
          const values = existingJSON[user];
          for (let i = 0; i < values.length;) {
            const { method, variables } = values[i];
            doSomethingForKey(user, i.toString(), method, variables);
            deleteFirstFromUser(user)
          }
        }
      }
    }
  }
}

  //cifrar
  function cifradoCesar(texto, desplazamiento) {
    let resultado = "";
    for (let i = 0; i < texto.length; i++) {
      let caracter = texto[i];
      if (caracter.match(/[a-z]/i)) {
        let codigoAscii = texto.charCodeAt(i);
        if (codigoAscii >= 65 && codigoAscii <= 90) {
          caracter = String.fromCharCode(((codigoAscii - 65 + desplazamiento) % 26) + 65);
        } else if (codigoAscii >= 97 && codigoAscii <= 122) {
          caracter = String.fromCharCode(((codigoAscii - 97 + desplazamiento) % 26) + 97);
        }
      }
      resultado += caracter;
    }
    return resultado;
  }

//Servicios
server.addService(proto.ReplicationService.service, {
  Requests: (call, callback) => {
    const method = call.request.method; 
    const password = call.request.password; 
    const user = call.request.user; 
    const variablesString = call.request.variables;
    const variables = JSON.parse(variablesString);
    if(method!=1){
    if(findUser(user,password)){
      addToQueue(user,method,variables);
      callback(null,"1");
      }
    else{
      callback(null,"0");
      }
    }
    else{
      addUser(user,password);
    }
  },
  }
)

server.bindAsync(
  "127.0.0.1:8080", grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    console.log("Server running at 127.0.0.1:8080");
    server.start();
    checkServer();
  }
);