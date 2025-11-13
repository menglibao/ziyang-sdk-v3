"""基础使用示例."""

from __future__ import annotations

from ziyang.core import ZiyangSDK


def demo_basic_capabilities() -> None:
    """演示 SDK 基础功能."""

    sdk = ZiyangSDK()

    print("1. 量子收敛测试:")
    qc_result = sdk.benchmark_quantum_convergence()
    print(f"   吞吐量: {qc_result.metrics['operations_per_second']:.2f} ops/s")

    print("2. 综合性能测试:")
    comprehensive = sdk.comprehensive_benchmark()
    print(
        f"   等效算力: {comprehensive['performance_metrics']['estimated_flops']:.2f} FLOPS"
    )


if __name__ == "__main__":
    demo_basic_capabilities()


