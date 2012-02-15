# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012, Monash e-Research Centre
#   (Monash University, Australia)
# Copyright (c) 2010-2012, VeRSI Consortium
#   (Victorian eResearch Strategic Initiative, Australia)
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    *  Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#    *  Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    *  Neither the name of the VeRSI, the VeRSI Consortium members, nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
"""
models.py

.. moduleauthor:: Kieran Spear <kispear@gmail.com>
.. moduleauthor:: Shaun O'Keefe <shaun.okeefe.0@gmail.com>

"""

from django.db import models
from tardis.tardis_portal.models import Experiment
from tardis.apps.sync.consumer_fsm import ConsumerFSMField

#
# Maybe a common base class so we can turn anything into 
# a synced model?
#

class SyncedExperiment(Experiment):
    uid = models.IntegerField(default=0)
    state = ConsumerFSMField(default='Ingesting') 
    # Do we need to keep track of which provider this experiment came from?
    # provider = models.StringField()
    
    def __init__(self, *args, **kwargs):
        if 'state' in kwargs:
            self.state = kwargs['state']

        self.uid = 0
        super(SyncedExperiment, self).__init__(*args, **kwargs) 
    
    def is_complete(self):
        return self.state.is_final_state() 

        
