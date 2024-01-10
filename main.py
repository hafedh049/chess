import flet as ft
from json import load


def main(page: ft.Page) -> None:
    board = ft.GridView(
        expand=True,
        max_extent=81,
        child_aspect_ratio=1,
    )

    page.add(board)

    with open("assets/chess.json", "r") as f:
        pieces: list[dict] = load(f)
        for piece in pieces:
            board.controls.append(
                ft.Container(
                    ft.Text(piece["piece"], size=18, weight=ft.font_weight.bold),
                    width=80,
                    height=80,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN
                    if pieces.index(piece) % 2 == 0
                    else ft.colors.WHITE,
                )
            )

    page.update()


ft.app(
    target=main,
    view=ft.AppView.FLET_APP,
    assets_dir="./assets",
    use_color_emoji=True,
)
