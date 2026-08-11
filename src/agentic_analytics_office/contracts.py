from __future__ import annotations

import json
from importlib.resources import files
from pathlib import Path
from typing import Any


REQUIRED_AGENT_FIELDS = {
    "name",
    "role",
    "objective",
    "allowed_inputs",
    "required_outputs",
    "reviewed_by",
}


def load_agent_contracts(path: str | Path | None = None) -> dict[str, Any]:
    if path is None:
        source_text = files("agentic_analytics_office").joinpath("agent_contracts.json").read_text(
            encoding="utf-8"
        )
        source_name = "packaged agent_contracts.json"
    else:
        source = Path(path)
        source_text = source.read_text(encoding="utf-8")
        source_name = str(source)

    try:
        payload = json.loads(source_text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{source_name}: invalid JSON") from exc

    if not isinstance(payload, dict) or not isinstance(payload.get("version"), str):
        raise ValueError(f"{source_name}: contract registry requires a string version")
    agents = payload.get("agents")
    if not isinstance(agents, list) or not agents:
        raise ValueError(f"{source_name}: contract registry requires a non-empty agents list")

    seen: set[str] = set()
    for index, agent in enumerate(agents):
        if not isinstance(agent, dict):
            raise ValueError(f"{source_name}: agents[{index}] must be an object")
        missing = sorted(REQUIRED_AGENT_FIELDS - set(agent))
        if missing:
            raise ValueError(
                f"{source_name}: agents[{index}] missing fields: {', '.join(missing)}"
            )
        for field in ("name", "role", "objective", "reviewed_by"):
            if not isinstance(agent[field], str) or not agent[field].strip():
                raise ValueError(f"{source_name}: agents[{index}].{field} must be non-empty")
        for field in ("allowed_inputs", "required_outputs"):
            values = agent[field]
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value for value in values
            ):
                raise ValueError(
                    f"{source_name}: agents[{index}].{field} must be a non-empty string list"
                )
        if agent["name"] in seen:
            raise ValueError(f"{source_name}: duplicate agent name {agent['name']}")
        seen.add(agent["name"])
    return payload


def canonical_contract_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
