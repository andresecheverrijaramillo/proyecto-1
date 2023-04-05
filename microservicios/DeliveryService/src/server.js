const grpc = require("@grpc/grpc-js");
const PROTO_PATH = "../protobufs/Service.proto";
var protoLoader = require("@grpc/proto-loader");
const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
  };
var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);
const proto = grpc.loadPackageDefinition(packageDefinition);
const server = new grpc.Server();

let delivery = {delivery:"On Going"}

server.addService(proto.DeliveryService.service, {
    GetDelivery: (_, callback) => {
      callback(null, delivery);
    },
  });

server.bindAsync(
    "127.0.0.1:8082",
    grpc.ServerCredentials.createInsecure(),
    (error, port) => {
      console.log("Server running at 127.0.0.1:8082");
      server.start();
    }
  );
