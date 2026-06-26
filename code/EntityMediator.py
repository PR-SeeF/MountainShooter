import self

from code.Const import WINDOW_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Entity):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.right >= WINDOW_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_Collision = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_Collision = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_Collision = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_Collision = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_Collision = True

        if valid_Collision == True:
            if (ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent2.last_damage = ent1.name
                ent1.last_damage = ent2.name




    @staticmethod
    def verify_collision(entity_List: list[Entity]):
        for i in range(len(entity_List)):
            test_entity1 = entity_List[i]
            EntityMediator.__verify_collision_window(test_entity1)
            for j in range(i + 1, len(entity_List)):
                test_entity2 = entity_List[j]
                EntityMediator.__verify_collision_entity(test_entity1, test_entity2)

    @staticmethod
    def verify_health(entity_List: list[Entity]):
        for ent in entity_List:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__score(ent, entity_List)
                entity_List.remove(ent)
    @staticmethod
    def __score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_damage == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_damage == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score