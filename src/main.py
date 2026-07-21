import flet as ft

from data_loader import (
    get_levels,
    get_classes,
    get_tricks
)

# Creates trick cards for each trick
# Each card contains the trick name, checkboxes for attempts, and an attempt counter

def create_trick_card(number, trick, page, on_completion_changed):

    attempt_count = ft.Text(
        "Attempts: 0/5"
    )

    boxes = []
    
    is_completed = False


    def update_attempts(e):

        nonlocal is_completed

        completed_attempts = sum(
            1 for box in boxes
            if box.value
        )

        attempt_count.value = f"Attempts: {completed_attempts}/5"

# Color logic

        if completed_attempts == 5:
            trick_title.color = ft.Colors.GREEN

            if not is_completed:
                is_completed = True
                on_completion_changed(1)
       
        elif completed_attempts > 0:
            trick_title.color = ft.Colors.YELLOW

            if is_completed:
                is_completed = False
                on_completion_changed(-1)

        else:
            trick_title.color = ft.Colors.RED
            
            if is_completed:
                is_completed = False
                on_completion_changed(-1)

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

    completed_tricks = 0
    total_tricks = 0

    def update_session_progress(change):
        nonlocal completed_tricks
        completed_tricks += change
        progress_text.value = (
            f"Completed {completed_tricks}/{total_tricks}"
        )

        if total_tricks > 0:
            progress_bar.value = completed_tricks / total_tricks

        page.update()


    progress_text = ft.Text(
        "Completed 0/0",
        size=18
    )

    progress_bar = ft.ProgressBar(
        width=500,
        value=0
    )

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

        global total_tricks, completed_tricks

        total_tricks = len(tricks)
        completed_tricks = 0

        progress_text.value = (
            f"Completed 0/{total_tricks}"
        )

        progress_bar.value = 0

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
                    page,
                    update_session_progress
                    )
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

        progress_text,

        progress_bar,

        trick_list
    )


ft.app(target=main)
