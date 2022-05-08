# CryptoTutor - A question and answer forum with code comparison capabilities.
# Copyright (C) 2022 Zoe Larson, Maya Lentsch, Tyler Bauer, Daniel Brinkman

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Registers models with the Django administration interface."""

from django.contrib import admin
from .models import *

admin.site.register(CodeSubmission)
admin.site.register(Question)
admin.site.register(Responses)

# admin.site.register(inheritedQuestion)
# admin.site.register(student)
# admin.site.register(inheritedUser)
# admin.site.register(keywords)
# admin.site.register(Notifications)
# admin.site.register(Requests)