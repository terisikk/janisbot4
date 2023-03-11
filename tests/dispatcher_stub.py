class DispatcherStub:
    called = False

    def register_message_handler(self, *args, **kwargs):
        self.called = True
