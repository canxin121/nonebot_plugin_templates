from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="templates_render",
    description="使用htmlrender和jinja2渲染,使用构建的menu,card或dict进行模板渲染",
    usage="import 后构建相应类并进行渲染得到bytes的图片",
    extra={},
    type="library",
    homepage="https://github.com/canxin121/nonebot_plugin_templates",
)
