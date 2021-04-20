요구사항
- 파이썬 3.5 이상
- pip 9.0 이상

프로젝트 설정
```
pip update
    python -m pip install --upgrade pip

grpc
    python -m pip install grpcio
    
grpc tools
    python -m pip install grpcio-tools 
```

proto build
```
    python -m grpc_tools.protoc \ 
            -I./proto \               // proto folder
            --python_out=. \          // service stub 
            --grpc_python_out=. \     // message stub
             ./proto/grpc.proto       // proto file
```