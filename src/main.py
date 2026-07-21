import flet as ft

from data_loader import (
    get_levels,
    get_classes,
    get_tricks
)

# Creates trick cards for each trick
# Each card contains the trick name, checkboxes for attempts, and an attempt counter
def create_trick_card(number, trick, page):

    attempt_count = ft.Text(
        "Attempts: 0/5"
    )

    boxes = []


    def update_attempts(e):

        completed = sum(
            1 for box in boxes
            if box.value
        )

        attempt_count.value = f"Attempts: {completed}/5"

        if completed == 5:
            trick_title.color = ft.Colors.GREEN
        elif completed > 0:
            trick_title.color = ft.Colors.ORANGE
        else:
            trick_title.color = ft.Colors.RED

        page.update()


    for i in range(1, 6):

        box = ft.Checkbox(
            label=str(i)
        )

        box.on_change = update_attempts

        boxes.append(box)

    trick_title = ft.Text(
        f"{number}. {trick}",
        size=18,
        color=ft.Colors.RED
    )

    return ft.Column(
        [
            trick_title,

            ft.Row(boxes),

            attempt_count,

            ft.Divider()
        ]
    )

def main(page: ft.Page):

    page.title = "Kendama Kentei Practice"
    page.window.width = 800
    page.window.height = 700
    page.padding = 30

    # -----------------------
    # Data
    # -----------------------

    levels = get_levels()

    print("Available levels:", levels)

    # -----------------------
    # UI Elements
    # -----------------------

    class_dropdown = ft.Dropdown(
        label="Class",
        width=300,
    )

    trick_list = ft.Column()


    # -----------------------
    # Events
    # -----------------------

    def level_changed(e):

        selected_level = e.control.value

        print("Selected level:", selected_level)

        classes = get_classes(selected_level)

        print("Classes found:", classes)

        class_dropdown.options = [
            ft.dropdown.Option(c)
            for c in classes
        ]

        class_dropdown.value = None

        page.update()


    def start_practice(e):

        selected_level = level_dropdown.value
        selected_class = class_dropdown.value

        print("Starting practice:")
        print(selected_level)
        print(selected_class)

        tricks = get_tricks(
            selected_level,
            selected_class
        )

        trick_list.controls.clear()

        trick_list.controls.append(
            ft.Text(
                f"{selected_level} - {selected_class}",
                size=24,
                weight=ft.FontWeight.BOLD
            )
        )

        for number, trick in enumerate(tricks, start=1):

            trick_list.controls.append(
                create_trick_card(
                    number,
                    trick,
                    page)
            )



        page.update()


    # -----------------------
    # Dropdowns
    # -----------------------

    level_dropdown = ft.Dropdown(
        label="Test",
        width=300,
        hint_text="Select a test",
        options=[
            ft.dropdown.Option(level)
            for level in levels
        ],
    )

    level_dropdown.on_select = level_changed


    # -----------------------
    # Layout
    # -----------------------

    page.add(

        ft.Text(
            "Kendama Kentei Practice",
            size=32,
            weight=ft.FontWeight.BOLD
        ),

        ft.Divider(),

        level_dropdown,

        class_dropdown,

        ft.ElevatedButton(
            "Start Practice",
            on_click=start_practice
        ),

        ft.Divider(),

        trick_list
    )


ft.app(target=main)
