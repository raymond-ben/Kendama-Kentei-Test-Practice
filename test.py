import flet as ft

def main(page: ft.Page):
    page.title = "Kendama Kentei Practice"
    page.add(
        ft.Text("Hello Kendama!", size=30),
        ft.ElevatedButton("Start Practice")
    )

ft.app(target=main)

# main.py open launcher

# import flet as ft

def main(page: ft.Page):
    page.title = "Kendama Kentei Test Practice"
    page.window.width = 800
    page.window.height = 650
    page.padding = 30

    title = ft.Text(
        "Kendama Kentei Practice",
        size=32,
        weight=ft.FontWeight.BOLD,
    )

    subtitle = ft.Text(
        "Choose level and class to begin.",
        size=18,
    )

    level = ft.Dropdown(
        label="Kentei Level",
        width=300,
        options=[
            ft.dropdown.Option("Medal Challenge"),
            ft.dropdown.Option("Beginner"),
            ft.dropdown.Option("Intermediate"),
            ft.dropdown.Option("Advanced"),
        ],
    )

    kentei_class = ft.Dropdown(
        label="Class",
        width=300,
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
        ],
    )

    page.add(
        title,
        subtitle,
        ft.Divider(),
        level,
        kentei_class,
        ft.ElevatedButton("Start Practice"),
    )


ft.app(target=main)
