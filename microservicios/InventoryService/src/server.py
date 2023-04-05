from concurrent import futures
import json
import grpc
import Service_pb2
import Service_pb2_grpc

HOST = '[::]:8081'

class InventoryService(Service_pb2_grpc.InventoryServiceServicer):
    
    def GetInventory(self, request, context):
        print("Request is received: " + str(request))
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())
        return Service_pb2.Inventory(inventory)
    
    def addProducts(self, request, context):
        productID = str(request.id)
        productName = str(request.name)
        replicate=False
        product={{"id":productID,"name": productName}}
        print("\nRequest received. Handling product "+productID+" with name "+productName)
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())
        for product in inventory["products"]:
            if product["id"] == productID:
                replicate=True
        if replicate:
            print("\n Product with that id already added to the Inventory")
            return Service_pb2.TransactionResponse(status_code=0)
        else:
            print("\nRequest received. Product ID: "+productID+" does not exist in this inventory. It will be added")
            inventory['products'].append(product)
            with open('inventory.json', 'w') as f:
                json.dump(inventory, f)
            return Service_pb2.TransactionResponse(status_code=1)
    
    def GetInventoryLastIdd(self, request, context):
        print("Request is received: " + str(request))
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())
        x = len(inventory['products'])+1
        return Service_pb2.Inventory(x)
    
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()