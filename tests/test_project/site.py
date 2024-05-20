from immunity_utils.admin_theme.admin import ImmunityAdminSite


class CustomAdminSite(ImmunityAdminSite):
    password_change_done_template = "password_change_done.html"
