class File(object):
    FILE_PERMISSIONS = "rwx"

    def __init__(self, name, owner, size=0, permission=""):
        self.name = name
        self.owner = owner
        self.size = size
        self.permission = permission

    def __str__(self):
        return "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner,self.get_permissions(), self.size)

    def has_access(self, user, mode):
        if mode not in self.FILE_PERMISSIONS:
            return
        if self.owner != user and mode not in self.permission:
            return "Access denied"

        else:
            return "Access granted"

    def get_permissions(self):
        if not self.permission:
            return "null"
        return "".join(sorted(self.permission))

    def enable_permission(self, user, mode):
        if mode not in self.FILE_PERMISSIONS:
            return

        if self.owner != user:
            print("Access denied")
            return

        if mode in self.permission:
            return
        self.permission += mode

    def disable_permission(self, user, mode):
        if mode not in self.FILE_PERMISSIONS:
            return

        if self.owner != user:
            print("Access denied")
            return

        if mode not in self.permission:
            return

        self.permission = self.permission.replace(mode, "")
