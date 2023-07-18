from pathlib import Path
from typing import Optional

from nonebot import require

from nonebot_plugin_templates.template_types import *

require("nonebot_plugin_htmlrender")
from nonebot_plugin_htmlrender import html_to_pic

from jinja2 import Environment, FileSystemLoader

TEMPLATES_PATH = Path(__file__).parent / "templates"

env = Environment(
    extensions=["jinja2.ext.loopcontrols"],
    loader=FileSystemLoader(str(Path(__file__).parent / "templates")),
    enable_async=True,
)

COLORLIST_TEMPLATE = env.get_template("colorlist.html")
MENUS_TEMPLATE = env.get_template("menus.html")
CARD_TEMPLATE = env.get_template("cards.html")

Font_Path = (TEMPLATES_PATH / "PingFang.ttf").as_uri()


async def colorlist_render(
        _list: dict,
        width: int,
        headline: str = "列表",
        description: str = "🌈列表",
        font_size: int = 15,
        font_path: str = Font_Path
) -> bytes:
    """ 函数名：colorlist_render

        功能：该函数用于生成一张带有颜色列表的图片。

        参数：
            _list: 字典类型的列表，其中键为字符串，值为颜色代码。
                {
                "line1 name":"description of line1",
                "line2 name":"description of line1"
                }
            width: 图片的宽度。
            headline: 列表的标题，默认值为"列表"。
            description: 列表的描述，默认值为"🌈列表"。
            font_size: 字体大小，默认值为15。
            font_path: 字体文件的路径，默认值为Font_Path。

        返回值:
            该函数返回彩色列表的图片bytes。
        """
    html = await COLORLIST_TEMPLATE.render_async(
        headline=headline,
        list=_list,
        description=description,
        font_path=font_path,
        font_size=font_size,
    )
    return await html_to_pic(html, viewport={"width": width, "height": 10})


async def menu_render(menus: Menus, width: int, colors: Optional[dict] = None, font_path: str = Font_Path) -> bytes:
    """
    函数：menu_render

    功能：该函数将菜单对象渲染成图片格式，以便于展示。

    参数：
    - menus: Menus对象，表示需要渲染的菜单对象。
        Menus(Menu("menu1", Funcs(Func("func1", "des1") + Func("func2", "des2")), "des of menu1") + Menu("menu2",Funcs(Func("func1","des1"))))
    - width: int类型，表示图片的宽度，单位为像素。
    - colors: 可选参数，字典类型，包含菜单渲染时使用的颜色信息。默认为None，使用内置颜色。
        {
            "html_bg": "#d9d9d9",  # 整体背景颜色
            "menu_header_bg": "#E5F3F9",  # 菜单标题和描述的背景颜色
            "grid_bg": "#ffffff",  # 命令表格背景颜色
            "func_name_pre": "#8D3C1E",  # 命令前的'#'的颜色
            "func_index_text": "#FFFFFF",  # 命令前的索引的数字的颜色
            "func_index_bg": "#8D3C1E",  # 命令前的索引的数字的圆形背景颜色
        }
    - font_path: str类型，表示字体文件的路径，默认为Font_Path。

    返回值：bytes类型，表示渲染后的图片二进制数据。
    """
    if colors is None:
        colors = {
            "html_bg": "#d9d9d9",  # 整体背景颜色
            "menu_header": "#E5F3F9",  # 菜单标题和描述的背景颜色
            "func_grid": "#ffffff",  # 命令表格背景颜色
            "func_name_pre": "#8D3C1E",  # 命令前的'#'的颜色
            "func_index_text": "#FFFFFF",  # 命令前的索引的数字的颜色
            "func_index_bg": "#8D3C1E",  # 命令前的索引的数字的圆形背景颜色
        }
    html = await MENUS_TEMPLATE.render_async(
        menus=menus.to_dict(), colors=colors, font_path=font_path
    )
    return await html_to_pic(html, viewport={"width": width, "height": 10})


async def cardlist_render(title: str, cards: Cards, subtitle: str = "", width: int = 500, colors: Optional[dict] = None,
                          font_path: str = Font_Path) -> bytes:
    """
    函数：cardlist_render

    功能：渲染一个带有标题和可选子标题的卡片列表图片。

    参数：

    title (str)：卡片列表的总标题。
    cards (Cards)：要渲染的 Card 对象的集合。可以通过将一个或多个 Card 对象添加到 Cards 对象中来创建 Cards 对象。
        Cards(Card("card1", Content(Line("line content 1", "line1 title") + Line("line content2")),Tags(Tag("tag1","while"),Tag("tag2","#ffffff"))))
        Tags是可选项,Line的title是可选项
    subtitle (str)：卡片列表的子标题（默认为 ""）。
    width (int)：卡片列表的宽度（以像素为单位）（默认为 500）。
    colors (Optional[Dict[str, str]])：一个字典，将用户定义的颜色名称映射到它们对应的十六进制代码的格式为 "#RRGGBB"。该参数是可选的，默认为 None。
                { "html": "#f3f3f3",  # 整体页面最底层的背景颜色
                  "body_border": "#ffffff",  # 最外面的边框的的背景颜色
                  "card_header": "#E5F3F9",  # 卡片的标题栏的背景颜色
                  "card-body": "#ffffff",  # 卡片主体的颜色
                  "index_text": "#FFFFFF",  # 数字索引的文本颜色
                  "index_bg": "#8D3C1E",  # 数字索引的圆形背景颜色
                  }
    font_path (str)：用于渲染文本的字体文件的路径（默认为 Font_Path）。

    返回值：

    bytes：包含卡片列表渲染图像的 bytes 对象,可直接发送。
    """
    if colors is None:
        colors = {"html": "#f3f3f3",  # 整体页面最底层的背景颜色
                  "body_border": "#ffffff",  # 最外面的边框的的背景颜色
                  "card_header": "#E5F3F9",  # 卡片的标题栏的背景颜色
                  "card-body": "#ffffff",  # 卡片主体的颜色
                  "index_text": "#FFFFFF",  # 数字索引的文本颜色
                  "index_bg": "#8D3C1E",  # 数字索引的圆形背景颜色
                  }
    html = await CARD_TEMPLATE.render_async(title=title, cards=cards.to_dict(), subtitle=subtitle, colors=colors,
                                            font_path=font_path)
    return await html_to_pic(html, viewport={"width": width, "height": 10})
