# -*- coding: utf-8 -*-
#
# intent.py
# extract intent constants from android.content.Intent
#
# Copyright (C) 2012-2015 Tommy Alex. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Create: 2013-05-21 01:15


import DroidUi as Ui


# standard intent constants
# http://developer.android.com/reference/android/content/Intent.html

ACTION = (
	'ACTION_MAIN',
	'ACTION_VIEW',
	'ACTION_ATTACH_DATA',
	'ACTION_EDIT',
	'ACTION_PICK',
	'ACTION_CHOOSER',
	'ACTION_GET_CONTENT',
	'ACTION_DIAL',
	'ACTION_CALL',
	'ACTION_SEND',
	'ACTION_SENDTO',
	'ACTION_ANSWER',
	'ACTION_INSERT',
	'ACTION_DELETE',
	'ACTION_RUN',
	'ACTION_SYNC',
	'ACTION_PICK_ACTIVITY',
	'ACTION_SEARCH',
	'ACTION_WEB_SEARCH',
	'ACTION_FACTORY_TEST',
)

BROADCAST = (
	'ACTION_TIME_TICK',
	'ACTION_TIME_CHANGED',
	'ACTION_TIMEZONE_CHANGED',
	'ACTION_BOOT_COMPLETED',
	'ACTION_PACKAGE_ADDED',
	'ACTION_PACKAGE_CHANGED',
	'ACTION_PACKAGE_REMOVED',
	'ACTION_PACKAGE_RESTARTED',
	'ACTION_PACKAGE_DATA_CLEARED',
	'ACTION_UID_REMOVED',
	'ACTION_BATTERY_CHANGED',
	'ACTION_POWER_CONNECTED',
	'ACTION_POWER_DISCONNECTED',
	'ACTION_SHUTDOWN',
)

CATEGORY = (
	'CATEGORY_DEFAULT',
	'CATEGORY_BROWSABLE',
	'CATEGORY_TAB',
	'CATEGORY_ALTERNATIVE',
	'CATEGORY_SELECTED_ALTERNATIVE',
	'CATEGORY_LAUNCHER',
	'CATEGORY_INFO',
	'CATEGORY_HOME',
	'CATEGORY_PREFERENCE',
	'CATEGORY_TEST',
	'CATEGORY_CAR_DOCK',
	'CATEGORY_DESK_DOCK',
	'CATEGORY_LE_DESK_DOCK',
	'CATEGORY_HE_DESK_DOCK',
	'CATEGORY_CAR_MODE',
	'CATEGORY_APP_MARKET',
)

EXTRA = (
	'EXTRA_ALARM_COUNT',
	'EXTRA_BCC',
	'EXTRA_CC',
	'EXTRA_CHANGED_COMPONENT_NAME',
	'EXTRA_DATA_REMOVED',
	'EXTRA_DOCK_STATE',
	'EXTRA_DOCK_STATE_HE_DESK',
	'EXTRA_DOCK_STATE_LE_DESK',
	'EXTRA_DOCK_STATE_CAR',
	'EXTRA_DOCK_STATE_DESK',
	'EXTRA_DOCK_STATE_UNDOCKED',
	'EXTRA_DONT_KILL_APP',
	'EXTRA_EMAIL',
	'EXTRA_INITIAL_INTENTS',
	'EXTRA_INTENT',
	'EXTRA_KEY_EVENT',
	'EXTRA_ORIGINATING_URI',
	'EXTRA_PHONE_NUMBER',
	'EXTRA_REFERRER',
	'EXTRA_REMOTE_INTENT_TOKEN',
	'EXTRA_REPLACING',
	'EXTRA_SHORTCUT_ICON',
	'EXTRA_SHORTCUT_ICON_RESOURCE',
	'EXTRA_SHORTCUT_INTENT',
	'EXTRA_STREAM',
	'EXTRA_SHORTCUT_NAME',
	'EXTRA_SUBJECT',
	'EXTRA_TEMPLATE',
	'EXTRA_TEXT',
	'EXTRA_TITLE',
	'EXTRA_UID',
)

FLAG = (
	'FLAG_GRANT_READ_URI_PERMISSION',
	'FLAG_GRANT_WRITE_URI_PERMISSION',
	'FLAG_GRANT_PERSISTABLE_URI_PERMISSION',
	'FLAG_GRANT_PREFIX_URI_PERMISSION',
	'FLAG_DEBUG_LOG_RESOLUTION',
	'FLAG_FROM_BACKGROUND',
	'FLAG_ACTIVITY_BROUGHT_TO_FRONT',
	'FLAG_ACTIVITY_CLEAR_TASK',
	'FLAG_ACTIVITY_CLEAR_TOP',
	'FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET',
	'FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS',
	'FLAG_ACTIVITY_FORWARD_RESULT',
	'FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY',
	'FLAG_ACTIVITY_MULTIPLE_TASK',
	'FLAG_ACTIVITY_NEW_DOCUMENT',
	'FLAG_ACTIVITY_NEW_TASK',
	'FLAG_ACTIVITY_NO_ANIMATION',
	'FLAG_ACTIVITY_NO_HISTORY',
	'FLAG_ACTIVITY_NO_USER_ACTION',
	'FLAG_ACTIVITY_PREVIOUS_IS_TOP',
	'FLAG_ACTIVITY_RESET_TASK_IF_NEEDED',
	'FLAG_ACTIVITY_REORDER_TO_FRONT',
	'FLAG_ACTIVITY_SINGLE_TOP',
	'FLAG_ACTIVITY_TASK_ON_HOME',
	'FLAG_RECEIVER_REGISTERED_ONLY',
)


def intent():
	def write(file, dict, keys = None):
		if keys is None:
			keys = sorted(dict)
		for k in keys:
			try:
				v = dict[k]
			except KeyError:
				print('no such key:', k)
				continue
			try:
				v = int(v)
				if v > 10: v = hex(v)
				file.write('%s = %s\n' % (k, v))
			except:
				file.write('%s = \'%s\'\n' % (k, v))
			del dict[k]
		file.write('\n')
	f = open('intent.txt', 'w+')
	consts = Ui.Class('android.content.Intent').consts()
	for i in (ACTION, BROADCAST, CATEGORY, EXTRA, FLAG):
		write(f, consts, i)
	write(f, consts)
	f.close()


if __name__ == '__main__':
	intent()
