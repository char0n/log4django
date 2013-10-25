from .settings import CONNECTION_NAME


class Log4DjangoRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'log4django':
            return CONNECTION_NAME
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'log4django':
            return CONNECTION_NAME
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'log4django' or obj2._meta.app_label == 'log4django':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == CONNECTION_NAME and model._meta.app_label == 'log4django':
            return True
        return None