from events.daointerface.baseinterface import BaseDaoInterface
from events.models.host import Host


class HostDaoInterface(BaseDaoInterface):

    model = Host
