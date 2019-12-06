import janisbot4.filters as filters

from tests.message_stub import MessageStub, Chat
from janisbot4.config import cfg


def test_a_single_id_can_be_added():
    filt = filters.ChatIdFilter(123)
    assert filt.chat_ids == [123]


def test_a_list_of_filters_can_be_added():
    filt = filters.ChatIdFilter([123, 456])
    assert filt.chat_ids == [123, 456]


def test_filter_works():
    filt = filters.ChatIdFilter(123)

    ok_message_stub = MessageStub()
    ok_message_stub.chat = Chat(123)

    filtered_message_stub = MessageStub()
    filtered_message_stub.chat = Chat(456)

    assert filt.check(ok_message_stub) is True
    assert filt.check(filtered_message_stub) is False


def test_chat_filter_can_be_loaded_from_config():
    ids = cfg.get('chat_ids')
    assert ids == ['1', '2', '3']
