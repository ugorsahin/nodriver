# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Accessibility (experimental)

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import dom, page, runtime
from .util import T_JSON_DICT, event_class


class AXNodeId(str):
    """
    Unique accessibility node identifier.
    """

    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> AXNodeId:
        return cls(json)

    def __repr__(self):
        return "AXNodeId({})".format(super().__repr__())


class AXValueType(enum.Enum):
    """
    Enum of possible property types.
    """

    BOOLEAN = "boolean"
    TRISTATE = "tristate"
    BOOLEAN_OR_UNDEFINED = "booleanOrUndefined"
    IDREF = "idref"
    IDREF_LIST = "idrefList"
    INTEGER = "integer"
    NODE = "node"
    NODE_LIST = "nodeList"
    NUMBER = "number"
    STRING = "string"
    COMPUTED_STRING = "computedString"
    TOKEN = "token"
    TOKEN_LIST = "tokenList"
    DOM_RELATION = "domRelation"
    ROLE = "role"
    INTERNAL_ROLE = "internalRole"
    VALUE_UNDEFINED = "valueUndefined"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AXValueType:
        return cls(json)


class AXValueSourceType(enum.Enum):
    """
    Enum of possible property sources.
    """

    ATTRIBUTE = "attribute"
    IMPLICIT = "implicit"
    STYLE = "style"
    CONTENTS = "contents"
    PLACEHOLDER = "placeholder"
    RELATED_ELEMENT = "relatedElement"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AXValueSourceType:
        return cls(json)


class AXValueNativeSourceType(enum.Enum):
    """
    Enum of possible native property sources (as a subtype of a particular AXValueSourceType).
    """

    DESCRIPTION = "description"
    FIGCAPTION = "figcaption"
    LABEL = "label"
    LABELFOR = "labelfor"
    LABELWRAPPED = "labelwrapped"
    LEGEND = "legend"
    RUBYANNOTATION = "rubyannotation"
    TABLECAPTION = "tablecaption"
    TITLE = "title"
    OTHER = "other"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AXValueNativeSourceType:
        return cls(json)


@dataclass
class AXValueSource:
    """
    A single source for a computed AX property.
    """

    #: What type of source this is.
    type_: AXValueSourceType

    #: The value of this property source.
    value: typing.Optional[AXValue] = None

    #: The name of the relevant attribute, if any.
    attribute: typing.Optional[str] = None

    #: The value of the relevant attribute, if any.
    attribute_value: typing.Optional[AXValue] = None

    #: Whether this source is superseded by a higher priority source.
    superseded: typing.Optional[bool] = None

    #: The native markup source for this value, e.g. a ``<label>`` element.
    native_source: typing.Optional[AXValueNativeSourceType] = None

    #: The value, such as a node or node list, of the native source.
    native_source_value: typing.Optional[AXValue] = None

    #: Whether the value for this property is invalid.
    invalid: typing.Optional[bool] = None

    #: Reason for the value being invalid, if it is.
    invalid_reason: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["type"] = self.type_.to_json()
        if self.value is not None:
            json["value"] = self.value.to_json()
        if self.attribute is not None:
            json["attribute"] = self.attribute
        if self.attribute_value is not None:
            json["attributeValue"] = self.attribute_value.to_json()
        if self.superseded is not None:
            json["superseded"] = self.superseded
        if self.native_source is not None:
            json["nativeSource"] = self.native_source.to_json()
        if self.native_source_value is not None:
            json["nativeSourceValue"] = self.native_source_value.to_json()
        if self.invalid is not None:
            json["invalid"] = self.invalid
        if self.invalid_reason is not None:
            json["invalidReason"] = self.invalid_reason
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AXValueSource:
        return cls(
            type_=AXValueSourceType.from_json(json["type"]),
            value=(
                AXValue.from_json(json["value"])
                if json.get("value", None) is not None
                else None
            ),
            attribute=(
                str(json["attribute"])
                if json.get("attribute", None) is not None
                else None
            ),
            attribute_value=(
                AXValue.from_json(json["attributeValue"])
                if json.get("attributeValue", None) is not None
                else None
            ),
            superseded=(
                bool(json["superseded"])
                if json.get("superseded", None) is not None
                else None
            ),
            native_source=(
                AXValueNativeSourceType.from_json(json["nativeSource"])
                if json.get("nativeSource", None) is not None
                else None
            ),
            native_source_value=(
                AXValue.from_json(json["nativeSourceValue"])
                if json.get("nativeSourceValue", None) is not None
                else None
            ),
            invalid=(
                bool(json["invalid"]) if json.get("invalid", None) is not None else None
            ),
            invalid_reason=(
                str(json["invalidReason"])
                if json.get("invalidReason", None) is not None
                else None
            ),
        )


