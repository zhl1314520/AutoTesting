<div align="center">
  <h1>🤖 AutoTesting</h1>
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Selenium_4-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium" />
    <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest" />
  </p>
  <p><em>Mastering Selenium 4 & Advanced Browser Automation</em></p>
</div>

<p align="center">
  <a href="#english">English</a> | <a href="#简体中文">简体中文</a>
</p>

---

<h2 id="english">English</h2>

A collection of automated testing project examples based on Python and Selenium 4, comprehensively covering WebDriver, BiDi (Bidirectional communication protocol), CDP (Chrome DevTools Protocol), and various advanced interaction APIs.

## 📁 Directory Structure

This project is clearly categorized according to the core functional modules of Selenium, including the following key directories:

- **`actions_API/`**: Advanced interaction APIs (ActionChains), including complex interaction demonstrations related to keyboard (`keyboard.py`), mouse (`mouse.py`), pen (`pen.py`), and wheel (`wheel.py`).
- **`bidi/`**: BiDi (Bidirectional communication) and CDP support introduced in Selenium 4, including advanced features such as log listening (`logging.py`), network interception (`network.py`), and script injection (`script.py`).
- **`drivers/`**: Browser driver management and configuration, including custom options (`options.py`), HTTP client configuration (`HTTP_client.py`), and remote control (`remote_webdriver.py`).
- **`elements/`**: Element location and operation, including various selectors (`locators.py`), file upload (`file_upload.py`), and element status information retrieval (`information.py`).
- **`getting-started/`**: Beginner examples, including your first Selenium script (`first_script.py`) and basic usage (`using_selenium.py`).
- **`interactions/`**: Browser-level interactions, such as alert handling (`alerts.py`), Cookie management (`cookies.py`), page navigation (`navigation.py`), printing page (`print_page.py`), and multi-window management (`windows.py`).
- **`support_features/`**: Auxiliary features, such as various expected conditions for explicit waits (`expected_conditions.py`) and dropdown list handling (`select_lists.py`).
- **`waits/`**: Implementation of page and element wait strategies (`waitstate.py`).

## 🚀 Quick Start

### 1. Environment Preparation

Make sure you have installed a Python 3.7+ environment.

### 2. Install Dependencies

In the project root directory, execute the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

**Core Dependencies**:
- `selenium==4.43.0`
- `pytest==9.0.3`
- `pytest-trio==0.8.0`

### 3. Run Test Examples

Enter the corresponding directory and run the specific Python script. For example, to run the getting-started example:

```bash
python getting-started/first_script.py
```

Or use `pytest` to run the test cases:

```bash
pytest
```

## 🛠 Tech Stack

- **Language**: Python 3
- **Core Framework**: Selenium 4
- **Testing Framework**: pytest, pytest-trio (Async testing support)
- **Features**: WebDriver, BiDi, CDP, ActionChains

## 📄 License

[MIT License](LICENSE)

---

<h2 id="简体中文">简体中文</h2>

基于 Python 和 Selenium 4 的自动化测试项目示例集合，全面覆盖了 WebDriver、BiDi (双向通信协议)、CDP (Chrome DevTools Protocol)、以及各类高级交互 API。

## 📁 目录结构

本项目按照 Selenium 的核心功能模块进行了清晰的分类，包含以下关键目录：

- **`actions_API/`**: 高级交互 API（ActionChains），包含键盘 (`keyboard.py`)、鼠标 (`mouse.py`)、触控笔 (`pen.py`) 及滚轮 (`wheel.py`) 相关的复杂交互演示。
- **`bidi/`**: Selenium 4 引入的 BiDi（双向通信）及 CDP 支持，包含日志监听 (`logging.py`)、网络拦截 (`network.py`) 和脚本注入 (`script.py`) 等高级特性。
- **`drivers/`**: 浏览器驱动管理与配置，包含自定义选项 (`options.py`)、HTTP客户端配置 (`HTTP_client.py`) 及远程控制 (`remote_webdriver.py`)。
- **`elements/`**: 元素定位与操作，包含各类选择器 (`locators.py`)、文件上传 (`file_upload.py`) 以及元素状态信息获取 (`information.py`)。
- **`getting-started/`**: 新手入门示例，包含你的第一个 Selenium 脚本 (`first_script.py`) 和基础用法 (`using_selenium.py`)。
- **`interactions/`**: 浏览器级交互，如弹窗处理 (`alerts.py`)、Cookie 管理 (`cookies.py`)、页面导航 (`navigation.py`)、打印页面 (`print_page.py`) 和多窗口管理 (`windows.py`)。
- **`support_features/`**: 辅助功能，如显式等待的各种预期条件 (`expected_conditions.py`) 和下拉列表处理 (`select_lists.py`)。
- **`waits/`**: 页面与元素等待策略的实现 (`waitstate.py`)。

## 🚀 快速开始

### 1. 环境准备

确保你已经安装了 Python 3.7+ 环境。

### 2. 安装依赖

在项目根目录下，执行以下命令安装所需依赖：

```bash
pip install -r requirements.txt
```

**核心依赖**:
- `selenium==4.43.0`
- `pytest==9.0.3`
- `pytest-trio==0.8.0`

### 3. 运行测试示例

进入对应的目录，运行具体的 Python 脚本。例如，运行入门示例：

```bash
python getting-started/first_script.py
```

或者使用 `pytest` 运行测试用例：

```bash
pytest
```

## 🛠 技术栈

- **语言**: Python 3
- **核心框架**: Selenium 4
- **测试框架**: pytest, pytest-trio (异步测试支持)
- **特性**: WebDriver, BiDi, CDP, ActionChains

## 📄 许可证

[MIT License](LICENSE)