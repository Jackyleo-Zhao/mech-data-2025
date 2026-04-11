# mech-data-2025

> 中国大学生机械工程创新创意大赛赛后整理展示仓库

本仓库整理了本人在中国大学生机械工程创新创意大赛中的部分核心代码与数据分析任务，内容涵盖工业监测数据读取、统计特征分析、异常检测与维护需求预测等环节。仓库对代码结构、命名方式、目录组织与运行流程进行了系统整理，用于展示本人在**数据理解、任务实现、工程组织与赛后整理**方面的综合能力。

## 项目概览

- **竞赛名称**：中国大学生机械工程创新创意大赛
- **项目负责人**：赵明艳（队长）
- **获奖情况**：国家二等奖
- **仓库名称**：`mech-data-2025`

## 项目定位

本仓库不是比赛现场原始代码的直接堆叠，而是面向科研展示场景完成的赛后整理版本。整理重点不在于“重新包装代码”，而在于更清晰地呈现一个完整的问题求解链条：

**工业数据接入 → 状态统计分析 → 异常样本识别 → 维护需求预测 → 工程化组织表达**

对于竞赛项目而言，真正能够体现差异的，往往不只是是否完成题目本身，而在于能否在赛后将零散实现整理成一个**结构清楚、逻辑完整、可审阅、可复现、可展示**的仓库。本项目即围绕这一目标完成重构。

## 任务内容

本仓库主要包含两类任务。

### 1. 基于 InfluxDB 的轴承状态统计分析

围绕比赛环境提供的 InfluxDB 数据库，对不同轴承状态的监测数据进行统计分析与可视化处理，主要包括：

- `normal / inner / outer / holder` 四类状态的标准差分析
- `normal / inner / outer / holder` 四类状态的偏度分析
- 不同状态偏度的可视化对比
- `unknown` 状态样本的统计特征分析

这一部分对应：

- `src/q1_bearing_std_analysis.py`
- `src/q2_bearing_skew_analysis.py`
- `src/q3_bearing_skew_visualization.py`
- `src/q4_unknown_condition_analysis.py`

该部分体现了对**工业时序数据库读取、统计量提取与状态表征分析**的基本实现能力。

### 2. 基于结构化数据的异常检测与维护预测

围绕题目提供的结构化数据文件，完成两个相对完整的数据分析任务：

#### （1）基于 3σ 原则的异常检测
使用正常参考样本建立统计边界，对待检测样本逐条判断其是否越界，从而识别异常样本。

对应脚本：

- `src/q5_three_sigma_detection.py`

#### （2）基于 Random Forest 的维护需求预测
使用带标签训练集构建设备维护需求分类模型，并对待预测数据输出维护需求判断结果。

对应脚本：

- `src/q6_maintenance_prediction.py`

该部分体现了对**统计异常检测、监督学习建模、结果输出与结构化数据处理**的完整实现能力。

## 仓库结构

```text
mech-data-2025/
├── data/
│   ├── problem3/
│   │   ├── normal_reference.csv
│   │   └── unknown_samples.csv
│   └── problem4/
│       ├── train.csv
│       └── predict.csv
├── src/
│   ├── common/
│   │   ├── __init__.py
│   │   ├── influx_config.py
│   │   ├── influx_helpers.py
│   │   └── paths.py
│   ├── q1_bearing_std_analysis.py
│   ├── q2_bearing_skew_analysis.py
│   ├── q3_bearing_skew_visualization.py
│   ├── q4_unknown_condition_analysis.py
│   ├── q5_three_sigma_detection.py
│   └── q6_maintenance_prediction.py
├── .gitignore
├── README.md
└── requirements.txt
