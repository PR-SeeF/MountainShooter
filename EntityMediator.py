from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Entity):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_List: list[Entity]):
        for i in range(len(entity_List)):
            test_entity = entity_List[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_List: list[Entity]):
        for ent in entity_List:
            if ent.health <= 0:
                entity_List.remove(ent)