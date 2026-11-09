from varasto import Varasto


def tulosta_getterit(varasto):
    print("Olut getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def kasittele_mehua(varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"Mehuvarasto: {varasto}")


def kasittele_virhetilanteet():
    print("Virhetilanteita:")

    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def tayta_olutta(varasto):
    print(f"Olutvarasto: {varasto}")
    print("olutta.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {varasto}")


def kokeile_negatiivista_lisaysta(varasto):
    print(f"Mehuvarasto: {varasto}")
    print("mehua.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {varasto}")


def tyhjenna_olutta(varasto):
    print(f"Olutvarasto: {varasto}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {varasto}")


def kokeile_negatiivista_ottoa(varasto):
    print(f"Mehuvarasto: {varasto}")
    print("mehua.ota_varastosta(-32.9)")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {varasto}")


def tulosta_luominen(mehu, olut):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")


def luo_varastot():
    return Varasto(100.0), Varasto(100.0, 20.2)


def main():
    mehua, olutta = luo_varastot()

    tulosta_luominen(mehua, olutta)
    tulosta_getterit(olutta)
    kasittele_mehua(mehua)
    kasittele_virhetilanteet()
    tayta_olutta(olutta)
    kokeile_negatiivista_lisaysta(mehua)
    tyhjenna_olutta(olutta)
    kokeile_negatiivista_ottoa(mehua)


if __name__ == "__main__":
    main()
