## 🧮 小学四则运算题目生成与判分系统

### 📘 项目简介

本项目实现了一个 **小学四则运算题目自动生成与判分程序**，支持生成指定数量与范围的随机四则运算题目，
并可根据用户提交的答案文件进行自动判分，输出统计结果。

系统功能模块化设计，包含：

* `generator.py` —— 自动生成题目与标准答案
* `evaluator.py` —— 四则运算表达式解析与计算
* `checker.py` —— 自动判题与结果统计
* `utils.py` —— 分数与带分数的格式化辅助函数
* `main.py` —— 命令行参数入口与模式控制

---

### ⚙️ 项目结构

```
合作作业/
│
├── main.py          # 主程序入口（解析命令行参数）
├── generator.py     # 生成四则运算题目与标准答案
├── evaluator.py     # 计算表达式值，支持分数与带分数
├── checker.py       # 对比答案文件与标准答案，生成判分报告
├── utils.py         # 工具函数（分数格式化）
├── Exercises.txt    # 自动生成的题目文件（示例）
├── Answers.txt      # 自动生成的标准答案（示例）
└── Grade.txt        # 判分结果输出文件
```

---

### 🧩 使用方法

#### 1️⃣ 生成题目

运行以下命令以生成题目和标准答案：

```bash
python main.py -n 10 -r 10
```

**参数说明：**

* `-n`：生成题目数量（默认 10）
* `-r`：题目中数字的取值范围（必须指定）

生成后，程序会在当前目录下生成：

* `Exercises.txt`：题目文件
* `Answers.txt`：标准答案文件

---

#### 2️⃣ 判分功能

当你有一份答案文件（如 `MyAnswers.txt`）时，可执行：

```bash
python main.py -e Exercises.txt -a MyAnswers.txt
```

程序会自动计算得分，并将结果输出到 `Grade.txt` 文件中。
输出格式示例：

```
Correct: 5 (1, 3, 5, 7, 9)
Wrong: 5 (2, 4, 6, 8, 10)
```

---

### 🧠 模块说明

#### 📄 `generator.py`

负责根据给定范围随机生成加、减、乘、除混合的合法表达式（支持带括号与分数），
并生成相应标准答案文件。

#### ⚙️ `evaluator.py`

实现对表达式的求值，支持：

* 自然数、真分数、带分数（如 `1'3/4`）
* 四则运算：`+ - × ÷`
* 括号嵌套运算

示例：

```python
evaluate_expression("2 + 1/3 × (1 + 1/2)")  # => Fraction(7, 3)
```

#### ✅ `checker.py`

负责读取题目与用户答案文件，调用 `evaluate_expression` 计算正确结果，
并使用 `format_fraction()` 对结果进行格式化比对，最后输出判分报告。

#### 🧰 `utils.py`

实现辅助功能：

* 分数化简与格式化输出

  * `Fraction(3, 2)` → `"1'1/2"`
  * `Fraction(1, 2)` → `"1/2"`
  * `Fraction(4, 1)` → `"4"`

---

### 📂 输出文件说明

| 文件名             | 内容说明      |
| --------------- | --------- |
| `Exercises.txt` | 自动生成的题目   |
| `Answers.txt`   | 系统计算的标准答案 |
| `MyAnswers.txt` | 用户提交的答案文件 |
| `Grade.txt`     | 判分统计结果    |

---

### 💡 示例流程

```bash
# 生成题目与标准答案
python main.py -n 10 -r 10

# 用户手动填写 MyAnswers.txt 后执行判分
python main.py -e Exercises.txt -a MyAnswers.txt
```

输出结果：

```
✅ 判题完成，结果已保存至 Grade.txt

Grade.txt 内容：
Correct: 7 (1, 3, 4, 5, 7, 8, 10)
Wrong: 3 (2, 6, 9)
```

---

### 🧱 依赖与运行环境

* Python ≥ 3.8
* 无需第三方库（仅使用标准库：`argparse`, `fractions`, `re`）


是否希望我帮你附上一个简单的 **示例输入输出文件（Exercises.txt / Answers.txt / MyAnswers.txt / Grade.txt）** 一起放进 README？
这样老师或同学一看就能马上运行体验。
