### WRAPPERS

import functools
from sanic.exceptions import abort
from src.errors import InputError, UnauthorizedError, ForbiddenError, NotFoundError, DataConflictError, UnprocessableEntityError

#===============================================================================
### Exception Wrapper

def exception_wrapper(method):
    @functools.wraps(method)
    def f(*args, **kwargs):

        try:
            return method(*args, **kwargs)
        except (InputError, ValueError) as e:
            # db.session.rollback()
            abort(400, str(e)) if str(e) else abort(400)
        except (UnauthorizedError) as e:
            # db.session.rollback()
            abort(401, str(e)) if str(e) else abort(401)
        except (ForbiddenError) as e:
            # db.session.rollback()
            abort(403, str(e)) if str(e) else abort(403)
        except (NotFoundError) as e:
            # db.session.rollback()
            abort(404, str(e)) if str(e) else abort(404)
        except(DataConflictError) as e:
            # db.session.rollback()
            abort(409, str(e)) if str(e) else abort(409)
        except(UnprocessableEntityError) as e:
            # db.session.rollback()
            abort(422, str(e)) if str(e) else abort(422)
        except Exception as e:
            # db.session.rollback()
            abort(500, str(e)) if str(e) else abort(500)

    return f
