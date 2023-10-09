class Teleport:
    class EventNotFoundException(Exception):
        def __init__(self, year):
            super().__init__(f"Введений рік {year} не знайдено у словнику подій !!\n")

    class EventAlreadyExists(Exception):
        def __init__(self, year):
            super().__init__(f"У введеному році {year} вже існує подія !!\n")

    class EventAlreadyVisitedException(Exception):
        def __init__(self, year):
            super().__init__(f"Ви вже відвідували {year} рік !!\n")

    __instance = None
    __visited_events = []
    __available_events = {
        1916: "Заснована корпорація 'Арасака'",
        2023: "Серпень : Голокост у Найт-Сіті. Ядерний пристрій вибухнув на об'єкті Арасака-тауер, більшість "
              "центральної частини Найт-Сіті зруйнована. Загинуло понад півмільйона людей.",
        2025: "Альт Каннінгем засновує Місто духів на руїнах Гонконгу.",
        2026: "Обмежені мережі VPN із корпоративними парками.",
        2030: "Початок реконструкції Найт-Сіті.",
        2035: "Мерева Варта намагається очистити РЕБІДС і зазнає невдачі, всі основні вузли у Старій Мережі вимкнені.",
    }

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __teleport(self, year: int) -> str:
        event = self.__available_events.get(year)

        if event is None:
            raise Teleport.EventNotFoundException(year)

        if (year, event) in self.__visited_events:
            raise Teleport.EventAlreadyVisitedException(year)

        self.__visited_events.append((year, event))

        return event

    def visit(self, years: set[int]):
        for i in years:
            try:
                event = self.__teleport(i)
                print(f"Ви відвідали {i} рік у якому: \n{event}\n")

            except Teleport.EventNotFoundException as e:
                print(e)

            except Teleport.EventAlreadyVisitedException as e:
                print(e)

    def clear_visiting_history(self):
        self.__visited_events.clear()

    def __event_exists(self, year):
        return self.__available_events.get(year) is not None

    def add_event(self, year, event_desc):
        if self.__event_exists(year):
            raise Teleport.EventAlreadyExists(year)

        self.__available_events[year] = event_desc

    def remove_event(self, year):
        if not self.__event_exists(year):
            raise Teleport.EventNotFoundException(year)

        del self.__available_events[year]
