#!/usr/bin/env python3.7
################################################################################
# File:    main.py
# Purpose: This is the main wrapper script for launching the buskill app
#          For more info, see: https://buskill.in/
# Authors: Michael Altfield <michael@buskill.in>
# Created: 2020-06-23
# Updated: 2020-06-23
# Version: 0.1
################################################################################

# this is needed for supporting Windows 10 with OpenGL < v2.0
# Example: VirtualBox w/ OpenGL v1.1
import platform, os
if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

################################################################################
#                                   IMPORTS                                    #
################################################################################

import argparse, logging

################################################################################
#                                  SETTINGS                                    #
################################################################################

BUSKILL_VERSION = '0.1'

################################################################################
#                                  MAIN BODY                                   #
################################################################################

#################
# SETUP LOGGING #
#################

# TODO: disable logging by default; enable it with an argument
# TODO: be able to override the path to the log file with an env var or argument value; make these just the defaults
if platform.system() == 'Windows':
	log_file_path = os.path.join( 'buskill.log' )
else:
	log_file_path = os.path.join( os.sep, 'tmp', 'buskill.log' )

logging.basicConfig(
 filename = log_file_path,
 filemode = 'a',
 format = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
 datefmt = '%H:%M:%S',
 level = logging.DEBUG
)
logging.debug("===============================================================================")
logging.debug( 'os.environ|' +str(os.environ)+ '|' )

if __name__ == '__main__':

	logging.debug( "entered main" )

	msg = "buskill version " +str(BUSKILL_VERSION)
	print( msg ); logging.info( msg )

	####################
	# HANDLE ARGUMENTS #
	####################

	# we use ArgmentParser to handle the user's command-line arguents
	parser = argparse.ArgumentParser(
	 description  = 'App for arming and configuring BusKill.'
	)

	# process command-line arguments
	args = parser.parse_args()

	# did we get any command-line arguments?
	if args == argparse.Namespace():
		# we were given 0 command line arguments; just launch the GUI

		print( "No command-line arguments detected. Launching GUI" )
		print( "Hint: execute `buskill --help` for command-line usage" )

		from buskill_gui import *
		BusKill().run()

