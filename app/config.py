# # -*- coding: utf-8 -*-
# import secrets
# import os
# from flask_uploads import UploadSet, ALL, IMAGES


# EXEMPT_METHODS = set(['OPTIONS'])
# CSRF_ENABLED = True
# SECRET_KEY = b'f\x99\xf9O\x1b\x06N\xe5P\xea\xb9\xe7\xbev\x15E'
# PERMANENT_SESSION_LIFETIME = 2678400
# API_SECRET = 'sBUT8dXiLn1lbng46suyE6EltSYrNDSoMwxjjyXfWW4'

# API_URL = 'http://vim-api:9002'

# # Uploads
# ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
# UPLOADED_IMAGES_DEST = os.path.join(ROOT_FOLDER, 'uploads')
# UPLOADED_LOGOS = UploadSet(
#     name='logos',
#     extensions=('jpeg', 'jpg', 'png', 'svg'),
#     default_dest=lambda app: os.path.join(app.config['UPLOADED_IMAGES_DEST'], 'logos')
# )
# UPLOADED_PLANS = UploadSet(
#     name='plans',
#     extensions=IMAGES,
#     default_dest=lambda app: os.path.join(app.config['UPLOADED_IMAGES_DEST'], 'plans')
# )
# UPLOADED_EXAMS = UploadSet(
#     name='exams',
#     extensions=ALL,
#     default_dest=lambda app: os.path.join(app.config['UPLOADED_IMAGES_DEST'], 'exams')
# )
# UPLOADED_RISKS = UploadSet(
#     name='risks',
#     extensions=('jpeg', 'jpg', 'png', 'pdf', 'csv'),
#     default_dest=lambda app: os.path.join(app.config['UPLOADED_IMAGES_DEST'], 'risks')
# )

# # Sendgrid
# MAIL_SENDGRID_API_KEY = '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'

