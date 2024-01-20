import flet as ft
import chess

board: chess.Board = chess.Board()


def main(page: ft.Page) -> None:
    page.title = "Chess"
    page.window_center()
    page.window_height = 600
    page.window_width = 600

    page.update()

    print(board)


if __name__ == "__main__":
    ft.app(target=main, name="Chess")
