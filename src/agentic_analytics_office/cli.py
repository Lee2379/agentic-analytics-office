from __future__ import annotations

import argparse
from pathlib import Path

from .orchestrator import run_workflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentic-office",
        description="Run the deterministic Agentic Analytics Office evaluation harness.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    run = subparsers.add_parser("run", help="run the seven-stage analytics workflow")
    run.add_argument("--products", type=Path, required=True)
    run.add_argument("--sales", type=Path, required=True)
    run.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        metrics = run_workflow(args.products, args.sales, args.output)
        forecast = metrics["forecast"]
        print("Agentic Analytics Office: completed")
        print(f"stages: {metrics['workflow']['stages_completed']}/7")
        print(f"holdout MAE: {forecast['mae']:.2f} units")
        print(f"QA passed: {metrics['qa']['passed']}")
        print(f"artifacts: {args.output}")
        return 0
    return 2
