from __future__ import absolute_import

from .pie_slice import apply_changes_to_python_environment
apply_changes_to_python_environment()

from isort.main import main  # noqa: E402

main()
