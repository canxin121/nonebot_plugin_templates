<div align="center">
  <a href="https://github.com/canxin121">
    <img src="https://socialify.git.ci/canxin121/nonebot_plugin_templates/image?font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Fcanxin121.github.io%2Fdocs%2Flogo.png&name=1&owner=1&pattern=Charlie%20Brown&pulls=1&stargazers=1&theme=Auto" width="700" height="350">
  </a>
  <h1>Nonebot_plugin_templates</h1>
</div>

<p align="center">
    <a href="https://pypi.python.org/pypi/nonebot-plugin-templates">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-templates" alt="pypi">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/nonebot-plugin-templates" alt="python">
    <img src="https://img.shields.io/pypi/dm/nonebot-plugin-templates" alt="pypi">
    <br />
    <a href="https://onebot.dev/">
    <img src="https://img.shields.io/badge/OneBot-v11-black?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="onebot">
    <a href="https://github.com/canxin121/nonebot_poe_chat/releases/">
    <img src="https://img.shields.io/github/last-commit/canxin121/nonebot_plugin_templates" alt="github">
    </a>
</p>
<div align="left">

## 最新版本号0.1.3

# 功能:提供一些jinja2 templates渲染,并提供构建所需参数的类

> 构建一个菜单的示例

```python
from nonebot_plugin_templates.template_types import *
from nonebot_plugin_templates.templates_render import menu_render, colorlist_render

menu = Menu("私有bot", des="使用和管理自己独有的bot的命令,私有bot只有主人可使用,其他人无法使用",
            funcs=Funcs(
                Func("/bot名称+询问的问题",
                     "与指定属于自己的bot对话\n(可使用'回复'某bot最后一个答案来连续和它对话)\n(可回复'清除历史','刷新对话'来清除bot的对话记忆)") +
                Func("/所有bot",
                     "查询所有的可用的私有的bot,以获取bot名称和相关信息") +
                Func("/创建bot", "创建新的私有的bot") +
                Func("/改名bot", "更改自己的bot的名称") +
                Func("/删除bot", "删除指定自己的bot")))
menu += Menu("公有bot", des="使用和管理公有的bot的命令",
             funcs=Funcs(
                 Func("bot名称+询问的问题",
                      "与指定属于公共的bot对话\n(可使用'回复'某bot最后一个答案来连续和它对话)\n(可回复'清除历史','刷新对话'来清除bot的对话记忆)") +
                 Func("所有bot", "查询所有的可用的公共的bot,以获取bot名称和相关信息") +
                 Func("创建bot", "创建新的公用的bot") +
                 Func("改名bot", "更改公用的bot的名称") +
                 Func("删除bot", "删除指定公用的bot")))
pic_bytes = await menu_render(menu, 800)
```

![menu.png](src/menu.png)

> 构建一个卡片列表的示例