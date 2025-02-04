#
#
#

from .base import Record
from .chunked import _ChunkedValue, _ChunkedValuesMixin


class SpfRecord(_ChunkedValuesMixin, Record):
    _type = 'SPF'
    _value_type = _ChunkedValue

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log.warning(
            'The SPF record type is DEPRECATED in favor of TXT values and will become an ValidationError in 2.0'
        )


Record.register_type(SpfRecord)
