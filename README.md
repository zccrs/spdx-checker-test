# SPDX Checker Test Project

这是一个用于测试 [github-actions-spdx-checker](https://github.com/zccrs/github-actions-spdx-checker) Action 的项目。

## 项目结构

```
.
├── .github/
│   └── workflows/
│       └── spdx-check.yml          # SPDX 检查工作流
├── examples/
│   ├── correct/                    # 包含正确 SPDX 头的示例文件
│   │   ├── example.py
│   │   ├── example.cpp
│   │   └── example.sh
│   └── incorrect/                  # 包含错误 SPDX 头的示例文件（用于测试）
│       ├── missing_header.py
│       └── wrong_year.py
└── README.md

```

## 使用方法

### 测试 Action 功能

1. **创建新文件测试**：
   - 添加一个新文件到 `examples/correct/` 目录
   - 添加正确格式的 SPDX 头（使用当前年份 2026）
   - 提交并创建 PR
   - 检查 Action 是否通过

2. **测试错误检测**：
   - 添加一个没有 SPDX 头的文件
   - 或添加错误年份的 SPDX 头
   - 提交并创建 PR
   - 检查 Action 是否正确报错

### 正确的 SPDX 头格式

#### Python/Shell 文件：
```python
# SPDX-FileCopyrightText: 2026 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-3.0-or-later
```

#### C/C++/JavaScript 文件：
```cpp
// SPDX-FileCopyrightText: 2026 UnionTech Software Technology Co., Ltd.
// SPDX-License-Identifier: GPL-3.0-or-later
```

## GitHub Actions Workflow

项目配置了自动 SPDX 头检查，会在以下情况触发：
- Pull Request 提交到 main 分支时
- 直接推送到 main 分支时

检查范围包括：
- Python (`.py`)
- JavaScript/TypeScript (`.js`, `.ts`)
- C/C++ (`.cpp`, `.c`, `.h`)
- Shell (`.sh`)
- YAML (`.yaml`, `.yml`)

## 相关链接

- [SPDX Checker Action](https://github.com/zccrs/github-actions-spdx-checker)
- [SPDX 规范](https://spdx.dev/)

## License

GPL-3.0-or-later
