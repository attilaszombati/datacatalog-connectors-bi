#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The max length of a Data Catalog Entry ID.
ENTRY_ID_MAX_LENGTH = 64
# The below asset type specific strings are appended to the standard
# ENTRY_ID_PREFIX when generating Qlik Entry IDs.
ENTRY_ID_PART_APP = 'app_'
ENTRY_ID_PART_STREAM = 'str_'
# This is the common prefix for all Qlik Entries.
ENTRY_ID_PREFIX = 'qlik_'
# This constant represents the max length a generated Entry ID can have before
# appending the standard ENTRY_ID_PREFIX to it. The necessary right-most chars
# will be removed from a generated Entry ID if it has more chars than the value
# of this constant.
NO_PREFIX_ENTRY_ID_MAX_LENGTH = ENTRY_ID_MAX_LENGTH - len(ENTRY_ID_PREFIX)

# The ID of the Tag Template created to store additional metadata for
# App-related Entries.
TAG_TEMPLATE_ID_APP = 'qlik_app_metadata'
# The ID of the Tag Template created to store additional metadata for
# Stream-related Entries.
TAG_TEMPLATE_ID_STREAM = 'qlik_stream_metadata'

# The user specified type of App-related Entries.
USER_SPECIFIED_TYPE_APP = 'app'
# The user specified type of Stream-related Entries.
USER_SPECIFIED_TYPE_STREAM = 'stream'