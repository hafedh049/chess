from flet import *


def main(page: Page) -> None:
    ...
    gv = GridView(
        expand=True,
        max_extent=150,
        child_aspect_ratio=1,
        col=8,
    )
    page.add(gv)

    for i in range(81):
        gv.controls.append(
            Container(
                Text(f"Item {i}"),
                alignment=alignment.center,
                bgcolor=colors.GREEN if i % 2 == 0 else colors.WHITE,
            )
        )
    page.update()


app(
    target=main,
    view=AppView.FLET_APP,
    assets_dir="./assets",
    use_color_emoji=True,
)
