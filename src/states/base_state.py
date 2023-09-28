class BaseState:
    def handle_event(self, entity, event):
        pass

    def update(self, entity):
        pass

    def draw(self, entity, screen):
        pass

    def get_rect(self, entity):
        return entity.rect
    