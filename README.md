# ESP32-CAM 物联网图像采集平台

这是一个基于 ESP32-CAM、Python 后端和 Web 网页的双人协作项目。

项目通过 ESP32-CAM 拍摄照片，将图片上传到云服务器，由后端负责接收和保存，最后通过网页查看照片。

## 一、项目目标

- 使用 ESP32-CAM 拍摄照片
- 通过 Wi-Fi 将 JPEG 图片上传到服务器
- 使用 Python 后端接收并保存图片
- 开发网页，展示照片及拍摄时间
- 使用 Nginx 和 Docker Compose 部署服务
- 实现基础日志、健康检查和故障排查
- 记录开发、部署和测试过程

## 二、技术栈

### 设备端（搭档负责）

- ESP32-CAM
- C / C++
- Arduino 框架或 ESP-IDF
- 摄像头控制
- Wi-Fi 与 HTTP 通信

### 后端、网页与部署（我负责）

- Python / Flask
- HTML / CSS / JavaScript
- Linux / Ubuntu
- Nginx
- Docker / Docker Compose
- Git / GitHub
- 日志、健康检查与服务排障

## 三、项目目录

```text
esp32-cam-iot-platform/
├── server/       # Python 后端 API
├── web/          # 网页前端
├── firmware/     # ESP32-CAM 设备端固件
├── deploy/       # Docker、Nginx 和部署配置
├── docs/         # 接口规范、设计文档和测试记录
├── .gitignore    # Git 忽略规则
└── README.md     # 项目说明
```

## 四、双方分工

### 负责人 A：后端、网页与 DevOps

- 开发图片上传接口
- 保存和管理上传的图片
- 开发照片展示网页
- 配置 Nginx 和 Docker Compose
- 将服务部署到阿里云 ECS
- 负责日志、健康检查和部署文档

### 负责人 B：硬件与嵌入式软件

- 选择并调试 ESP32-CAM 开发板
- 学习 C / C++ 和设备端开发
- 实现摄像头拍照
- 实现 Wi-Fi 连接和 HTTP 图片上传
- 处理网络异常、超时和重试
- 记录串口日志并协助联调

### 双方共同完成

- 确定设备端与服务器端的接口规范
- 使用 Git / GitHub 协作
- 完成端到端测试
- 排查并修复问题
- 整理项目文档和演示材料

## 五、计划中的 API

| 接口 | 功能 |
|---|---|
| GET /api/health | 检查后端服务状态 |
| POST /api/upload | 上传 JPEG 图片 |
| GET /api/photos | 获取照片列表 |
| GET /images/{filename} | 查看已保存的图片 |

以上接口为计划中的设计，具体请求格式和响应结构以 `docs/` 中的接口规范为准。

## 六、项目进度

- [x] 创建 GitHub 仓库
- [x] 创建基础目录结构
- [ ] 完善接口规范
- [ ] 实现后端图片上传与保存
- [ ] 实现 ESP32-CAM 拍照和上传
- [ ] 实现照片展示网页
- [ ] 完成设备与服务器联调
- [ ] 使用 Docker Compose 部署
- [ ] 完成异常测试与项目文档

## 七、安全注意事项

- 不要将 Wi-Fi 密码、服务器密码、API Token 或私钥提交到 GitHub
- 不要将 `.env` 等包含真实凭据的文件提交到仓库
- 对上传文件限制大小并校验格式
- 公网部署时配置 HTTPS 和必要的身份验证
- 照片等运行数据应保存在独立的数据目录中，不要直接提交到代码仓库

## 八、项目原则

- 先完成最小可运行版本，再逐步增加功能
- 接口先约定，再分别开发，最后联调
- 每个阶段都保留可验证的成果
- 重要配置、问题和解决方法及时记录
