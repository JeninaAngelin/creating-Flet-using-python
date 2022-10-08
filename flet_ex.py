import flet
from flet import IconButton, Page, Row, TextField, icons

#defining function main__
def main(p : Page):
    p.title = "...***.Numbers Counter.***..."
    p.vertical_alignment = "center"

    textNum = TextField(value="0", text_align="center", width=100)

    def minus_click(e):
        textNum.value = int(textNum.value) - 1
        p.update()

    def plus_click(e):
        textNum.value = int(textNum.value) + 1
        p.update()

    p.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                textNum,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )

#calling function and implementing in app form
flet.app(target=main)
