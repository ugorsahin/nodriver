# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Tracing

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import io
from .util import T_JSON_DICT, event_class


class MemoryDumpConfig(dict):
    """
    Configuration for memory dump. Used only when "memory-infra" category is enabled.
    """

    def to_json(self) -> dict:
        return self

    @classmethod
    def from_json(cls, json: dict) -> MemoryDumpConfig:
        return cls(json)

    def __repr__(self):
        return "MemoryDumpConfig({})".format(super().__repr__())


@dataclass
class TraceConfig:
    #: Controls how the trace buffer stores data.
    record_mode: typing.Optional[str] = None

    #: Size of the trace buffer in kilobytes. If not specified or zero is passed, a default value
    #: of 200 MB would be used.
    trace_buffer_size_in_kb: typing.Optional[float] = None

    #: Turns on JavaScript stack sampling.
    enable_sampling: typing.Optional[bool] = None

    #: Turns on system tracing.
    enable_systrace: typing.Optional[bool] = None

    #: Turns on argument filter.
    enable_argument_filter: typing.Optional[bool] = None

    #: Included category filters.
    included_categories: typing.Optional[typing.List[str]] = None

    #: Excluded category filters.
    excluded_categories: typing.Optional[typing.List[str]] = None

    #: Configuration to synthesize the delays in tracing.
    synthetic_delays: typing.Optional[typing.List[str]] = None

    #: Configuration for memory dump triggers. Used only when "memory-infra" category is enabled.
    memory_dump_config: typing.Optional[MemoryDumpConfig] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        if self.record_mode is not None:
            json["recordMode"] = self.record_mode
        if self.trace_buffer_size_in_kb is not None:
            json["traceBufferSizeInKb"] = self.trace_buffer_size_in_kb
        if self.enable_sampling is not None:
            json["enableSampling"] = self.enable_sampling
        if self.enable_systrace is not None:
            json["enableSystrace"] = self.enable_systrace
        if self.enable_argument_filter is not None:
            json["enableArgumentFilter"] = self.enable_argument_filter
        if self.included_categories is not None:
            json["includedCategories"] = [i for i in self.included_categories]
        if self.excluded_categories is not None:
            json["excludedCategories"] = [i for i in self.excluded_categories]
        if self.synthetic_delays is not None:
            json["syntheticDelays"] = [i for i in self.synthetic_delays]
        if self.memory_dump_config is not None:
            json["memoryDumpConfig"] = self.memory_dump_config.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> TraceConfig:
        return cls(
            record_mode=(
                str(json["recordMode"])
                if json.get("recordMode", None) is not None
                else None
            ),
            trace_buffer_size_in_kb=(
                float(json["traceBufferSizeInKb"])
                if json.get("traceBufferSizeInKb", None) is not None
                else None
            ),
            enable_sampling=(
                bool(json["enableSampling"])
                if json.get("enableSampling", None) is not None
                else None
            ),
            enable_systrace=(
                bool(json["enableSystrace"])
                if json.get("enableSystrace", None) is not None
                else None
            ),
            enable_argument_filter=(
                bool(json["enableArgumentFilter"])
                if json.get("enableArgumentFilter", None) is not None
                else None
            ),
            included_categories=(
                [str(i) for i in json["includedCategories"]]
                if json.get("includedCategories", None) is not None
                else None
            ),
            excluded_categories=(
                [str(i) for i in json["excludedCategories"]]
                if json.get("excludedCategories", None) is not None
                else None
            ),
            synthetic_delays=(
                [str(i) for i in json["syntheticDelays"]]
                if json.get("syntheticDelays", None) is not None
                else None
            ),
            memory_dump_config=(
                MemoryDumpConfig.from_json(json["memoryDumpConfig"])
                if json.get("memoryDumpConfig", None) is not None
                else None
            ),
        )


