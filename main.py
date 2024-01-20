import flet as ft
import chess

board: chess.Board = chess.Board()


def main(page: ft.Page) -> None:
    page.title = "Chess"
    page.window_center()
    page.window_height = 700
    page.window_width = 700
    page.window_resizable = False
    page.window_maximizable = False
    page.window_minimizable = False
    page.padding = 0
    page.spacing = 0

    painter: bool = True

    for row in str(board).split("\n"):
        new_row = row.split()

        row_widget: ft.Row = ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        for piece in new_row:
            row_widget.controls.append(
                ft.Container(
                    alignment=ft.Alignment(0.5, 0.5),
                    margin=0,
                    bgcolor=ft.colors.WHITE if painter else ft.colors.GREEN,
                    expand=True,
                    content=ft.Image(
                        f"assets/pieces/{'black' if piece.islower() else 'white'}/{piece}.png"
                    )
                    if piece != "."
                    else None,
                ),
            )
            painter = not painter
        page.add(row_widget)
        painter = not painter

    page.update()

    print(board)


if __name__ == "__main__":
    ft.app(target=main, name="Chess")
