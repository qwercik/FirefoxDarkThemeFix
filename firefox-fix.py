#!/usr/bin/env python3

import configparser
import os
import shutil

def get_profiles_list(firefox_files_path):
	profiles_list = []

	config = configparser.ConfigParser()
	config.read(firefox_files_path + '/profiles.ini')

	if not config:
		return profiles_list

	sections_list = config.sections()

	for section in sections_list:
		if 'Path' in config[section]:
			profiles_list.append(config[section]['Path'])

	return profiles_list

def fix_profile(firefox_files_path, profile_name, css_filename):
	css_directory = firefox_files_path + '/' + profile_name + '/chrome'

	if not os.path.isdir(css_directory):
		os.mkdir(css_directory)

	if not os.path.exists(css_filename):
		print('File', css_filename, 'not exist! Check if your repository clone isn\'t reject')
		return False

	shutil.copy(css_filename, css_directory)
	return True

def main():
	firefox_files_path = os.path.expanduser('~/.mozilla/firefox')
	if not os.path.isdir(firefox_files_path):
		print('I haven\'t found any Firefox installafion')

	profiles_list = get_profiles_list(firefox_files_path)
	css_filename = 'userContent.css'
	
	for profile in profiles_list:
		print('Fixing', profile, 'profile.')

		if not fix_profile(firefox_files_path, profile, css_filename):
			print('Couldn\'t fix', profile, 'profile')
	
	print('All profiles has been fixed')	
	
if __name__ == '__main__':
	main()
