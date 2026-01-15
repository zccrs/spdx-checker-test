# 测试指南

本文档介绍如何测试 SPDX Checker Action 的各种功能。

## 测试场景

### 场景 1: 新文件带正确的 SPDX 头

**预期结果**: ✅ 通过检查

1. 创建一个新文件，例如 `test_new.py`
2. 添加当前年份的 SPDX 头：
   ```python
   # SPDX-FileCopyrightText: 2026 UnionTech Software Technology Co., Ltd.
   # SPDX-License-Identifier: GPL-3.0-or-later
   ```
3. 提交并创建 PR
4. 检查 workflow 运行结果

### 场景 2: 新文件缺少 SPDX 头

**预期结果**: ❌ 检查失败

1. 创建一个新文件，不添加 SPDX 头
2. 提交并创建 PR
3. 应该看到错误信息提示缺少 SPDX 头

### 场景 3: 新文件使用错误的年份

**预期结果**: ❌ 检查失败

1. 创建一个新文件
2. 添加错误年份的 SPDX 头（如 2020）
3. 提交并创建 PR
4. 应该看到错误信息提示年份不正确

### 场景 4: 修改旧文件（需要更新年份范围）

**预期结果**: 根据文件创建时间决定

1. 修改一个已存在的文件
2. 如果文件是今年创建的，使用单年份 `2026`
3. 如果文件是往年创建的，使用年份范围 `YYYY-2026`
4. 提交并创建 PR

## 手动测试命令

如果安装了 Python 环境，也可以本地运行检查脚本：

```bash
# 克隆 spdx-checker action 仓库
git clone https://github.com/zccrs/github-actions-spdx-checker.git

# 在测试项目中运行检查
cd /path/to/spdx-checker-test
python3 ../github-actions-spdx-checker/scripts/check_spdx_headers.py --base origin/main
```

## 查看检查结果

1. 进入 GitHub Actions 页面
2. 查看 "SPDX Header Check" workflow
3. 点击具体的运行记录查看详细日志