class StreamFormat(enum.Enum):
    """
    Data format of a trace. Can be either the legacy JSON format or the
    protocol buffer format. Note that the JSON format will be deprecated soon.
    """

    JSON = "json"
    PROTO = "proto"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> StreamFormat:
        return cls(json)


class StreamCompression(enum.Enum):
    """
    Compression type to use for traces returned via streams.
    """

    NONE = "none"
    GZIP = "gzip"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> StreamCompression:
        return cls(json)


class MemoryDumpLevelOfDetail(enum.Enum):
    """
    Details exposed when memory request explicitly declared.
    Keep consistent with memory_dump_request_args.h and
    memory_instrumentation.mojom
    """

    BACKGROUND = "background"
    LIGHT = "light"
    DETAILED = "detailed"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> MemoryDumpLevelOfDetail:
        return cls(json)


class TracingBackend(enum.Enum):
    """
    Backend type to use for tracing. ``chrome`` uses the Chrome-integrated
    tracing service and is supported on all platforms. ``system`` is only
    supported on Chrome OS and uses the Perfetto system tracing service.
    ``auto`` chooses ``system`` when the perfettoConfig provided to Tracing.start
    specifies at least one non-Chrome data source; otherwise uses ``chrome``.
    """

    AUTO = "auto"
    CHROME = "chrome"
    SYSTEM = "system"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> TracingBackend:
        return cls(json)


def end() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Stop trace events collection.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Tracing.end",
    }
    json = yield cmd_dict


def get_categories() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[str]]:
    """
    Gets supported tracing categories.

    **EXPERIMENTAL**

    :returns: A list of supported tracing categories.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Tracing.getCategories",
    }
    json = yield cmd_dict
    return [str(i) for i in json["categories"]]


def record_clock_sync_marker(
    sync_id: str,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Record a clock sync marker in the trace.

    **EXPERIMENTAL**

    :param sync_id: The ID of this clock sync marker
    """
    params: T_JSON_DICT = dict()
    params["syncId"] = sync_id
    cmd_dict: T_JSON_DICT = {
        "method": "Tracing.recordClockSyncMarker",
        "params": params,
    }
    json = yield cmd_dict


def request_memory_dump(
    deterministic: typing.Optional[bool] = None,
    level_of_detail: typing.Optional[MemoryDumpLevelOfDetail] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.Tuple[str, bool]]:
    """
    Request a global memory dump.

    **EXPERIMENTAL**

    :param deterministic: *(Optional)* Enables more deterministic results by forcing garbage collection
    :param level_of_detail: *(Optional)* Specifies level of details in memory dump. Defaults to "detailed".
    :returns: A tuple with the following items:

        0. **dumpGuid** - GUID of the resulting global memory dump.
        1. **success** - True iff the global memory dump succeeded.
    """
    params: T_JSON_DICT = dict()
    if deterministic is not None:
        params["deterministic"] = deterministic
    if level_of_detail is not None:
        params["levelOfDetail"] = level_of_detail.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Tracing.requestMemoryDump",
        "params": params,
    }
    json = yield cmd_dict
    return (str(json["dumpGuid"]), bool(json["success"]))


