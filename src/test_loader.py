from data_loader import (
    get_levels,
    get_classes,
    get_tricks
)


print("Levels:")
print(get_levels())


print("\nClasses:")
print(get_classes("Medal Challenge"))


print("\nTricks:")
print(
    get_tricks(
        "Medal Challenge",
        "3rd Class"
    )
)