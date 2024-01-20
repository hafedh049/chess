import flet as ft
import chess

board: chess.Board = chess.Board()


def main(page: ft.Page) -> None:
    page.title = "Chess"
    page.window_center()
    page.window_height = 600
    page.window_width = 600

    painter: bool = True

    for row in str(board).split("\n"):
        new_row = row.split()

        print(new_row)
        row_widget : ft.Row = ft.Row()
        for piece in new_row:

            painter = not painter
         page.add(
                ft.Container(bgcolor=ft.colors.WHITE if painter else ft.colors.GREEN)
            )

    page.update()

    print(board)


if __name__ == "__main__":
    ft.app(target=main, name="Chess")
