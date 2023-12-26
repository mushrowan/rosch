class Host:
	default_port = "22"
	default_user = "root"
	def __init__(self, hostname):
		self.hostname = hostname
		self.port = Host.default_port
		self.user = Host.default_user

	def set_user(self, user):
		self.user = user

	def set_port(self, port):
		self.port = port
