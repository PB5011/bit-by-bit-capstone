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

"""Facilitates mapping models to form submissions."""

from django.forms import ModelForm
from cryptotutor.models import *


class QuestionForm(ModelForm):
    """Class defining models in use by question form"""
    class Meta:
        """Class defining metadata for models in use by question form"""
        model = Question
        fields = ['StudentName','StudentName','projectLink', 'description']

class CodeForm(ModelForm):
    """Class defining models in use by code form"""
    class Meta:
        """Class defining metadata for models in use by code form"""
        #model = CodeSub
        fields = ['studentID','studentName','codeFragments']
