# -*- coding:utf-8 -*-
## src/common/pep.py
##
## Copyright (C) 2007 Piotr Gaczkowski <doomhammerng AT gmail.com>
## Copyright (C) 2007-2012 Yann Leboulanger <asterix AT lagaule.org>
## Copyright (C) 2008 Brendan Taylor <whateley AT gmail.com>
##                    Jean-Marie Traissard <jim AT lapin.org>
##                    Jonathan Schleifer <js-common.gajim AT webkeks.org>
##                    Stephan Erb <steve-e AT h3c.de>
##
## This file is part of Gajim.
##
## Gajim is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published
## by the Free Software Foundation; version 3 only.
##
## Gajim is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Gajim. If not, see <http://www.gnu.org/licenses/>.
##
from gettext import gettext as _

MOODS = {
        'afraid':                       _('Afraid'),
        'amazed':                       _('Amazed'),
        'amorous':                      _('Amorous'),
        'angry':                                _('Angry'),
        'annoyed':                      _('Annoyed'),
        'anxious':                      _('Anxious'),
        'aroused':                      _('Aroused'),
        'ashamed':                      _('Ashamed'),
        'bored':                                _('Bored'),
        'brave':                                _('Brave'),
        'calm':                         _('Calm'),
        'cautious':                     _('Cautious'),
        'cold':                         _('Cold'),
        'confident':            _('Confident'),
        'confused':                     _('Confused'),
        'contemplative':        _('Contemplative'),
        'contented':            _('Contented'),
        'cranky':                       _('Cranky'),
        'crazy':                                _('Crazy'),
        'creative':                     _('Creative'),
        'curious':                      _('Curious'),
        'dejected':                     _('Dejected'),
        'depressed':            _('Depressed'),
        'disappointed': _('Disappointed'),
        'disgusted':            _('Disgusted'),
        'dismayed':                     _('Dismayed'),
        'distracted':           _('Distracted'),
        'embarrassed':          _('Embarrassed'),
        'envious':                      _('Envious'),
        'excited':                      _('Excited'),
        'flirtatious':          _('Flirtatious'),
        'frustrated':           _('Frustrated'),
        'grateful':                     _('Grateful'),
        'grieving':                     _('Grieving'),
        'grumpy':                       _('Grumpy'),
        'guilty':                       _('Guilty'),
        'happy':                                _('Happy'),
        'hopeful':                      _('Hopeful'),
        'hot':                          _('Hot'),
        'humbled':                      _('Humbled'),
        'humiliated':           _('Humiliated'),
        'hungry':                       _('Hungry'),
        'hurt':                         _('Hurt'),
        'impressed':            _('Impressed'),
        'in_awe':                       _('In Awe'),
        'in_love':                      _('In Love'),
        'indignant':            _('Indignant'),
        'interested':           _('Interested'),
        'intoxicated':          _('Intoxicated'),
        'invincible':           _('Invincible'),
        'jealous':                      _('Jealous'),
        'lonely':                       _('Lonely'),
        'lost':                         _('Lost'),
        'lucky':                                _('Lucky'),
        'mean':                         _('Mean'),
        'moody':                                _('Moody'),
        'nervous':                      _('Nervous'),
        'neutral':                      _('Neutral'),
        'offended':                     _('Offended'),
        'outraged':                     _('Outraged'),
        'playful':                      _('Playful'),
        'proud':                                _('Proud'),
        'relaxed':                      _('Relaxed'),
        'relieved':                     _('Relieved'),
        'remorseful':           _('Remorseful'),
        'restless':                     _('Restless'),
        'sad':                          _('Sad'),
        'sarcastic':            _('Sarcastic'),
        'satisfied':            _('Satisfied'),
        'serious':                      _('Serious'),
        'shocked':                      _('Shocked'),
        'shy':                          _('Shy'),
        'sick':                         _('Sick'),
        'sleepy':                       _('Sleepy'),
        'spontaneous':          _('Spontaneous'),
        'stressed':                     _('Stressed'),
        'strong':                       _('Strong'),
        'surprised':            _('Surprised'),
        'thankful':                     _('Thankful'),
        'thirsty':                      _('Thirsty'),
        'tired':                                _('Tired'),
        'undefined':            _('Undefined'),
        'weak':                         _('Weak'),
        'worried':                      _('Worried')}

