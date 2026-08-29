# The Summer Kitten

这是一个使用 Hexo + Butterfly 搭建的静态博客，部署在 GitHub Pages 上。

线上地址：

https://thesummerkitten.github.io/TheSummerKitten/

## 项目结构

```text
.
├── source/
│   ├── _posts/          # 博客文章目录
│   ├── img/             # 图片、头像、站点 icon 等静态资源
│   ├── css/custom.css   # 自定义样式
│   └── index.md         # 首页内容
├── _config.yml          # Hexo 主配置
├── _config.butterfly.yml # Butterfly 主题配置
├── package.json         # npm 脚本和依赖
└── .github/workflows/   # GitHub Pages 自动部署配置
```

## 本地预览

首次拉取项目后，先安装依赖：

```powershell
npm install
```

启动本地预览：

```powershell
npm run server
```

然后访问：

```text
http://localhost:4000/
```

如果页面没有更新，可以先清理再启动：

```powershell
npm run clean
npm run server
```

## 新增文章

使用 Hexo 命令创建新文章：

```powershell
npx hexo new "文章标题"
```

文章会生成在：

```text
source/_posts/
```

文章示例：

```markdown
---
title: 文章标题
date: 2026-05-24 12:00:00
tags:
  - 日记
---

这里开始写正文。
```

如果文章是繁体中文，可以用仓库里的 OpenCC 脚本转成简体中文：

```powershell
python .\scripts\opencc_convert.py "source/_posts/2026/07/xxxx.md"
```

默认会生成一个新文件，例如：

```text
source/_posts/2026/07/xxxx-简体.md
```

常用参数：

```powershell
python .\scripts\opencc_convert.py source/_posts
python .\scripts\opencc_convert.py "source/_posts/2026/07/xxxx.md" --in-place
python .\scripts\opencc_convert.py "source/_posts/2026/07/xxxx.md" -c tw2s
```

说明：

- `source/_posts`：批量转换整个文章目录下的 Markdown 文件
- `--in-place`：直接覆盖原文件，谨慎使用
- `-c tw2s`：适合台湾繁体到简体的转换
- 默认配置是 `t2s`，适合大多数繁体中文内容

## 修改首页

首页内容在：

```text
source/index.md
```

如果暂时没有文章，也可以保留这个文件，避免博客首页为空时出现 404。

## 图片资源

图片建议放在：

```text
source/img/
```

例如：

```text
source/img/Avatar.jpg
source/img/site.ico
source/img/default-cover.jpg
```

在 Butterfly 配置里引用图片时，通常写：

```yaml
avatar:
  img: /img/Avatar.jpg
```

不要写成：

```yaml
avatar:
  img: /TheSummerKitten/img/Avatar.jpg
```

因为 Hexo 会根据 `_config.yml` 里的 `root: /TheSummerKitten/` 自动补上项目路径。

注意：GitHub Pages 对文件名大小写敏感，`Avatar.jpg` 和 `avatar.jpg` 是不同文件。

## 修改主题样式

Butterfly 主题配置在：

```text
_config.butterfly.yml
```

常用修改项包括：

```yaml
menu:          # 顶部菜单
favicon:      # 站点 icon
avatar:       # 作者头像
default_top_img:
index_img:
background:
subtitle:
aside:
theme_color:
```

自定义 CSS 在：

```text
source/css/custom.css
```

适合放颜色、圆角、阴影、间距等个性化样式。

## Live2D 看板娘

当前项目使用 `hexo-helper-live2d` 接入 Live2D，看板娘配置在：

```text
_config.yml
```

配置段落：

```yaml
live2d:
  enable: true
  model:
    use: live2d-widget-model-koharu
```

当前使用的本地模型是：

```text
source/live2d/yuri/model.json
```

项目里还包含另一个本地模型：

```text
source/live2d/snow_miku/model.json
```

如果要切换模型，修改 `_config.yml` 里的 `model.use`：

```yaml
live2d:
  model:
    use: /TheSummerKitten/live2d/snow_miku/model.json
```

注意：这里写完整的 `/TheSummerKitten/live2d/...` 路径，是为了适配 GitHub Pages 项目站点路径。

如果要更换 npm 公开模型，也可以安装模型包：

```powershell
npm install live2d-widget-model-shizuku --save
```

然后把 `_config.yml` 里的模型名改成：

```yaml
live2d:
  model:
    use: live2d-widget-model-shizuku
```

常见公开模型包包括：

```text
live2d-widget-model-koharu
live2d-widget-model-shizuku
live2d-widget-model-wanko
live2d-widget-model-haru
live2d-widget-model-hijiki
live2d-widget-model-miku
live2d-widget-model-tororo
live2d-widget-model-z16
```

如果使用自己的 Live2D 模型，需要提供完整模型文件夹，通常包含：

```text
model.json 或 model3.json
贴图文件
动作文件
表情文件
物理配置文件
```

注意不要只提供 `model.json` 或 `model3.json`，它们只是入口配置，里面引用到的贴图、动作、物理文件也必须一起提供。

## 构建项目

本地生成静态文件：

```powershell
npm run clean
npm run build
```

生成结果会在：

```text
public/
```

`public/` 是构建产物，不需要提交到 Git。

## 发布到 GitHub Pages

修改文章、图片或配置后，执行：

```powershell
git status
git add .
git commit -m "Update blog"
git push
```

推送到 `main` 分支后，GitHub Actions 会自动构建并发布到 GitHub Pages。

可以在这里查看部署状态：

https://github.com/TheSummerKitten/TheSummerKitten/actions

部署成功后访问：

https://thesummerkitten.github.io/TheSummerKitten/

## 常用命令

```powershell
npm run server   # 本地预览
npm run clean    # 清理缓存和构建产物
npm run build    # 生成静态网站
npx hexo new "文章标题" # 新建文章
```

## 常见问题

### 线上图片不显示

检查图片是否放在 `source/img/` 下，并确认配置中的文件名大小写完全一致。

### 首页显示 404

确认是否存在：

```text
source/index.md
```

如果没有文章，并且首页文件也不存在，构建后可能不会生成 `index.html`。

### GitHub Pages 没更新

先检查 GitHub Actions 是否成功：

```text
https://github.com/TheSummerKitten/TheSummerKitten/actions
```

如果 Actions 成功但页面暂时没变，等几十秒后刷新浏览器。

### 修改主题后没有生效

尝试重新清理并构建：

```powershell
npm run clean
npm run build
```
