import flet as ft
from json import load


def main(page: ft.Page) -> None:
    page.window_resizable = False
    page.
    page.window_width = 800
    page.window_height = 600
    board = ft.GridView(
        expand=True,
        child_aspect_ratio=1,
    )

    page.add(board)

    with open("assets/chess.json", "r") as f:
        pieces: list[dict] = load(f)
        for piece in pieces:
            board.controls.append(
                ft.Container(
                    ft.Text(piece["piece"], size=18, weight=ft.FontWeight.W_500),
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
