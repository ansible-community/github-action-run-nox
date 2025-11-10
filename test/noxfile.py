# Copyright (c) 2025 Maxwell G <maxwell@gtmx.me>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or
# https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

import nox


@nox.session
def extra_args(session: nox.Session) -> None:
    expected = ["hello"]
    if session.posargs != expected:
        session.error(f"Expected session.posargs {expected}, got {session.posargs}")
