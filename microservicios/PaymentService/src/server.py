from concurrent import futures
import json
import grpc
import Service_pb2
import Service_pb2_grpc

HOST = '[::]:8082'

class ProductService(Service_pb2_grpc.ProductServiceServicer):
   
    def AddProduct(self, request, context):
        print("Request is received: " + str(request))
        productID = str(request.id_product)
        productName = str(request.name)
        userName = str(request.userName)
        productName = descifrado_cesar(productName, 3)
        userName = descifrado_cesar(userName, 3)
        print(productID,productName,userName)
        product={"id":productID,"name": productName}
        print("\nRequest received. Handling product "+productID+" with name "+productName)
        with open("car.json","r") as productList:
            car = json.loads(productList.read())
        print(car)
        print('hola')
        if userName in car:
            id_list = []
            for item in car[userName]:
                if "id" in item:
                    id_list.append(item["id"])
            if productID in id_list:
                print("\n Product with that id already added to the car")
                return Service_pb2.TransactionResponse(status_code=0)
            else:
                print("\nRequest received. Product ID: "+productID+" does not exist in this car. It will be added")
                print(car[userName])
                print(product)
                print('hola')
                if isinstance(car[userName], list):
                    car[userName].append(product)
                else:
                    car[userName] = [car[userName], product]
                print(car[userName])
                with open('car.json', 'w') as f:
                    json.dump(car, f)
                return Service_pb2.TransactionResponse(status_code=1)
        else:
            car[userName]=product
            with open('car.json', 'w') as f:
                    json.dump(car, f)
            return Service_pb2.TransactionResponse(status_code=1)
    
        
    def DeleteProduct(self, request, context):
        print("Request is received: " + str(request))
        productID = str(request.id_product)
        productName = str(request.name)
        userName = str(request.userName)
        productName = descifrado_cesar(productName, 3)
        userName = descifrado_cesar(userName, 3)
        replicate=False
        print("\nRequest received. Handling product "+productID+" with name "+productName)
        with open("car.json","r") as productList:
            car = json.loads(productList.read())
        if isinstance(car[userName], list):
            indexToDelete = None
            for i, item in enumerate(car[userName]):
                if item["id"] == productID:
                    indexToDelete = i
                    break
            if indexToDelete is not None:
                del car[userName][indexToDelete]
                replicate=True
        else:
            if car[userName]["id"] == productID:
                del car[userName]
                replicate=True
        if replicate:
            print("\n Product "+ productName +" eliminated from the user "+ userName +" car")
            with open('car.json', 'w') as f:
                    json.dump(car, f)
            return Service_pb2.TransactionResponse(status_code=0)
        else:
            print("\n Product "+ productName +" doesn't exist in the user "+ userName +" car")
            return Service_pb2.TransactionResponse(status_code=2)
        
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
    Service_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    print(HOST)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()