class Stanok:
    def __init__(self, proizvoditelnost, stoimost, srednyaya_tsena_detali):
        self.proizvoditelnost = proizvoditelnost
        self.stoimost = stoimost
        self.srednyaya_tsena_detali = srednyaya_tsena_detali

    def kolichestvo_detalei_dlya_okupaemosti(self):
        return self.stoimost / self.srednyaya_tsena_detali


class FrezernyStanok(Stanok):
    def __init__(self, proizvoditelnost, stoimost, srednyaya_tsena_detali, tip_instrumenta):
        super().__init__(proizvoditelnost, stoimost, srednyaya_tsena_detali)
        self.tip_instrumenta = tip_instrumenta

    def vremya_okupaemosti(self):
        return self.kolichestvo_detalei_dlya_okupaemosti() / self.proizvoditelnost


class StanokChPU(Stanok):
    def __init__(self, proizvoditelnost, stoimost, srednyaya_tsena_detali, uroven_tochnosti):
        super().__init__(proizvoditelnost, stoimost, srednyaya_tsena_detali)
        self.uroven_tochnosti = uroven_tochnosti

    def vremya_okupaemosti(self):
        return self.kolichestvo_detalei_dlya_okupaemosti() / self.proizvoditelnost


if __name__ == "__main__":
    frezerny_stanok = FrezernyStanok(proizvoditelnost=100, stoimost=50000, srednyaya_tsena_detali=50, tip_instrumenta="Сверло")
    print("=== Фрезерный станок ===")
    print("Количество деталей для окупаемости:", frezerny_stanok.kolichestvo_detalei_dlya_okupaemosti())
    print("Время окупаемости (в часах):", frezerny_stanok.vremya_okupaemosti())

    stanok_chpu = StanokChPU(proizvoditelnost=150, stoimost=100000, srednyaya_tsena_detali=75, uroven_tochnosti="Высокая")
    print("\n=== Станок с ЧПУ ===")
    print("Количество деталей для окупаемости:", stanok_chpu.kolichestvo_detalei_dlya_okupaemosti())
    print("Время окупаемости (в часах):", stanok_chpu.vremya_okupaemosti())