@dataclass
class AXRelatedNode:
    #: The BackendNodeId of the related DOM node.
    backend_dom_node_id: dom.BackendNodeId

    #: The IDRef value provided, if any.
    idref: typing.Optional[str] = None

    #: The text alternative of this node in the current context.
    text: typing.Optional[str] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["backendDOMNodeId"] = self.backend_dom_node_id.to_json()
        if self.idref is not None:
            json["idref"] = self.idref
        if self.text is not None:
            json["text"] = self.text
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AXRelatedNode:
        return cls(
            backend_dom_node_id=dom.BackendNodeId.from_json(json["backendDOMNodeId"]),
            idref=str(json["idref"]) if json.get("idref", None) is not None else None,
            text=str(json["text"]) if json.get("text", None) is not None else None,
        )


@dataclass
class AXProperty:
    #: The name of this property.
    name: AXPropertyName

    #: The value of this property.
    value: AXValue

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["name"] = self.name.to_json()
        json["value"] = self.value.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AXProperty:
        return cls(
            name=AXPropertyName.from_json(json["name"]),
            value=AXValue.from_json(json["value"]),
        )


@dataclass
class AXValue:
    """
    A single computed AX property.
    """

    #: The type of this value.
    type_: AXValueType

    #: The computed value of this property.
    value: typing.Optional[typing.Any] = None

    #: One or more related nodes, if applicable.
    related_nodes: typing.Optional[typing.List[AXRelatedNode]] = None

    #: The sources which contributed to the computation of this property.
    sources: typing.Optional[typing.List[AXValueSource]] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["type"] = self.type_.to_json()
        if self.value is not None:
            json["value"] = self.value
        if self.related_nodes is not None:
            json["relatedNodes"] = [i.to_json() for i in self.related_nodes]
        if self.sources is not None:
            json["sources"] = [i.to_json() for i in self.sources]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AXValue:
        return cls(
            type_=AXValueType.from_json(json["type"]),
            value=json["value"] if json.get("value", None) is not None else None,
            related_nodes=(
                [AXRelatedNode.from_json(i) for i in json["relatedNodes"]]
                if json.get("relatedNodes", None) is not None
                else None
            ),
            sources=(
                [AXValueSource.from_json(i) for i in json["sources"]]
                if json.get("sources", None) is not None
                else None
            ),
        )


class AXPropertyName(enum.Enum):
    """
    Values of AXProperty name:
    - from 'busy' to 'roledescription': states which apply to every AX node
    - from 'live' to 'root': attributes which apply to nodes in live regions
    - from 'autocomplete' to 'valuetext': attributes which apply to widgets
    - from 'checked' to 'selected': states which apply to widgets
    - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
    """

    ACTIONS = "actions"
    BUSY = "busy"
    DISABLED = "disabled"
    EDITABLE = "editable"
    FOCUSABLE = "focusable"
    FOCUSED = "focused"
    HIDDEN = "hidden"
    HIDDEN_ROOT = "hiddenRoot"
    INVALID = "invalid"
    KEYSHORTCUTS = "keyshortcuts"
    SETTABLE = "settable"
    ROLEDESCRIPTION = "roledescription"
    LIVE = "live"
    ATOMIC = "atomic"
    RELEVANT = "relevant"
    ROOT = "root"
    AUTOCOMPLETE = "autocomplete"
    HAS_POPUP = "hasPopup"
    LEVEL = "level"
    MULTISELECTABLE = "multiselectable"
    ORIENTATION = "orientation"
    MULTILINE = "multiline"
    READONLY = "readonly"
    REQUIRED = "required"
    VALUEMIN = "valuemin"
    VALUEMAX = "valuemax"
    VALUETEXT = "valuetext"
    CHECKED = "checked"
    EXPANDED = "expanded"
    MODAL = "modal"
    PRESSED = "pressed"
    SELECTED = "selected"
    ACTIVEDESCENDANT = "activedescendant"
    CONTROLS = "controls"
    DESCRIBEDBY = "describedby"
    DETAILS = "details"
    ERRORMESSAGE = "errormessage"
    FLOWTO = "flowto"
    LABELLEDBY = "labelledby"
    OWNS = "owns"
    URL = "url"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AXPropertyName:
        return cls(json)


