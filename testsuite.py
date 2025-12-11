import unittest

from AwsomeGame import NPC, Player , Game , Coin, Timer, Score


g = Game()

npc = NPC()
npc.x = 100
npc.y = 100


for i in range(100):
    last_pos = [npc.x,npc.y]

    last_path = npc.path

    npc.movement()

    if last_path == 'north':
        assert npc.y == last_pos[1]-npc.speed
        assert npc.x == last_pos[0]
    elif last_path == 'south':
        assert npc.y == last_pos[1]+npc.speed
        assert npc.x == last_pos[0]
    elif last_path == 'east':
        assert npc.x == last_pos[0]+npc.speed
        assert npc.y == last_pos[1]
    elif last_path == 'west':
        assert npc.x == last_pos[0]-npc.speed
        assert npc.y == last_pos[1]

print("movement check worked")
