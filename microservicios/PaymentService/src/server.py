from concurrent import futures
import json
import grpc
import Service_pb2
import Service_pb2_grpc

HOST = '[::]:8082'

class ProductService(Service_pb2_grpc.ProductServiceServicer):
   
    def AddProduct(self, request, context):
        print("Request is received: " + str(request))
        productID = str(request.id)
        productName = str(request.name)
        userName = str(request.userName)
        product={{"id":productID,"name": productName}}
        print("\nRequest received. Handling product "+productID+" with name "+productName)
        with open("car.json","r") as productList:
            car = json.loads(productList.read())
        if productID in car[userName].keys():
            print("\n Product with that id already added to the car")
            return Service_pb2.TransactionResponse(status_code=0)
        else:
            print("\nRequest received. Product ID: "+productID+" does not exist in this car. It will be added")
            car[userName].append(product)
            with open('car.json', 'w') as f:
                json.dump(car, f)
            return Service_pb2.TransactionResponse(status_code=1)
    
        
    def DeleteProduct(self, request, context):
        print("Request is received: " + str(request))
        productID = str(request.id)
        productName = str(request.name)
        userName = str(request.userName)
        replicate=False
        print("\nRequest received. Handling product "+productID+" with name "+productName)
        with open("car.json","r") as productList:
            car = json.loads(productList.read())
        for carProduct in car[userName]:
            if carProduct["id"] == productID:
                replicate=True
                car[userName].remove(carProduct)
        if replicate:
            print("\n Product "+ productName +" eliminated from the user "+ userName +" car")
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