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



server.bindAsync(
  "127.0.0.1:8082",grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    console.log("Server running at 127.0.0.1:8082");
    server.start();
    checkServer();
  }
);
