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
