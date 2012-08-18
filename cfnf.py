
import sublime, sublime_plugin
import time

class cfnfCommand(sublime_plugin.WindowCommand):
	def run(self):
		a = self.window.new_file()
		a.run_command("addheader")

class addheaderCommand(sublime_plugin.TextCommand):
	def run(self, edit):		
		localtime = time.asctime( time.localtime(time.time()) )
		self.view.insert(edit,0,"<!---\n	Name:\n	Description:\n	Written By:\n	Date Created: "+localtime+"\n	History:\n--->\n")		
