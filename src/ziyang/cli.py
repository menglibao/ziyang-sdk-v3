"""命令行接口工具."""

from __future__ import annotations

import argparse
from typing import Any, Dict

from .core import ZiyangSDK


def _run_single_benchmark(sdk: ZiyangSDK, test: str, iterations: int) -> Dict[str, Any]:
    if test == "quantum":
        result = sdk.benchmark_quantum_convergence(iterations)
        return result.to_dict()
    if test == "digital":
        result = sdk.benchmark_digital_root(iterations)
        return result.to_dict()
    if test == "cosmic":
        result = sdk.benchmark_cosmic_cycles(iterations)
        return result.to_dict()
    combined = sdk.comprehensive_benchmark()
    return combined


def run_benchmarks(sdk: ZiyangSDK, args: argparse.Namespace) -> Dict[str, Any]:
    """根据命令行参数运行基准测试."""

    return _run_single_benchmark(sdk, args.test, args.iterations)


def format_output(results: Dict[str, Any], output_format: str) -> str:
    """根据输出格式格式化结果."""

    if output_format == "json":
        import json

        return json.dumps(results, ensure_ascii=False, indent=2)
    if output_format == "text":
        lines = ["紫阳智库 v3 性能测试结果"]

        def _append_metrics(label: str, metrics: Dict[str, Any]) -> None:
            lines.append(f"[{label}]")
            for metric, metric_value in metrics.items():
                lines.append(f"  - {metric}: {metric_value}")

        if "metrics" in results:
            label = results.get("name", "benchmark")
            _append_metrics(label, results["metrics"])
        else:
            for key, value in results.items():
                if isinstance(value, dict) and "metrics" in value:
                    _append_metrics(key, value["metrics"])
                else:
                    lines.append(f"{key}: {value}")
        return "\n".join(lines)
    if output_format == "csv":
        if "metrics" in results:
            headers = ",".join(results["metrics"].keys())
            values = ",".join(str(v) for v in results["metrics"].values())
            return f"{headers}\n{values}"
        flat_metrics = []
        for key, value in results.items():
            if isinstance(value, dict) and "metrics" in value:
                flat_metrics.append(
                    ",".join(str(val) for val in value["metrics"].values())
                )
        return "\n".join(flat_metrics)

    raise ValueError(f"不支持的输出格式：{output_format}")


def main() -> None:
    parser = argparse.ArgumentParser(description="紫阳智库v3算力测试工具")
    parser.add_argument(
        "--test",
        choices=["quantum", "digital", "cosmic", "all"],
        default="all",
        help="选择测试类型",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=1000,
        help="测试迭代次数",
    )
    parser.add_argument(
        "--output",
        choices=["json", "text", "csv"],
        default="text",
        help="输出格式",
    )
    args = parser.parse_args()

    sdk = ZiyangSDK()
    results = run_benchmarks(sdk, args)
    print(format_output(results, args.output))


if __name__ == "__main__":
    main()
