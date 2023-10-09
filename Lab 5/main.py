from time_machine import Teleport

if __name__ == '__main__':
    Teleport().add_event(1, "Test Event")
    Teleport().visit({2023, 1, 1916})
    Teleport().remove_event(1)
    Teleport().clear_visiting_history()
    Teleport().visit({2023, 1, 1916})