# # Security
# SECURITY_CHANGEABLE = True
# SECURITY_CONFIRMABLE = True
# SECURITY_REGISTERABLE = True
# SECURITY_RECOVERABLE = True
# SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
# SECURITY_CHANGE_URL = '/user_password'
# SECURITY_CHANGE_PASSWORD_TEMPLATE = 'dashboard/user_password.html'
# SECURITY_EMAIL_SENDER = 'no-reply@prixtips.com'
# SECURITY_EMAIL_SUBJECT_CONFIRM = 'Por favor, confirma tu correo electrónico'
# SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = 'Tu contraseña ha sido restablecida'
# SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = 'Instrucciones de recuperación de contraseña'
# SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = 'Tu contraseña ha sido modificada'
# SECURITY_EMAIL_SUBJECT_REGISTER = 'Bienvenido a Prixtips'
# SECURITY_URL_PREFIX = '/account'
# SECURITY_POST_CHANGE_VIEW = '/account/user_password'
# SECURITY_POST_CONFIRM_VIEW = 'dashboard'
# SECURITY_POST_LOGIN_VIEW = 'dashboard.home'
# SECURITY_POST_LOGOUT_VIEW = '/account/post-logout'
# SECURITY_POST_REGISTER_VIEW = 'security.login'
# SECURITY_POST_RESET_VIEW = 'security.login'
# SECURITY_RESET_SALT = 'y2k.v1m'
# SECURITY_PASSWORD_SALT = 'y2k.v1m'
# DEFAULT_HTTP_AUTH_REALM = 'Inicio de sesión necesario'
# SECURITY_MSG_UNAUTHORIZED = (
#     'No tienes permiso para consultar este recurso.',
#     'danger'
# )
# SECURITY_MSG_CONFIRM_REGISTRATION = (
#     'Gracias. Un correo con instrucciones sobre cómo confirmar tu cuenta ha sido enviado a %(email)s.',
#     'success'
# )
# SECURITY_MSG_EMAIL_CONFIRMED = (
#     'Gracias. Tu correo electrónico ha sido confirmado.',
#     'success'
# )
# SECURITY_MSG_ALREADY_CONFIRMED = (
#     'Tu correo electrónico ya ha sido confirmado.',
#     'info'
# )
# SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = (
#     'Token de confirmación inválido.',
#     'danger'
# )
# SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = (
#     '%(email)s ya está asociado a una cuenta.',
#     'danger'
# )
# SECURITY_MSG_PASSWORD_MISMATCH = (
#     'La contraseña no coincide',
#     'danger'
# )
# SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = (
#     'Las contraseñas no coinciden',
#     'danger'
# )
# SECURITY_MSG_INVALID_REDIRECT = (
#     'Las redirecciones a sitios web externos están prohibidas',
#     'danger'
# )
# SECURITY_MSG_PASSWORD_RESET_REQUEST = (
#     'Las instrucciones para restablecer tu contraseña han sido enviadas a %(email)s.',
#     'info'
# )
# SECURITY_MSG_PASSWORD_RESET_EXPIRED = (
#     'No restableciste tu contraseña antes de %(within)s. Nuevas instrucciones han sido enviadas a %(email)s.',
#     'danger'
# )
# SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = (
#     'Token de restablecimiento de contraseña inválido.',
#     'danger'
# )
# SECURITY_MSG_CONFIRMATION_REQUIRED = (
#     'El correo electrónico requiere confirmación.',
#     'danger'
# )
# SECURITY_MSG_CONFIRMATION_REQUEST = (
#     'Las instrucciones de confirmación se han enviado a %(email)s.',
#     'info'
# )
# SECURITY_MSG_CONFIRMATION_EXPIRED = (
#     'No confirmaste tu correo electrónico antes de %(within)s. Nuevas instrucciones para confirmar tu correo electrónico han sido enviadas a %(email)s.',
#     'danger'
# )
# SECURITY_MSG_LOGIN_EXPIRED = (
#     'No iniciaste sesión antes de %(within)s. Nuevas instrucciones para iniciar sesión han sido enviadas a %(email)s.',
#     'danger'
# )
# SECURITY_MSG_LOGIN_EMAIL_SENT = (
#     'Instrucciones para iniciar sesión han sido enviadas a %(email)s.',
#     'success'
# )
# SECURITY_MSG_INVALID_LOGIN_TOKEN = (
#     'Token de inicio de sesión inválido.',
#     'danger'
# )
# SECURITY_MSG_DISABLED_ACCOUNT = (
#     'Cuenta deshabilitada.',
#     'danger'
# )
# SECURITY_MSG_EMAIL_NOT_PROVIDED = (
#     'Correo electrónico no indicado',
#     'danger'
# )
# SECURITY_MSG_INVALID_EMAIL_ADDRESS = (
#     'Dirección de correo electrónico inválida',
#     'danger'
# )
# SECURITY_MSG_PASSWORD_NOT_PROVIDED = (
#     'Contraseña no indicada',
#     'danger'
# )
# SECURITY_MSG_PASSWORD_NOT_SET = (
#     'Ninguna contraseña ha sido definida para este usuario',
#     'danger'
# )
# SECURITY_MSG_PASSWORD_INVALID_LENGTH = (
#     'La contraseña debe contar al menos con 6 caracteres',
#     'danger'
# )
# SECURITY_MSG_USER_DOES_NOT_EXIST = (
#     'El suario especificado no existe',
#     'danger'
# )
# SECURITY_MSG_INVALID_PASSWORD = (
#     'Contraseña inválida',
#     'danger'
# )
# SECURITY_MSG_FORGOT_PASSWORD = (
#     '¿Olvidaste tu contraseña?',
#     'info'
# )
# SECURITY_MSG_PASSWORD_RESET = (
#     'Has restablecido tu contraseña con éxito y tu sesión se ha iniciado automáticamente.',
#     'success'
# )
# SECURITY_MSG_PASSWORD_IS_THE_SAME = (
#     'Tu nueva contraseña debe ser diferente de la antigua.',
#     'danger'
# )
# SECURITY_MSG_PASSWORD_CHANGE = (
#     'Has cambiado tu contraseña con éxito.',
#     'success'
# )
# SECURITY_MSG_LOGIN = (
#     'Debes iniciar sesión para poder acceder a esta página.',
#     'info'
# )
# SECURITY_MSG_REFRESH = (
#     'Deber iniciar sesión nuevamente para poder acceder a esta página.',
#     'info'
# )
# PREFERRED_URL_SCHEME = 'https'
