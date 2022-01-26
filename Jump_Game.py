from aerforge import*

forge = Forge(fps = 60)

player = prefabs.PlatformerController(forge, width = 20, height = 50  ,color = color.Color(50, 50, 50),jump_force = -10, walk_speed = 5)


graund = Entity(forge, width = 1200, height = 30, y = 570, x = 0)
graund_2 = Entity(forge, width = 50, height = 10, y = 504, x = 230)
graund_3 = Entity(forge, width = 50, height = 10, y = 467, x = 423)
graund_4 = Entity(forge, width = 50, height = 10, y = 437, x = 579)
graund_5 = Entity(forge, width = 50, height = 10, y = 401, x = 766)
graund_6 = Entity(forge, width = 50, height = 10, y = 310, x = 649)
graund_7 = Entity(forge, width = 50, height = 10, y = 266, x = 440)
graund_8 = Entity(forge, width = 50, height = 10, y = 230, x = 294)
graund_9 = Entity(forge, width = 50, height = 10, y = 161, x = 550)
final_graund = Entity(forge, width = 200, height = 20, y = 94, x = 768)


player.objects.append(graund)
player.objects.append(graund_2)
player.objects.append(graund_3)
player.objects.append(graund_4)
player.objects.append(graund_5)
player.objects.append(graund_6)
player.objects.append(graund_7)
player.objects.append(graund_8)
player.objects.append(graund_9)
player.objects.append(final_graund)


def update():
    pass

forge.run()
