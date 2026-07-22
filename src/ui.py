import flet as ft

from data_loader import (
    get_levels,
    get_classes,
    get_tricks
)
from trick_card import TrickCard

def build_ui(page: ft.Page):

    page.title = "Kendama Kentei Trainer"
    page.scroll = ft.ScrollMode.AUTO


    title = ft.Text(
        "Kendama Kentei Test Practice",
        size=28,
        weight=ft.FontWeight.BOLD
    )

    # Dropdowns

    level_dropdown = ft.Dropdown(
        label="Select Level",
        options=[
            ft.dropdown.Option(level)
            for level in get_levels()
        ]
    )

    class_dropdown = ft.Dropdown(
        label="Select Class",
        options=[]
    )

    trick_list = ft.Column()

    # Progress

    completed_tricks = 0
    total_tricks = 0

    progress_text = ft.Text(
        "Completed: 0/0",
        size=18
    )

    progress_bar = ft.ProgressBar(
        width=500,
        value=0
    )

    # Events
    
    def update_session_progress(change):

        nonlocal completed_tricks

        completed_tricks += change

        progress_text.value = (
            f"Completed: {completed_tricks}/{total_tricks}"
        )

        if total_tricks > 0:
            progress_bar.value = (
                completed_tricks / total_tricks
            )

        page.update()

    def level_changed(e):

        classes = get_classes(
            level_dropdown.value
        )

        print("Classes:", classes)

        class_dropdown.options = [
            ft.dropdown.Option(c)
            for c in classes
        ]

        class_dropdown.value = None
        print(class_dropdown.options)
        class_dropdown.update()

        page.update()

    level_dropdown.on_select = level_changed

    def start_practice(e):

        nonlocal total_tricks
        nonlocal completed_tricks

        print("Starting Practice")
        print(level_dropdown.value)
        print(class_dropdown.value)

        tricks = get_tricks(
            level_dropdown.value,
            class_dropdown.value
        )

        trick_list.controls.clear()

        total_tricks = len(tricks)
        completed_tricks = 0

        progress_text.value = (
            f"Completed: 0/{total_tricks}"
        )

        progress_bar.value = 0

        for number, trick in enumerate(
            tricks,
            start=1
        ):

            card = TrickCard(
                number,
                trick,
                page,
                update_session_progress
            )

            trick_list.controls.append(
                card.view()
            )

        page.update()

    start_button = ft.ElevatedButton(
        "Start Practice",
        on_click=start_practice
    )

    # Layout

    page.add(

        title,

        ft.Divider(),

        level_dropdown,

        class_dropdown,

        start_button,

        ft.Divider(),

        progress_text,

        progress_bar,

        trick_list
    )