def start(
    categories: typing.Optional[str] = None,
    options: typing.Optional[str] = None,
    buffer_usage_reporting_interval: typing.Optional[float] = None,
    transfer_mode: typing.Optional[str] = None,
    stream_format: typing.Optional[StreamFormat] = None,
    stream_compression: typing.Optional[StreamCompression] = None,
    trace_config: typing.Optional[TraceConfig] = None,
    perfetto_config: typing.Optional[str] = None,
    tracing_backend: typing.Optional[TracingBackend] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Start trace events collection.

    :param categories: **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* Category/tag filter
    :param options: **(DEPRECATED)** **(EXPERIMENTAL)** *(Optional)* Tracing options
    :param buffer_usage_reporting_interval: **(EXPERIMENTAL)** *(Optional)* If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
    :param transfer_mode: *(Optional)* Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to ```ReportEvents````).
    :param stream_format: *(Optional)* Trace data format to use. This only applies when using ````ReturnAsStream```` transfer mode (defaults to ````json````).
    :param stream_compression: **(EXPERIMENTAL)** *(Optional)* Compression format to use. This only applies when using ````ReturnAsStream```` transfer mode (defaults to ````none````)
    :param trace_config: *(Optional)*
    :param perfetto_config: **(EXPERIMENTAL)** *(Optional)* Base64-encoded serialized perfetto.protos.TraceConfig protobuf message When specified, the parameters ````categories````, ````options````, ````traceConfig```` are ignored. (Encoded as a base64 string when passed over JSON)
    :param tracing_backend: **(EXPERIMENTAL)** *(Optional)* Backend type (defaults to ````auto```)
    """
    params: T_JSON_DICT = dict()
    if categories is not None:
        params["categories"] = categories
    if options is not None:
        params["options"] = options
    if buffer_usage_reporting_interval is not None:
        params["bufferUsageReportingInterval"] = buffer_usage_reporting_interval
    if transfer_mode is not None:
        params["transferMode"] = transfer_mode
    if stream_format is not None:
        params["streamFormat"] = stream_format.to_json()
    if stream_compression is not None:
        params["streamCompression"] = stream_compression.to_json()
    if trace_config is not None:
        params["traceConfig"] = trace_config.to_json()
    if perfetto_config is not None:
        params["perfettoConfig"] = perfetto_config
    if tracing_backend is not None:
        params["tracingBackend"] = tracing_backend.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Tracing.start",
        "params": params,
    }
    json = yield cmd_dict


@event_class("Tracing.bufferUsage")
@dataclass
class BufferUsage:
    """
    **EXPERIMENTAL**


    """

    #: A number in range [0..1] that indicates the used size of event buffer as a fraction of its
    #: total size.
    percent_full: typing.Optional[float]
    #: An approximate number of events in the trace log.
    event_count: typing.Optional[float]
    #: A number in range [0..1] that indicates the used size of event buffer as a fraction of its
    #: total size.
    value: typing.Optional[float]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> BufferUsage:
        return cls(
            percent_full=(
                float(json["percentFull"])
                if json.get("percentFull", None) is not None
                else None
            ),
            event_count=(
                float(json["eventCount"])
                if json.get("eventCount", None) is not None
                else None
            ),
            value=float(json["value"]) if json.get("value", None) is not None else None,
        )


@event_class("Tracing.dataCollected")
@dataclass
class DataCollected:
    """
    **EXPERIMENTAL**

    Contains a bucket of collected trace events. When tracing is stopped collected events will be
    sent as a sequence of dataCollected events followed by tracingComplete event.
    """

    value: typing.List[dict]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DataCollected:
        return cls(value=[dict(i) for i in json["value"]])


@event_class("Tracing.tracingComplete")
@dataclass
class TracingComplete:
    """
    Signals that tracing is stopped and there is no trace buffers pending flush, all data were
    delivered via dataCollected events.
    """

    #: Indicates whether some trace data is known to have been lost, e.g. because the trace ring
    #: buffer wrapped around.
    data_loss_occurred: bool
    #: A handle of the stream that holds resulting trace data.
    stream: typing.Optional[io.StreamHandle]
    #: Trace data format of returned stream.
    trace_format: typing.Optional[StreamFormat]
    #: Compression format of returned stream.
    stream_compression: typing.Optional[StreamCompression]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> TracingComplete:
        return cls(
            data_loss_occurred=bool(json["dataLossOccurred"]),
            stream=(
                io.StreamHandle.from_json(json["stream"])
                if json.get("stream", None) is not None
                else None
            ),
            trace_format=(
                StreamFormat.from_json(json["traceFormat"])
                if json.get("traceFormat", None) is not None
                else None
            ),
            stream_compression=(
                StreamCompression.from_json(json["streamCompression"])
                if json.get("streamCompression", None) is not None
                else None
            ),
        )
