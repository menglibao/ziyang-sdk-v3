"""高级使用示例 - 自定义测试配置."""

from __future__ import annotations

import json

from ziyang.core import ZiyangSDK


def custom_benchmark_config() -> None:
    """自定义基准测试配置."""

    config = {
        "quantum_iterations": 256,
        "digital_root_samples": 2048,
        "cosmic_cycles": 512,
        "flops_multiplier": 2.0,
    }

    sdk = ZiyangSDK(config)
    results = sdk.comprehensive_benchmark()

    with open("benchmark_results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=2)
    print("结果已写入 benchmark_results.json")


if __name__ == "__main__":
    custom_benchmark_config()


