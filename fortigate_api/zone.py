"""Zone Object."""

from fortigate_api.base import Base


class Zone(Base):
    """Zone Object."""

    def __init__(self, rest):
        """Zone Object.

        ::
            :param rest: Fortigate REST API connector
            :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/system/zone/")
