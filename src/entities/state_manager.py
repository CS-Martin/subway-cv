class StateManager:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def change_state(self, new_state):
        self.current_state = new_state

    def handle_event(self, entity, event):
        self.current_state.handle_event(entity, event)

    def update(self, entity):
        self.current_state.update(entity)

    def draw(self, entity, screen):
        self.current_state.draw(entity, screen)
