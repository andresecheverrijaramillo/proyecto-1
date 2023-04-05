import dotenv from 'dotenv';
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';
import fs from 'fs';
dotenv.config()
const PROTO_PATH = process.env.PROTO_PATH;
const REMOTE_HOST = process.env.REMOTE_HOST;
const REMOTE_HOST2 = process.env.REMOTE_HOST2;
const MOM = process.env.MOM;

// definir atributos para la conexion con el servidor
const packageDefinition = protoLoader.loadSync(
  PROTO_PATH,
  {keepCase: true,
   longs: String,
   enums: String,
   defaults: true,
   oneofs: true
  });
// se crea el constructor para crear conexiones con el servidor

const replicationService = grpc.loadPackageDefinition(packageDefinition).ReplicationService;
const productService = grpc.loadPackageDefinition(packageDefinition).ProductService;
const inventoryService = grpc.loadPackageDefinition(packageDefinition).InventoryService;
const proto = grpc.loadPackageDefinition(packageDefinition);
const server = new grpc.Server();
// se crea la coexion con el servidor
const externalServer = new replicationService(MOM,grpc.credentials.createInsecure());

function checkServer() {
  externalServer.waitForReady(new Date().setTime(new Date().getTime() + 5000), (err) => {
    if (err) {
      console.log('El servidor externo 3 está caído.');
      // Si el servidor externo 3 está caído, continuar verificando
      setTimeout(checkServer, 10000);
    } else {
      console.log('El servidor externo 3 está prendido.');
      // Si el servidor externo 3 está prendido, continuar con la ejecución del servidor
      setTimeout(checkServer, 10000);
    }
  });
}

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

function findUser(userName, userPassword) {
  const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));  
  const foundUser = users.user.find(user => user.name === userName && user.password === userPassword);
return foundUser;}

function addToQueue(userName, method, variables){
  const existingJSON = JSON.parse(fs.readFileSync('queues.json', 'utf-8'));
  const newJSON = {[userName]: [{"method": method,"variables": variables}]}
  const combinedJSON = {...existingJSON, ...newJSON};
  fs.writeFileSync('queues.json', JSON.stringify(combinedJSON));
}

server.addService(proto.QueueService.service,{
  add: (call, callback) => {
    const method = call.request.method; 
    const password = call.request.password; 
    const user = call.request.user; 
    const variables = call.request.variables;
    if(findUser(user,password)){
      switch (method) {
        case 1:{
          addUser(user,password);
        }
        case 2:{
          client2.GetInventory((err, data) => {
            if(err){
              callback(null,"0");
            } else {
              callback(null,data);
            }
           })
        }
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
        case 4:{
          client2.GetInventoryLastIdd((err, data) => {
            if(err){
              callback(null,"0");
            } else {
              callback(null,data);
            }
           })
        }
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
    else{
      callback(null,"0");
    }
  },
})

server.bindAsync(
  "127.0.0.1:8082",grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    console.log("Server running at 127.0.0.1:8082");
    server.start();
    checkServer();
  }
);
