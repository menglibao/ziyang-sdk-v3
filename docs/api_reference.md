紫阳智库 v3 SDK API参考文档
============================

ZiyangSDK 类
------------

### `__init__(config: dict | None = None)`

初始化 SDK 实例。

- `config`: 可选配置字典，未提供时使用默认配置。

### `benchmark_quantum_convergence(iterations: int | None = None) -> BenchmarkResult`

执行量子收敛性能测试。

- `iterations`: 迭代次数，默认读取配置 `quantum_iterations`。

返回 `BenchmarkResult`，包含迭代次数、平均最终单元、吞吐量等指标。

### `benchmark_digital_root(data_size: int | None = None) -> BenchmarkResult`

执行数字根性能测试。

- `data_size`: 参与计算的数据规模。

返回 `BenchmarkResult`，包含吞吐量、最大/最小数字根、标准差等指标。

### `benchmark_cosmic_cycles(cycles: int | None = None) -> BenchmarkResult`

执行宇宙循环性能测试。

- `cycles`: 循环次数。

返回 `BenchmarkResult`，包含吞吐量、峰值状态、稳定性指数等指标。

### `comprehensive_benchmark() -> dict`

执行综合性能测试，返回包括三项基准测试结果及综合性能指标的字典。

CosmicMath 类
-------------

### `digital_root(n: int) -> int`

计算整数的数字根，支持 O(1) 算法。

### `quantum_convergence_path(base: int) -> dict`

计算量子收敛路径，返回最终单元值、路径字符串与步骤数。

### `multi_state_compression(data: Any) -> dict`

对任意可序列化数据生成压缩摘要。

BenchmarkResult 类
------------------

### `to_dict() -> dict`

将基准测试结果转换为字典。

### `to_json() -> str`

将基准测试结果转换为 JSON 字符串。

PerformanceTracker 类
---------------------

### `add_result(result: BenchmarkResult) -> None`

加入一条基准测试结果。

### `generate_report() -> str`

生成当前收集结果的文本报告。


