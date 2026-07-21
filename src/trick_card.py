import flet as ft


class TrickCard:
    def __init__(self, number, trick, page, on_completion_changed):

        self.number = number
        self.trick = trick
        self.page = page
        self.on_completion_changed = on_completion_changed

        self.is_completed = False

        self.attempt_count = ft.Text(
            "Attempts: 0/5"
        )

        self.checkboxes = []

        self.trick_title = ft.Text(
            f"{number}. {trick}",
            size=18,
            color=ft.Colors.RED
        )

        self.build_checkboxes()


    def build_checkboxes(self):

        for i in range(1, 6):

            checkbox = ft.Checkbox(
                label=str(i),
                on_change=self.update_attempts
            )

            self.checkboxes.append(checkbox)


    def update_attempts(self, e):

        completed_attempts = sum(
            1
            for box in self.checkboxes
            if box.value
        )


        self.attempt_count.value = (
            f"Attempts: {completed_attempts}/5"
        )


        if completed_attempts == 5:

            self.trick_title.color = ft.Colors.GREEN

            if not self.is_completed:
                self.is_completed = True
                self.on_completion_changed(1)


        elif completed_attempts > 0:

            self.trick_title.color = ft.Colors.YELLOW

            if self.is_completed:
                self.is_completed = False
                self.on_completion_changed(-1)


        else:

            self.trick_title.color = ft.Colors.RED

            if self.is_completed:
                self.is_completed = False
                self.on_completion_changed(-1)


        self.page.update()


    def view(self):

        return ft.Column(
            [
                self.trick_title,

                ft.Row(
                    self.checkboxes
                ),

                self.attempt_count,

                ft.Divider()
            ]
        )