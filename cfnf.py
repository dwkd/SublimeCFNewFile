import sublime, sublime_plugin
import time

class cfnewfile(sublime_plugin.TextCommand):
	def run(self, edit):
		localtime = time.asctime( time.localtime(time.time()) )
		self.view.insert(edit,0,"<!---\r\n	Name:\r\n	Description:\r\n	Written By:\r\n	Date Created: "+localtime+"\r\n	History:\r\n--->\r\n")		
