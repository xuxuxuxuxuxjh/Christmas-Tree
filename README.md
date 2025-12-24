# 🎄 Christmas Tree - 3D 交互式圣诞树

一个使用 Three.js 和 MediaPipe 手势识别技术构建的交互式 3D 圣诞树项目。支持手势控制、照片上传、音乐播放等功能。

## 🎬 演示视频

![演示 GIF](sample.gif)

**[📹 点击观看完整演示视频](sample.mp4)**

<details>
<summary>📥 如果视频无法播放，点击这里下载</summary>

[下载 sample.mp4](sample.mp4)

</details>

> 💡 **提示**：上方 GIF 为项目预览，点击链接可观看完整高清视频。GitHub 会自动识别视频文件并提供在线播放功能。

## ✨ 功能特性

### Simple 版本
- 🌲 **3D 圣诞树渲染**：使用 Three.js 构建精美的 3D 圣诞树
- 👋 **手势识别交互**：通过 MediaPipe 实现手势控制
  - 无手势：显示圣诞树
  - 捏合手势：查看照片
  - 释放手势：散落照片
- 📸 **批量照片上传**：支持一次性上传多张照片作为装饰
- 🎨 **精美 UI 设计**：金色主题，玻璃态效果

### Complex 版本
- 🎵 **背景音乐播放**：内置《Jingle Bells》音乐
- 🎁 **礼物装饰**：支持自定义礼物图片
- 🔧 **图片处理工具**：提供 Python 脚本批量处理图片为 Base64 编码

## 📁 项目结构

```
Christmas-Tree/
├── Simple/                    # 简单版本
│   └── christmas_tree.html   # 基础交互式圣诞树
├── Complex/                  # 复杂版本
│   ├── christmas_tree.html   # 完整功能版本
│   ├── Jingle_Bells.mp3      # 背景音乐
│   ├── process.py            # 图片处理脚本
│   └── gift_images_code.txt  # 礼物图片代码（Base64）
├── sample.mp4                # 项目演示视频（完整版）
├── sample.gif                # 项目演示 GIF（预览版）
├── convert_to_gif.py         # 视频转 GIF 工具脚本
└── README.md                 # 项目说明文档
```

## 🚀 快速开始

### 方法一：直接打开（推荐）

1. 克隆或下载本项目
2. 选择你想要的版本：
   - **Simple 版本**：打开 `Simple/christmas_tree.html`
   - **Complex 版本**：打开 `Complex/christmas_tree.html`
3. 在浏览器中打开 HTML 文件即可使用

### 方法二：使用本地服务器

```bash
# 使用 Python 启动本地服务器
cd Christmas-Tree
python -m http.server 8000

# 然后在浏览器中访问
# http://localhost:8000/Simple/christmas_tree.html
# 或
# http://localhost:8000/Complex/christmas_tree.html
```

## 🎮 使用说明

### 基本操作

1. **上传照片**：
   - 点击 "ADD MEMORIES (BATCH)" 按钮
   - 选择多张照片（支持 JPG、PNG 等格式）
   - 照片会自动添加到圣诞树上

2. **手势控制**：
   - **无手势**：正常显示圣诞树
   - **捏合手势**：将手靠近摄像头并做出捏合动作，可以查看照片
   - **释放手势**：松开手，照片会散落

3. **音乐控制**（Complex 版本）：
   - 点击左下角的音乐按钮可以播放/暂停背景音乐

### 自定义礼物图片（Complex 版本）

1. 准备你的礼物图片，放在 `Complex/yao/` 目录下
2. 运行图片处理脚本：
   ```bash
   cd Complex
   python process.py
   ```
3. 脚本会生成 `gift_images_code.txt` 文件
4. 打开 `christmas_tree.html`，找到 `GIFT_IMAGES` 数组（约第85-94行）
5. 将 `gift_images_code.txt` 中的内容替换到该数组
6. 保存后即可使用自定义礼物图片

## 🛠️ 技术栈

- **Three.js**：3D 图形渲染
- **MediaPipe Tasks Vision**：手势识别
- **WebGL**：硬件加速渲染
- **HTML5/CSS3**：界面和样式
- **Python**：图片处理工具

## 📋 系统要求

- 现代浏览器（Chrome、Firefox、Edge、Safari 等）
- 支持 WebGL 的显卡
- 摄像头（用于手势识别）
- 网络连接（首次加载需要下载 CDN 资源）

## 🎨 特色功能

- ✨ **实时手势识别**：无需额外设备，使用摄像头即可控制
- 🎭 **沉浸式体验**：精美的 UI 设计和流畅的动画效果
- 📱 **响应式设计**：支持桌面和移动设备
- 🎁 **个性化定制**：可以上传自己的照片和礼物图片

## 📝 注意事项

1. **摄像头权限**：首次使用时需要允许浏览器访问摄像头
2. **网络连接**：项目使用 CDN 加载 Three.js 和 MediaPipe，需要网络连接
3. **浏览器兼容性**：建议使用最新版本的 Chrome 或 Edge 浏览器以获得最佳体验
4. **性能优化**：如果照片过多可能影响性能，建议适量上传

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证。

## 🎄 节日快乐！

祝大家圣诞快乐，新年快乐！🎅🎁❄️
