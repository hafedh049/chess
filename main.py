from flet import *


def main(page: Page) -> None:
    ...
    gv = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            Container(
                Text(f"Item {i}"),
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1, colors.AMBER_400),
                border_radius=border_radius.all(5),
            )
        )
    page.update()


app(
    target=main,
    view=AppView.FLET_APP,
    assets_dir="./assets",
    use_color_emoji=True,
)