ACTIVITIES = {
        'doing_chores': {'category':            _('Doing Chores'),
                'buying_groceries':                     _('Buying Groceries'),
                'cleaning':                             _('Cleaning'),
                'cooking':                              _('Cooking'),
                'doing_maintenance':                    _('Doing Maintenance'),
                'doing_the_dishes':                     _('Doing the Dishes'),
                'doing_the_laundry':                    _('Doing the Laundry'),
                'gardening':                            _('Gardening'),
                'running_an_errand':                    _('Running an Errand'),
                'walking_the_dog':                      _('Walking the Dog')},
        'drinking': {'category':                _('Drinking'),
                'having_a_beer':                         _('Having a Beer'),
                'having_coffee':                        _('Having Coffee'),
                'having_tea':                           _('Having Tea')},
        'eating': {'category':                  _('Eating'),
                'having_a_snack':                       _('Having a Snack'),
                'having_breakfast':                     _('Having Breakfast'),
                'having_dinner':                        _('Having Dinner'),
                'having_lunch':                         _('Having Lunch')},
        'exercising': {'category':              _('Exercising'),
                'cycling':                              _('Cycling'),
                'dancing':                              _('Dancing'),
                'hiking':                               _('Hiking'),
                'jogging':                              _('Jogging'),
                'playing_sports':                       _('Playing Sports'),
                'running':                              _('Running'),
                'skiing':                               _('Skiing'),
                'swimming':                             _('Swimming'),
                'working_out':                          _('Working out')},
        'grooming': {'category':                _('Grooming'),
                'at_the_spa':                           _('At the Spa'),
                'brushing_teeth':                       _('Brushing Teeth'),
                'getting_a_haircut':                    _('Getting a Haircut'),
                'shaving':                              _('Shaving'),
                'taking_a_bath':                        _('Taking a Bath'),
                'taking_a_shower':                      _('Taking a Shower')},
        'having_appointment': {'category':      _('Having an Appointment')},
        'inactive': {'category':                _('Inactive'),
                'day_off':                              _('Day Off'),
                'hanging_out':                          _('Hanging out'),
                'hiding':                               _('Hiding'),
                'on_vacation':                          _('On Vacation'),
                'praying':                              _('Praying'),
                'scheduled_holiday':                    _('Scheduled Holiday'),
                'sleeping':                             _('Sleeping'),
                'thinking':                             _('Thinking')},
        'relaxing': {'category':                _('Relaxing'),
                'fishing':                               _('Fishing'),
                'gaming':                                _('Gaming'),
                'going_out':                             _('Going out'),
                'partying':                              _('Partying'),
                'reading':                               _('Reading'),
                'rehearsing':                            _('Rehearsing'),
                'shopping':                              _('Shopping'),
                'smoking':                               _('Smoking'),
                'socializing':                           _('Socializing'),
                'sunbathing':                            _('Sunbathing'),
                'watching_tv':                           _('Watching TV'),
                'watching_a_movie':                      _('Watching a Movie')},
        'talking': {'category':                  _('Talking'),
                'in_real_life':                          _('In Real Life'),
                'on_the_phone':                          _('On the Phone'),
                'on_video_phone':                        _('On Video Phone')},
        'traveling': {'category':                _('Traveling'),
                'commuting':                             _('Commuting'),
                'cycling':                               _('Cycling'),
                'driving':                               _('Driving'),
                'in_a_car':                              _('In a Car'),
                'on_a_bus':                              _('On a Bus'),
                'on_a_plane':                            _('On a Plane'),
                'on_a_train':                            _('On a Train'),
                'on_a_trip':                             _('On a Trip'),
                'walking':                               _('Walking')},
        'working': {'category':                  _('Working'),
                'coding':                                _('Coding'),
                'in_a_meeting':                          _('In a Meeting'),
                'studying':                              _('Studying'),
                'writing':                               _('Writing')}}

LOCATION_DATA = {
        'accuracy':     _('accuracy'),
        'alt':          _('alt'),
        'area':         _('area'),
        'bearing':      _('bearing'),
        'building':     _('building'),
        'country':      _('country'),
        'countrycode':  _('countrycode'),
        'datum':        _('datum'),
        'description':  _('description'),
        'error':        _('error'),
        'floor':        _('floor'),
        'lat':          _('lat'),
        'locality':     _('locality'),
        'lon':          _('lon'),
        'postalcode':   _('postalcode'),
        'region':       _('region'),
        'room':         _('room'),
        'speed':        _('speed'),
        'street':       _('street'),
        'text':         _('text'),
        'timestamp':    _('timestamp'),
        'uri':          _('uri')}
