# Expose these functions directly at the package level so clients can import my_utilities.init_log,
# rather than import my_utilities.my_utilities.init_log.
from .my_utilities import init_log