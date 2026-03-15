# ComfyUI PromptSE 节点 (中文)

一个为 ComfyUI 设计的功能强大的自定义节点，旨在彻底改变你管理和组合提示词的方式。它通过支持权重调整、词库辅助、拖拽排序和全局设置等高级功能，将提示词工程（Prompt Engineering）的效率和灵活性提升到一个新的水平。

## ✨ 功能特点

-   **条目化管理**: 轻松增加、删除、编辑和启用/禁用多个提示词条目。
-   **精准权重控制**: 为每个条目快速增减权重，自动生成 `(prompt:weight)` 格式。
-   **集成式词库**:
    -   一键导入 `.txt` 格式的自定义词库。
    -   实时搜索词条（支持英文和中文）。
    -   点击标签即可将词条追加到当前提示词。
    -   在编辑器内快速创建和添加新词条。
-   **直观拖拽排序**: 通过拖拽操作，自由调整提示词条目的顺序和优先级。
-   **全局连接符**: 自定义多个提示词之间的连接符，如 `, `、`\n` (换行) 或 ` | `。
-   **S/M 模式切换**: 在“单个模式”（仅输出选中的第一个条目）和“多个模式”（输出所有启用的条目）之间自由切换。
-   **响应式 UI**: 节点界面会根据节点宽度自动调整布局，确保在任何尺寸下都有良好的用户体验。
-   **数据持久化**: 所有设置、条目和词库都会随 ComfyUI 工作流一起保存和加载，无需重复配置。

## 🚀 安装方法

1.  将项目文件放置到你的 ComfyUI 自定义节点目录中，通常是：
    ```bash
    ComfyUI/custom_nodes/PromptSE/
    ```
    你需要确保 `__init__.py`, `nodes.py`, 和 `js/promptse_node.js` 文件都在这个目录中。
2.  重启 ComfyUI。
3.  在节点搜索框中输入 "PromptSE"，即可找到并使用本节点。

## 📚 使用方法

### LTX 2.3 默认提示词模板

仓库提供了 `ltx2.3_default_prompt.json`，可直接作为 PromptSE 的默认数据模板导入/粘贴使用。该模板按镜头类型、主体动作、场景氛围、相机运动、风格与避免项进行分段，适合作为 LTX 2.3 的起步提示词结构。

1.  **基础操作**:
    *   从节点菜单中添加 "PromptSE" 节点。
    *   使用节点底部的 `+` 和 `-` 按钮来增加或移除条目。
    *   点击条目左侧的复选框来启用或禁用它。
    *   点击条目本身（非复选框区域）打开编辑器。

2.  **编辑条目**:
    *   在编辑弹窗中，修改**标题**（仅用于UI显示）和**提示词内容**。
    *   使用 "Weight:" 旁边的 `+` / `-` 按钮调整权重。
    *   **使用词库**:
        *   点击 "Import .txt Lexicon" 导入词库文件。
        *   在 "Search tags..." 中搜索，点击结果标签即可追加到内容中。
        *   在 "Create New Lexicon Entry" 区域创建新词条。
    *   点击 "Save" 保存更改。

3.  **高级功能**:
    *   **拖拽排序**: 在主界面按住条目并上下拖动即可排序。
    *   **全局设置**: 点击左下角的 `⚙️` 按钮修改全局连接符。
    *   **S/M 模式**: 点击右下角的 "Mode: M/S" 按钮切换输出模式。

## 📄 词库文件格式

词库应为 UTF-8 编码的 `.txt` 文件。每行代表一个词条，格式为 `英文提示词,中文译名` 或 `英文提示词 中文译名`。

**示例 (`my_lexicon.txt`)**:
```
1boy,a boy
masterpiece,杰作
best quality,最高质量
solo,单人
```

## 🛠️ 技术架构

本项目旨在提供一个专业且高度可扩展的提示词管理工具，其技术架构遵循现代化和模块化的设计原则。

-   **后端**: 基于 Python 和 ComfyUI 的节点框架，负责处理最终的字符串逻辑和数据I/O。
-   **前端**: 使用原生 JavaScript ES6+，无任何外部框架依赖，确保了轻量和高性能。UI采用模块化设计，分为头部工具栏、条目列表、条目编辑器、词库面板和设置面板等组件，便于维护和扩展。
-   **数据结构**: 节点的所有状态（包括条目、设置、词库）被序列化为一个单一的JSON对象，存储在widget值中。这确保了与 ComfyUI 工作流保存/加载系统的完美兼容性。
    ```json
    {
      "entries": [
        { "id": "uuid", "title": "...", "content": "...", "enabled": true, "weight": 1.0 }
      ],
      "settings": { "connector": ", ", "mode": "M" },
      "lexicon": [
        { "english": "...", "chinese": "..." }
      ]
    }
    ```

## 🗺️ 项目蓝图 (Roadmap)

我们致力于持续改进 PromptSE 节点，未来的开发计划包括：

-   [ ] **高级设置面板**: 提供更多自定义选项，如权重格式、UI主题、导入/导出配置等。
-   [ ] **性能优化**: 针对超大量词库和条目列表进行虚拟滚动和搜索优化。
-   [ ] **用户体验增强**: 增加更多动画过渡效果、键盘快捷键和更完善的错误处理机制。
-   [ ] **兼容性测试**: 确保在不同版本的 ComfyUI 上都能稳定运行。

## ❤️ 贡献

我们欢迎任何形式的贡献！无论是提交 Issue 来报告错误、提出功能建议，还是通过 Pull Request 来直接改进代码，都对我们非常有帮助。

