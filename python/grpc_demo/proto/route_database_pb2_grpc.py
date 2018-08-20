# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import route_database_pb2 as route__database__pb2


class RouteGreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeature = channel.unary_unary(
        '/route_database.RouteGreeter/GetFeature',
        request_serializer=route__database__pb2.FeatureRequest.SerializeToString,
        response_deserializer=route__database__pb2.FeatureReply.FromString,
        )
    self.ListFeatures = channel.unary_unary(
        '/route_database.RouteGreeter/ListFeatures',
        request_serializer=route__database__pb2.PointRequest.SerializeToString,
        response_deserializer=route__database__pb2.PointReply.FromString,
        )
    self.RecordRoute = channel.unary_unary(
        '/route_database.RouteGreeter/RecordRoute',
        request_serializer=route__database__pb2.PointRequest.SerializeToString,
        response_deserializer=route__database__pb2.PointReply.FromString,
        )
    self.RouteChat = channel.unary_unary(
        '/route_database.RouteGreeter/RouteChat',
        request_serializer=route__database__pb2.PointRequest.SerializeToString,
        response_deserializer=route__database__pb2.PointReply.FromString,
        )


class RouteGreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetFeature(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFeatures(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecordRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RouteChat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RouteGreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeature': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeature,
          request_deserializer=route__database__pb2.FeatureRequest.FromString,
          response_serializer=route__database__pb2.FeatureReply.SerializeToString,
      ),
      'ListFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.ListFeatures,
          request_deserializer=route__database__pb2.PointRequest.FromString,
          response_serializer=route__database__pb2.PointReply.SerializeToString,
      ),
      'RecordRoute': grpc.unary_unary_rpc_method_handler(
          servicer.RecordRoute,
          request_deserializer=route__database__pb2.PointRequest.FromString,
          response_serializer=route__database__pb2.PointReply.SerializeToString,
      ),
      'RouteChat': grpc.unary_unary_rpc_method_handler(
          servicer.RouteChat,
          request_deserializer=route__database__pb2.PointRequest.FromString,
          response_serializer=route__database__pb2.PointReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'route_database.RouteGreeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))