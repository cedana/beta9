# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: queue.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
import grpclib


@dataclass
class SimpleQueuePutRequest(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class SimpleQueuePutResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


@dataclass
class SimpleQueuePopRequest(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class SimpleQueuePopResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class SimpleQueuePeekResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    value: bytes = betterproto.bytes_field(2)


@dataclass
class SimpleQueueEmptyResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    empty: bool = betterproto.bool_field(2)


@dataclass
class SimpleQueueSizeResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    size: int = betterproto.uint64_field(2)


@dataclass
class SimpleQueueRequest(betterproto.Message):
    name: str = betterproto.string_field(1)


class SimpleQueueServiceStub(betterproto.ServiceStub):
    async def put(
        self, *, name: str = "", value: bytes = b""
    ) -> SimpleQueuePutResponse:
        request = SimpleQueuePutRequest()
        request.name = name
        request.value = value

        return await self._unary_unary(
            "/simplequeue.SimpleQueueService/Put",
            request,
            SimpleQueuePutResponse,
        )

    async def pop(
        self, *, name: str = "", value: bytes = b""
    ) -> SimpleQueuePopResponse:
        request = SimpleQueuePopRequest()
        request.name = name
        request.value = value

        return await self._unary_unary(
            "/simplequeue.SimpleQueueService/Pop",
            request,
            SimpleQueuePopResponse,
        )

    async def peek(self, *, name: str = "") -> SimpleQueuePeekResponse:
        request = SimpleQueueRequest()
        request.name = name

        return await self._unary_unary(
            "/simplequeue.SimpleQueueService/Peek",
            request,
            SimpleQueuePeekResponse,
        )

    async def empty(self, *, name: str = "") -> SimpleQueueEmptyResponse:
        request = SimpleQueueRequest()
        request.name = name

        return await self._unary_unary(
            "/simplequeue.SimpleQueueService/Empty",
            request,
            SimpleQueueEmptyResponse,
        )

    async def size(self, *, name: str = "") -> SimpleQueueSizeResponse:
        request = SimpleQueueRequest()
        request.name = name

        return await self._unary_unary(
            "/simplequeue.SimpleQueueService/Size",
            request,
            SimpleQueueSizeResponse,
        )