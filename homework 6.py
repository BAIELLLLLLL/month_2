class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return (
            self.live() + "\n" +
            self.earn() + "\n" +
            self.superpower() +
            "\nСоздаю светящийся стрим с лазерным шоу!"
        )


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return (
            self.live() + "\n" +
            self.viral() + "\n" +
            self.superpower() +
            "\nСнимаю вирусные тиктоки с лазерами и кибер-эффектами!"
        )


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return (
            self.live() + "\n" +
            self.earn() + "\n" +
            self.viral() +
            "\nПревращаю донаты и просмотры в магический контент!"
        )

glow = GlowStreamer()
cyborg = ViralCyborg()
mage = DonateMage()


print("GlowStreamer MRO:")
print(GlowStreamer.mro())

print("\nViralCyborg MRO:")
print(ViralCyborg.mro())

print("\nDonateMage MRO:")
print(DonateMage.mro())


print("\n--- LIVE ---")

print("GlowStreamer:")
print(glow.live())

print("\nViralCyborg:")
print(cyborg.live())

print("\nDonateMage:")
print(mage.live())


print("\n--- ULTIMATE CONTENT ---")

print("\nGlowStreamer:")
print(glow.ultimate_content())

print("\nViralCyborg:")
print(cyborg.ultimate_content())

print("\nDonateMage:")
print(mage.ultimate_content())