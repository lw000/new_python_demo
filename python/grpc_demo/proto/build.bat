python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./chat.proto
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./route_database.proto
                                                  