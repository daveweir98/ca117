class File(object):
    FILE_PERMISSIONS = "rwx"

    def __init__(self, name, owner, size=0, permission=""):
        self.name = name
        self.owner = owner
        self.size = size
        self.permission = permission

    def __str__(self):
        return "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner,self.get_permissions(), self.get_size())

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

    def get_size(self):
        return self.size

    def disable_permission(self, user, mode):
        if mode not in self.FILE_PERMISSIONS:
            return

        if self.owner != user:
            print("Access denied")
            return

        if mode not in self.permission:
            return

        self.permission = self.permission.replace(mode, "")

class Folder(object):
    #d is a dictionary that maps from file names to file objects
    def __init__(self):
        self.d = {}

    def add_file(self, f):
        if f.name in self.d:
            print("File already exists")
            return
        self.d[f.name] = f

    def del_file(self, user, name):
        if name not in self.d:
            print("No such file")
            return

        if self.d[name].owner != user:
            print("Access denied")
            return
        del self.d[name]

    def get_size(self):
        return sum([f.get_size() for f in self.d.values()])

    def __str__(self):
        heading = "Folder contents"
        uline = "="*len(heading)
        slist = [heading, uline]
        for k in sorted(self.d.keys()):
            slist.append("".join(self.d[k].__str__()))
        slist.append("Folder size: {} bytes".format(self.get_size()))
        return "\n".join(slist)
