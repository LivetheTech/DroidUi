@echo off

REM Copyright (C) 2012-2014 Tommy Alex. All Rights Reserved.
REM
REM This program is free software: you can redistribute it and/or modify
REM it under the terms of the GNU General Public License as published by
REM the Free Software Foundation, either version 3 of the License, or
REM (at your option) any later version.
REM
REM This program is distributed in the hope that it will be useful,
REM but WITHOUT ANY WARRANTY; without even the implied warranty of
REM MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
REM GNU General Public License for more details.
REM
REM You should have received a copy of the GNU General Public License
REM along with this program.  If not, see <http://www.gnu.org/licenses/>

REM install.bat
REM install DroidUi in your Android device

set sl4a=/sdcard/sl4a/scripts/

call adb push DroidUi "%sl4a%DroidUi/"
call adb push examples "%sl4a%"

