# US Address Generator

随机生成逼真的美国地址信息，用于测试和表单填写等场景。

**单文件 Python 3 脚本，零依赖** — 仅使用标准库。

[English](README_EN.md)

## 特性

- 生成完整的美国地址信息：姓名、街道、公寓号、城市、州、邮编、电话、邮箱
- 内置全部 50 州 + DC 的真实数据（城市、邮编范围、区号）
- **默认从免税州生成**（OR、MT、NH、DE、AK）
- 支持文本和 JSON 两种输出格式
- 支持批量生成

## 安装

```bash
git clone https://github.com/zchdu/us-address-generator.git
cd us-address-generator
```

无需安装任何依赖，只需 Python 3。

## 使用方法

```bash
# 生成 1 个地址（随机免税州）
python3 us_address_generator.py

# 生成 5 个地址
python3 us_address_generator.py -n 5

# 指定州
python3 us_address_generator.py -s CA

# JSON 格式输出
python3 us_address_generator.py -n 3 -f json

# 组合使用
python3 us_address_generator.py -n 2 -s NY -f json
```

### 命令行参数

| 参数 | 说明 |
|------|------|
| `-n`, `--count` | 生成数量（默认 1） |
| `-s`, `--state` | 指定州缩写（如 `CA`、`NY`），不指定则从免税州随机选取 |
| `-f`, `--format` | 输出格式：`text`（默认）或 `json` |
| `-h`, `--help` | 显示帮助信息 |

## 输出示例

### 文本格式（默认）

```
John Smith
1234 Oak Avenue, Apt 5B
Los Angeles, CA 90012
Phone: (213) 555-1234
Email: john.smith@gmail.com
```

### JSON 格式（`-f json`）

```json
{
  "first_name": "John",
  "last_name": "Smith",
  "street": "1234 Oak Avenue",
  "apt": "Apt 5B",
  "city": "Los Angeles",
  "state": "CA",
  "zip": "90012",
  "phone": "(213) 555-1234",
  "email": "john.smith@gmail.com"
}
```

批量生成时（`-n` > 1），JSON 输出为数组格式。

## 生成字段说明

| 字段 | 生成方式 |
|------|---------|
| 姓名 | 从常见美国姓名库随机组合 |
| 街道 | 随机门牌号 + 街道名 + 类型（St/Ave/Blvd/Dr/...），可能带方向前缀 |
| 公寓号 | 25% 概率出现，随机格式（Apt/Suite/Unit/#） |
| 城市 | 按所选州匹配真实城市 |
| 州 | 支持全部 50 州 + DC |
| 邮编 | 在该州真实邮编范围内生成 |
| 电话 | 使用该州真实区号 |
| 邮箱 | 基于生成的姓名 + 随机域名 |

## 免税州

未指定 `--state` 时，默认从以下无消费税的州中随机选取：

- **Oregon (OR)** — 俄勒冈
- **Montana (MT)** — 蒙大拿
- **New Hampshire (NH)** — 新罕布什尔
- **Delaware (DE)** — 特拉华
- **Alaska (AK)** — 阿拉斯加

## License

MIT
