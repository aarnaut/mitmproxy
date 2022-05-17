"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx
import mitmproxy
from mitmproxy.utils.protoc import ProtocSerializer

class Counter:

    def __init__(self):
        self.num = 0
        self.serializer = ProtocSerializer()
        self.serializer.set_descriptor("../../descriptor.proto")

    def response(self, flow):
        if "GetComments" in flow.request.path:
            ctx.log.info("GetComments response")
            with open('../../getcomments_response.txt', 'r') as file:
                data = file.read()
                serialized = self.serializer.serialize(flow.response, flow.request.path, data)
                flow.response.content = serialized 

addons = [
    Counter()
]
