# RPG Assister: A program to aid in character creation and management in many RPG systems.
# Copyright (C)2019  Kylan Byrd: aviananalyst+rpgassist@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

class NumaneraCharacter:
    def __init__(self, name, descriptor, type, focus, height=None, weight=None, age=None, description=None, backstory=None,
                 inventory=None, tier=1, effort=None, xp=0, increase_capabilities=False, move_towards_perfection=False,
                 extra_effort=False, skill_training=False, other_option=True, notes=None):
        self.name = name
        self.descriptor = descriptor
        self.type = type
        self.focus = focus
        self.sentence = name + ' is a ' + descriptor + ' ' + type + ' who ' + focus
        if descriptor in ['Diruk', 'Mlox', 'Golthiar', 'Nalurus', 'Lattimor', 'Varjellen', 'Artificially Intelligent',
                          'Calramite', 'Echryni', 'Naidapt', 'Ormyrl', 'Proxima', 'Skeane', 'Octopus']:
            self.species = descriptor
        else:
            self.species = 'Human'
        self.height = height
        self.weight = weight
        self.age = age
        self.description = description
        self.backstory = backstory
        self.inventory = inventory
        self.tier = tier
        if effort:
            self.effort = effort
        else:
            self.effort = self.tier
        self.xp = xp
        self.advancement_option_number =
        self.advancement_tracker = {
            'Increase Capabilities': increase_capabilities,
            'Move Towards Perfection': move_towards_perfection,
            'Extra Effort': extra_effort,
            'Skill Training': skill_training
        }
        # TODO: Figure out how to track advancement options for tier leveling up.
        self.notes = notes  # This will be removed once the note manager is up.

    def lvlup(self):
        self.level += 1


class NumaneraIneventory:
    pass



