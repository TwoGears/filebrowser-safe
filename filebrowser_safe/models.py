
class AdminThumbMixin(object):
    """
    Provides a thumbnail method on models for admin classes to
    reference in the ``list_display`` definition.
    """

    admin_thumb_field = None

    def admin_thumb(self):
        thumb = ""
        if self.admin_thumb_field:
            thumb = getattr(self, self.admin_thumb_field, "")
        if not thumb:
            return ""
        from mezzanine.conf import settings
        from templatetags.remote_storage_thumbnails_tags import thumbnail
        x, y = settings.ADMIN_THUMB_SIZE.split('x')
        thumb_url = thumbnail(thumb, x, y)
        return "<img src='%s%s'>" % (settings.MEDIA_URL, thumb_url)
    admin_thumb.allow_tags = True
    admin_thumb.short_description = ""