@dataclass
class AXNode:
    """
    A node in the accessibility tree.
    """

    #: Unique identifier for this node.
    node_id: AXNodeId

    #: Whether this node is ignored for accessibility
    ignored: bool

    #: Collection of reasons why this node is hidden.
    ignored_reasons: typing.Optional[typing.List[AXProperty]] = None

    #: This ``Node``'s role, whether explicit or implicit.
    role: typing.Optional[AXValue] = None

    #: This ``Node``'s Chrome raw role.
    chrome_role: typing.Optional[AXValue] = None

    #: The accessible name for this ``Node``.
    name: typing.Optional[AXValue] = None

    #: The accessible description for this ``Node``.
    description: typing.Optional[AXValue] = None

    #: The value for this ``Node``.
    value: typing.Optional[AXValue] = None

    #: All other properties
    properties: typing.Optional[typing.List[AXProperty]] = None

    #: ID for this node's parent.
    parent_id: typing.Optional[AXNodeId] = None

    #: IDs for each of this node's child nodes.
    child_ids: typing.Optional[typing.List[AXNodeId]] = None

    #: The backend ID for the associated DOM node, if any.
    backend_dom_node_id: typing.Optional[dom.BackendNodeId] = None

    #: The frame ID for the frame associated with this nodes document.
    frame_id: typing.Optional[page.FrameId] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["nodeId"] = self.node_id.to_json()
        json["ignored"] = self.ignored
        if self.ignored_reasons is not None:
            json["ignoredReasons"] = [i.to_json() for i in self.ignored_reasons]
        if self.role is not None:
            json["role"] = self.role.to_json()
        if self.chrome_role is not None:
            json["chromeRole"] = self.chrome_role.to_json()
        if self.name is not None:
            json["name"] = self.name.to_json()
        if self.description is not None:
            json["description"] = self.description.to_json()
        if self.value is not None:
            json["value"] = self.value.to_json()
        if self.properties is not None:
            json["properties"] = [i.to_json() for i in self.properties]
        if self.parent_id is not None:
            json["parentId"] = self.parent_id.to_json()
        if self.child_ids is not None:
            json["childIds"] = [i.to_json() for i in self.child_ids]
        if self.backend_dom_node_id is not None:
            json["backendDOMNodeId"] = self.backend_dom_node_id.to_json()
        if self.frame_id is not None:
            json["frameId"] = self.frame_id.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AXNode:
        return cls(
            node_id=AXNodeId.from_json(json["nodeId"]),
            ignored=bool(json["ignored"]),
            ignored_reasons=(
                [AXProperty.from_json(i) for i in json["ignoredReasons"]]
                if json.get("ignoredReasons", None) is not None
                else None
            ),
            role=(
                AXValue.from_json(json["role"])
                if json.get("role", None) is not None
                else None
            ),
            chrome_role=(
                AXValue.from_json(json["chromeRole"])
                if json.get("chromeRole", None) is not None
                else None
            ),
            name=(
                AXValue.from_json(json["name"])
                if json.get("name", None) is not None
                else None
            ),
            description=(
                AXValue.from_json(json["description"])
                if json.get("description", None) is not None
                else None
            ),
            value=(
                AXValue.from_json(json["value"])
                if json.get("value", None) is not None
                else None
            ),
            properties=(
                [AXProperty.from_json(i) for i in json["properties"]]
                if json.get("properties", None) is not None
                else None
            ),
            parent_id=(
                AXNodeId.from_json(json["parentId"])
                if json.get("parentId", None) is not None
                else None
            ),
            child_ids=(
                [AXNodeId.from_json(i) for i in json["childIds"]]
                if json.get("childIds", None) is not None
                else None
            ),
            backend_dom_node_id=(
                dom.BackendNodeId.from_json(json["backendDOMNodeId"])
                if json.get("backendDOMNodeId", None) is not None
                else None
            ),
            frame_id=(
                page.FrameId.from_json(json["frameId"])
                if json.get("frameId", None) is not None
                else None
            ),
        )


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables the accessibility domain.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.disable",
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables the accessibility domain which causes ``AXNodeId``'s to remain consistent between method calls.
    This turns on accessibility for the page, which can impact performance until accessibility is disabled.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.enable",
    }
    json = yield cmd_dict


