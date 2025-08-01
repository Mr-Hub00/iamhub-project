from rolepermissions.roles import AbstractUserRole

class Creator(AbstractUserRole):
    available_permissions = {
        'can_mint': True,
        'can_view_dashboard': True
    }

class Editor(AbstractUserRole):
    available_permissions =