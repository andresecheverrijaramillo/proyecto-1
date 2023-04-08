from concurrent import futures
import json
import grpc
import Service_pb2
import Service_pb2_grpc

HOST = '[::]:8083'

class InventoryService(Service_pb2_grpc.InventoryServiceServicer):
    
    def GetInventory(self, request, context):
        print("Request is received: ")
        with open("inventory.json","r") as productList:
            print("inventory: ")
            inventory = json.loads(productList.read())
        print(str(inventory["products"]))
        #my_string = str(json.dumps(inventory["products"]))
        #print(my_string)
        print(type(str(inventory["products"])))
        return Service_pb2.Inventory(Inv=str(inventory["products"]))
    
    def addProducts(self, request, context):
        productID = str(request.id)
        productName = str(request.name)
        replicate=False
        producto={"id":productID,"name": productName}
        productName = descifrado_cesar(productName, 3)
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
            inventory['products'].append(producto)
            print(inventory)
            with open('inventory.json', 'w') as f:
                json.dump(inventory, f)
            return Service_pb2.TransactionResponse(status_code=1)
    
    def GetLastIdd(self, request, context):
        print("Request is received: " + str(request))
        with open("inventory.json","r") as productList:
            inventory = json.loads(productList.read())
        x = len(inventory['products'])+1
        x=str(x)
        print(x)
        print(type(x))
        return Service_pb2.LastIdd(LIdd=x)
    
def descifrado_cesar(texto_cifrado, desplazamiento):
    resultado = ""
    for caracter in texto_cifrado:
        if caracter.isalpha():
            codigo_ascii = ord(caracter)
            if codigo_ascii >= 65 and codigo_ascii <= 90:
                # Letra mayúscula
                resultado += chr((codigo_ascii - desplazamiento - 65) % 26 + 65)
            elif codigo_ascii >= 97 and codigo_ascii <= 122:
                # Letra minúscula
                resultado += chr((codigo_ascii - desplazamiento - 97) % 26 + 97)
        else:
            resultado += caracter
    return resultado


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    print(HOST)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()