def get_partial_ax_tree(
    node_id: typing.Optional[dom.NodeId] = None,
    backend_node_id: typing.Optional[dom.BackendNodeId] = None,
    object_id: typing.Optional[runtime.RemoteObjectId] = None,
    fetch_relatives: typing.Optional[bool] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[AXNode]]:
    """
    Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.

    **EXPERIMENTAL**

    :param node_id: *(Optional)* Identifier of the node to get the partial accessibility tree for.
    :param backend_node_id: *(Optional)* Identifier of the backend node to get the partial accessibility tree for.
    :param object_id: *(Optional)* JavaScript object id of the node wrapper to get the partial accessibility tree for.
    :param fetch_relatives: *(Optional)* Whether to fetch this node's ancestors, siblings and children. Defaults to true.
    :returns: The ``Accessibility.AXNode`` for this DOM node, if it exists, plus its ancestors, siblings and children, if requested.
    """
    params: T_JSON_DICT = dict()
    if node_id is not None:
        params["nodeId"] = node_id.to_json()
    if backend_node_id is not None:
        params["backendNodeId"] = backend_node_id.to_json()
    if object_id is not None:
        params["objectId"] = object_id.to_json()
    if fetch_relatives is not None:
        params["fetchRelatives"] = fetch_relatives
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.getPartialAXTree",
        "params": params,
    }
    json = yield cmd_dict
    return [AXNode.from_json(i) for i in json["nodes"]]


def get_full_ax_tree(
    depth: typing.Optional[int] = None, frame_id: typing.Optional[page.FrameId] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[AXNode]]:
    """
    Fetches the entire accessibility tree for the root Document

    **EXPERIMENTAL**

    :param depth: *(Optional)* The maximum depth at which descendants of the root node should be retrieved. If omitted, the full tree is returned.
    :param frame_id: *(Optional)* The frame for whose document the AX tree should be retrieved. If omitted, the root frame is used.
    :returns:
    """
    params: T_JSON_DICT = dict()
    if depth is not None:
        params["depth"] = depth
    if frame_id is not None:
        params["frameId"] = frame_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.getFullAXTree",
        "params": params,
    }
    json = yield cmd_dict
    return [AXNode.from_json(i) for i in json["nodes"]]


def get_root_ax_node(
    frame_id: typing.Optional[page.FrameId] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, AXNode]:
    """
    Fetches the root node.
    Requires ``enable()`` to have been called previously.

    **EXPERIMENTAL**

    :param frame_id: *(Optional)* The frame in whose document the node resides. If omitted, the root frame is used.
    :returns:
    """
    params: T_JSON_DICT = dict()
    if frame_id is not None:
        params["frameId"] = frame_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.getRootAXNode",
        "params": params,
    }
    json = yield cmd_dict
    return AXNode.from_json(json["node"])