## 📜 许可证

本项目遵循与 ComfyUI 相同的许可证。

---

# ComfyUI PromptSE Node (English)

A powerful custom node for ComfyUI, designed to revolutionize the way you manage and compose prompts. It elevates the efficiency and flexibility of Prompt Engineering to a new level by supporting advanced features like weight adjustment, lexicon assistance, drag-and-drop sorting, and global settings.

## ✨ Features

-   **Itemized Management**: Easily add, delete, edit, and enable/disable multiple prompt entries.
-   **Precise Weight Control**: Quickly increase or decrease the weight for each entry, automatically formatted as `(prompt:weight)`.
-   **Integrated Lexicon**:
    -   One-click import of custom lexicons in `.txt` format.
    -   Real-time search for entries (supports both English and Chinese).
    -   Click a tag to append its content to the current prompt.
    -   Quickly create and add new lexicon entries directly within the editor.
-   **Intuitive Drag-and-Drop Sorting**: Freely adjust the order and priority of prompt entries with drag-and-drop operations.
-   **Global Connector**: Customize the separator used between multiple prompts, such as `, `, `\n` (newline), or ` | `.
-   **S/M Mode Toggle**: Switch freely between "Single Mode" (outputs only the first enabled entry) and "Multiple Mode" (outputs all enabled entries).
-   **Responsive UI**: The node's interface automatically adjusts its layout based on the node's width, ensuring a great user experience at any size.
-   **Data Persistence**: All settings, entries, and the lexicon are saved and loaded with the ComfyUI workflow, eliminating the need for repeated configuration.

## 🚀 Installation

1.  Place the project files into your ComfyUI custom nodes directory, which is typically:
    ```bash
    ComfyUI/custom_nodes/PromptSE/
    ```
    You need to ensure that `__init__.py`, `nodes.py`, and `js/promptse_node.js` are all in this directory.
2.  Restart ComfyUI.
3.  Search for "PromptSE" in the node search box to find and use the node.

## 📚 How to Use

### LTX 2.3 Default Prompt Template

The repository includes `ltx2.3_default_prompt.json`, which can be directly imported/pasted as PromptSE default data. The template is organized by shot type, subject/action, scene/mood, camera motion, visual style, and avoid terms as a practical starting structure for LTX 2.3 prompting.

1.  **Basic Operations**:
    *   Add the "PromptSE" node from the node menu.
    *   Use the `+` and `-` buttons at the bottom of the node to add or remove entries.
    *   Click the checkbox on the left of an entry to enable or disable it.
    *   Click the entry itself (not the checkbox area) to open the editor.
2.  **Editing an Entry**:
    *   In the editor popup, modify the **Title** (for UI display only) and the **Prompt Content**.
    *   Use the `+` / `-` buttons next to "Weight:" to adjust the weight.
    *   **Using the Lexicon**:
        *   Click "Import .txt Lexicon" to import a lexicon file.
        *   Search in "Search tags...", and click a resulting tag to append it to the content.
        *   Create new entries in the "Create New Lexicon Entry" area.
    *   Click "Save" to save your changes.
3.  **Advanced Features**:
    *   **Drag-and-Drop Sorting**: Press and hold an entry in the main interface and drag it up or down to reorder.
    *   **Global Settings**: Click the `⚙️` button in the lower-left corner to change the global connector.
    *   **S/M Mode**: Click the "Mode: M/S" button in the lower-right corner to toggle the output mode.

## 📄 Lexicon File Format

The lexicon should be a UTF-8 encoded `.txt` file. Each line represents an entry, formatted as `prompt_text,translation_or_description`.

**Example (`my_lexicon.txt`)**:
```
1boy,a boy
masterpiece,杰作
best quality,最高质量
solo,单人
```

## 🛠️ Technical Architecture

This project aims to provide a professional and highly extensible prompt management tool, with a technical architecture that follows modern and modular design principles.

-   **Backend**: Based on Python and the ComfyUI node framework, responsible for handling the final string logic and data I/O.
-   **Frontend**: Built with native JavaScript (ES6+), with no external framework dependencies, ensuring it is lightweight and high-performance. The UI is modular, divided into components like a header toolbar, entry list, entry editor, lexicon panel, and settings panel for easy maintenance and extension.
-   **Data Structure**: The entire state of the node (including entries, settings, and lexicon) is serialized into a single JSON object and stored in the widget's value. This ensures perfect compatibility with the ComfyUI workflow save/load system.
    ```json
    {
      "entries": [
        { "id": "uuid", "title": "...", "content": "...", "enabled": true, "weight": 1.0 }
      ],
      "settings": { "connector": ", ", "mode": "M" },
      "lexicon": [
        { "english": "...", "chinese": "..." }
      ]
    }
    ```

## 🗺️ Roadmap

We are committed to the continuous improvement of the PromptSE node. Future development plans include:

-   [ ] **Advanced Settings Panel**: To provide more customization options, such as weight formatting, UI themes, and configuration import/export.
-   [ ] **Performance Optimization**: Implementing virtual scrolling and search optimization for very large lexicons and entry lists.
-   [ ] **UX Enhancements**: Adding more animations, transition effects, keyboard shortcuts, and a more robust error-handling mechanism.
-   [ ] **Compatibility Testing**: Ensuring stable operation across different versions of ComfyUI.

## ❤️ Contributing

We welcome contributions of all forms! Whether it's submitting an issue to report a bug, suggesting a new feature, or improving the code directly through a pull request, your help is greatly appreciated.

## 📜 License

This project is licensed under the same license as ComfyUI.