def get_ax_node_and_ancestors(
    node_id: typing.Optional[dom.NodeId] = None,
    backend_node_id: typing.Optional[dom.BackendNodeId] = None,
    object_id: typing.Optional[runtime.RemoteObjectId] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[AXNode]]:
    """
    Fetches a node and all ancestors up to and including the root.
    Requires ``enable()`` to have been called previously.

    **EXPERIMENTAL**

    :param node_id: *(Optional)* Identifier of the node to get.
    :param backend_node_id: *(Optional)* Identifier of the backend node to get.
    :param object_id: *(Optional)* JavaScript object id of the node wrapper to get.
    :returns:
    """
    params: T_JSON_DICT = dict()
    if node_id is not None:
        params["nodeId"] = node_id.to_json()
    if backend_node_id is not None:
        params["backendNodeId"] = backend_node_id.to_json()
    if object_id is not None:
        params["objectId"] = object_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.getAXNodeAndAncestors",
        "params": params,
    }
    json = yield cmd_dict
    return [AXNode.from_json(i) for i in json["nodes"]]


def get_child_ax_nodes(
    id_: AXNodeId, frame_id: typing.Optional[page.FrameId] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[AXNode]]:
    """
    Fetches a particular accessibility node by AXNodeId.
    Requires ``enable()`` to have been called previously.

    **EXPERIMENTAL**

    :param id_:
    :param frame_id: *(Optional)* The frame in whose document the node resides. If omitted, the root frame is used.
    :returns:
    """
    params: T_JSON_DICT = dict()
    params["id"] = id_.to_json()
    if frame_id is not None:
        params["frameId"] = frame_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.getChildAXNodes",
        "params": params,
    }
    json = yield cmd_dict
    return [AXNode.from_json(i) for i in json["nodes"]]


def query_ax_tree(
    node_id: typing.Optional[dom.NodeId] = None,
    backend_node_id: typing.Optional[dom.BackendNodeId] = None,
    object_id: typing.Optional[runtime.RemoteObjectId] = None,
    accessible_name: typing.Optional[str] = None,
    role: typing.Optional[str] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[AXNode]]:
    """
    Query a DOM node's accessibility subtree for accessible name and role.
    This command computes the name and role for all nodes in the subtree, including those that are
    ignored for accessibility, and returns those that match the specified name and role. If no DOM
    node is specified, or the DOM node does not exist, the command returns an error. If neither
    ``accessibleName`` or ``role`` is specified, it returns all the accessibility nodes in the subtree.

    **EXPERIMENTAL**

    :param node_id: *(Optional)* Identifier of the node for the root to query.
    :param backend_node_id: *(Optional)* Identifier of the backend node for the root to query.
    :param object_id: *(Optional)* JavaScript object id of the node wrapper for the root to query.
    :param accessible_name: *(Optional)* Find nodes with this computed name.
    :param role: *(Optional)* Find nodes with this computed role.
    :returns: A list of ``Accessibility.AXNode`` matching the specified attributes, including nodes that are ignored for accessibility.
    """
    params: T_JSON_DICT = dict()
    if node_id is not None:
        params["nodeId"] = node_id.to_json()
    if backend_node_id is not None:
        params["backendNodeId"] = backend_node_id.to_json()
    if object_id is not None:
        params["objectId"] = object_id.to_json()
    if accessible_name is not None:
        params["accessibleName"] = accessible_name
    if role is not None:
        params["role"] = role
    cmd_dict: T_JSON_DICT = {
        "method": "Accessibility.queryAXTree",
        "params": params,
    }
    json = yield cmd_dict
    return [AXNode.from_json(i) for i in json["nodes"]]


@event_class("Accessibility.loadComplete")
@dataclass
class LoadComplete:
    """
    **EXPERIMENTAL**

    The loadComplete event mirrors the load complete event sent by the browser to assistive
    technology when the web page has finished loading.
    """

    #: New document root node.
    root: AXNode

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> LoadComplete:
        return cls(root=AXNode.from_json(json["root"]))


@event_class("Accessibility.nodesUpdated")
@dataclass
class NodesUpdated:
    """
    **EXPERIMENTAL**

    The nodesUpdated event is sent every time a previously requested node has changed the in tree.
    """

    #: Updated node data.
    nodes: typing.List[AXNode]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> NodesUpdated:
        return cls(nodes=[AXNode.from_json(i) for i in json["nodes"]])
